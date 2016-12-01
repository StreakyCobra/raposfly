# -*- coding: utf-8 -*-
# pylint: disable=too-many-ancestors
"""Views for the shop application."""

from constance import config
from django.db.models import Count, Sum
from django.utils import timezone
from escpos.exceptions import Error, USBNotFoundError
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .models import Category, Composition, Item, Purchase


class ItemViewSet(viewsets.ModelViewSet):
    """Item viewset of the shop."""

    serializer_class = serializers.ItemSerializer
    queryset = Item.objects.all()


class PurchaseViewSet(viewsets.ModelViewSet):
    """Purchase viewset of the shop."""

    serializer_class = serializers.HistorySerializer
    queryset = Purchase.objects.all()


class StoreView(APIView):
    """List the items of the shop grouped by categories."""

    serializer_class = serializers.CategorySerializer

    def get(self, request):
        """GET request for items of the shop grouped by categories."""
        categories = [c for c in Category.objects.all() if c.item_set.all()]
        return Response(self.serializer_class(categories, many=True).data)


class HistoryView(APIView):
    """List the history of purchases of the shop."""

    serializer_class = serializers.HistorySerializer

    def get(self, request):
        """GET request for the list the history of purchases of the shop."""
        purchases = Purchase.objects.all()
        return Response(self.serializer_class(purchases, many=True).data)


class BuyView(APIView):
    """Buy items in the shop."""

    serializer_class = serializers.BuySerializer

    def post(self, request):
        """POST request to purcharse items in the shop."""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        orders = serializer.validated_data['orders']
        receipt = serializer.validated_data['receipt']

        # ------------------------------------------------------------------- #
        # Verify that items are valid and haven't changed                     #
        # ------------------------------------------------------------------- #

        items = []
        for order in orders:
            try:
                item = Item.objects.get(id=order['item_id'])
            except Item.DoesNotExist:
                return Response({'status': 'Some items are not valid or '
                                           'have changed in the database.'},
                                status=400)
            items.append((item, order['quantity']))

        # ------------------------------------------------------------------- #
        # Print the tickets                                                   #
        # ------------------------------------------------------------------- #

        try:
            pass
            # printer = Usb(0x04b8, 0x0e15)
        except USBNotFoundError:
            return Response({'status': 'Impossible to connect to the '
                                       'printer.'},
                            status=400)

        try:
            # Each ticket
            pass
            # for (item, quantity) in items:
            #     print_ticket(printer, item)
            #     total += item.price * quantity
            # if receipt:
            #     print_total(printer, items, total)
        except Error:
            return Response({'status': 'Impossible to print the tickets'},
                            status=400)

        # ------------------------------------------------------------------- #
        # Store the purchasñe                                                 #
        # ------------------------------------------------------------------- #

        purchase = Purchase(date=timezone.now())
        purchase.save()
        for (item, quantity) in items:
            Composition(item=item,
                        purchase=purchase,
                        price=item.price,
                        quantity=quantity).save()

        return Response({'status': 'ok'})


class StatsView(APIView):
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

        purchases = Purchase.objects.order_by('date')\
                                    .annotate(total=Sum('items__price'))
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


class ConfigView(APIView):
    """The config of the shop."""

    def get(self, request):
        """GET request to access the configuration of the shop."""
        keys = list(config.__dir__())
        confs = {k: config.__getattr__(k) for k in keys}
        return Response(confs)
