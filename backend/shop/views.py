# -*- coding: utf-8 -*-
"""Views for the shop application."""

from django.utils import timezone
from escpos.exceptions import Error, USBNotFoundError
from escpos.printer import Usb
from itertools import groupby
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .models import Item, Purchase, Composition


class ListItems(APIView):
    """List the items of the shop."""

    def get(self, request):
        """GET request to access the list of items of the shop."""
        items = Item.objects.all()
        return Response(serializers.ItemSerializer(items, many=True).data)


class ListPurchases(APIView):
    """List the purchases of the shop."""

    def get(self, request):
        """GET request to access the list of purchases of the shop."""
        purchases = Purchase.objects.order_by('date').reverse()
        serialized = serializers.PurchaseSerializer(purchases, many=True)
        return Response(serialized.data)


class PurchaseItems(APIView):
    """Purchase items in the shop."""

    serializer_class = serializers.ItemSerializer

    def post(self, request):
        """POST request to purcharse items in the shop."""
        serializer = self.serializer_class(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        sent_items = serializer.validated_data

        # ------------------------------------------------------------------- #
        # Verify that items are valid and haven't changed                     #
        # ------------------------------------------------------------------- #

        items = []
        for item in sent_items:
            try:
                item = Item.objects.get(**item)
            except Item.DoesNotExist:
                return Response({'status': 'Some items are not valid or '
                                           'have changed in the database.'},
                                status=400)
            items.append(item)

        # ------------------------------------------------------------------- #
        # Print the tickets                                                   #
        # ------------------------------------------------------------------- #

        try:
            printer = Usb(0x04b8, 0x0e02)
            pass
        except USBNotFoundError:
            return Response({'status': 'Impossible to connect to the '
                                       'printer.'},
                            status=400)

        try:
            for item in items:
                print(item.pk)
                printer.text('{name} ({price} CHF)\n'.format(**item))
                printer.cut()
        except Error:
            return Response({'status': 'Impossible to print the tickets'},
                            status=400)

        # ------------------------------------------------------------------- #
        # Store the purchasñe                                                 #
        # ------------------------------------------------------------------- #

        purchase = Purchase(date=timezone.now())
        purchase.save()
        for item in items:
            Composition(item=item, purchase=purchase, price=item.price).save()

        return Response({'status': 'ok'})
