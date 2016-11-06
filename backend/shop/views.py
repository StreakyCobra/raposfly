# -*- coding: utf-8 -*-
"""Views for the shop application."""

from escpos.exceptions import Error, USBNotFoundError
from escpos.printer import Usb
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Item
from .serializers import ItemSerializer


class ListItems(APIView):
    """List the items in the shop."""

    def get(self, request):
        """GET request to access the list of items in the shop."""
        items = Item.objects.all()
        return Response(ItemSerializer(items, many=True).data)


class PurchaseItems(APIView):
    """Purchase items in the shop."""

    serializer_class = ItemSerializer

    def post(self, request):
        """POST request to purcharse items in the shop."""
        serializer = self.serializer_class(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)

        sent_items = serializer.validated_data
        items = []

        # ------------------------------------------------------------------- #
        # Verify that items are valid and haven't changed                     #
        # ------------------------------------------------------------------- #

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

        return Response({'status': 'ok'})
