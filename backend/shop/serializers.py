# -*- coding: utf-8 -*-
# pylint: disable=abstract-method
"""Serializers for the shop application."""

from rest_framework import serializers

from .models import Category, Order, Item, Purchase


class ItemSerializer(serializers.ModelSerializer):
    """Serializer for an Item."""

    image = serializers.FileField(source='image_item_or_categorie')

    class Meta:
        model = Item
        exclude = ()


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for a Category."""

    items = ItemSerializer(many=True, read_only=True, source='item_set')

    class Meta:
        model = Category
        exclude = ()


class PurchaseSerializer(serializers.ModelSerializer):
    """Serializer for a Purchase."""

    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        model = Purchase
        exclude = ()


class OrderSerializer(serializers.ModelSerializer):
    """Serializer for a composition."""

    item = ItemSerializer(read_only=True)

    class Meta:
        model = Order
        exclude = ('purchase',)


class HistorySerializer(serializers.ModelSerializer):
    """Serializer for purchases history."""

    orders = OrderSerializer(many=True, read_only=True)

    class Meta:
        model = Purchase
        exclude = ('items',)


class OrderSerializer(serializers.Serializer):
    """Serializer for buying a given quantity of an item."""

    item_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class BuySerializer(serializers.Serializer):
    """Serializer for doing a purchase."""

    orders = OrderSerializer(many=True)
    receipt = serializers.BooleanField()


class PrintReceiptSerializer(serializers.Serializer):
    """Serializer for printing a receipt."""

    purchase_id = serializers.IntegerField()
