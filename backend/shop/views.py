# -*- coding: utf-8 -*-
"""Views for the shop application."""

from django.db.models import Sum, Count
from django.utils import timezone
from escpos.exceptions import Error, USBNotFoundError
from escpos.printer import Usb
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .models import Category, Composition, Item, Purchase
from .tickets import print_ticket, print_total


class ListItems(APIView):
    """List the items of the shop."""

    def get(self, request):
        """GET request to access the list of items of the shop."""
        categories = Category.objects.all()
        return Response(serializers.CategorySerializer(categories,
                                                       many=True).data)


class ListPurchases(APIView):
    """List the purchases of the shop."""

    def get(self, request):
        """GET request to access the list of purchases of the shop."""
        purchases = Purchase.objects.order_by('date').reverse()
        serialized = serializers.PurchaseSerializer(purchases, many=True)
        return Response(serialized.data)


class PurchaseView(APIView):
    """Access a purchases of the shop."""

    def delete(self, request, purchase_id):
        """DELETE request to delete a purchases of the shop."""
        try:
            Purchase.objects.get(pk=purchase_id).delete()
        except Purchase.DoesNotExist:
            return Response("Purchase does not exist", status=400)
        return Response("Purchase deleted")


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
        total = 0
        for item in sent_items:
            try:
                item = Item.objects.get(name=item['name'], price=item['price'])
                total += item.price
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
            # Each ticket
            for item in items:
                print_ticket(printer, item)
            print_total(printer, items, total)
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


class Stats(APIView):
    """The stats of the shop."""

    def get(self, request):
        """GET request to access the stats of the shop."""
        stats = dict()

        # ------------------------------------------------------------------- #
        # Total sales                                                         #
        # ------------------------------------------------------------------- #

        total_sales = Composition.objects.aggregate(Sum('price'))
        stats['total_sales'] = total_sales['price__sum']

        # ------------------------------------------------------------------- #
        # Cumulative Sales                                                   #
        # ------------------------------------------------------------------- #

        purchases = Purchase.objects.annotate(total=Sum('items__price'))
        running_total = 0
        stats['cumulative_sales'] = []
        for p in purchases:
            running_total += p.total
            stats['cumulative_sales'].append({'x': int(p.date.timestamp()),
                                              'y': running_total})

        # ------------------------------------------------------------------- #
        # Count                                                               #
        # ------------------------------------------------------------------- #

        items = Item.objects.annotate(count=Count('items_set'))
        stats['counts'] = dict()
        stats['counts']['labels'] = [i.name for i in items]
        stats['counts']['series'] = [i.count for i in items]

        return Response(stats)
