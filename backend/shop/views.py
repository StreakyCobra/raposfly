# -*- coding: utf-8 -*-
"""Views for the shop application."""

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Item
from .serializers import ItemSerializer


class ListItems(APIView):
    """List the items in the shop."""

    def get(self, request):
        """GET request to access the list of items in the shop."""
        items = Item.objects.all()
        return Response(ItemSerializer(items, many=True).data)
