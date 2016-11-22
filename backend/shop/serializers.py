# -*- coding: utf-8 -*-
"""Serializers for the shop application."""

from rest_framework import serializers

from .models import Category, Item, Purchase, Composition


class ItemSerializer(serializers.ModelSerializer):
    """Serializer for an Item."""

    class Meta:
        model = Item
        exclude = ()


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for a Category."""

    items = ItemSerializer(many=True, source='item_set')

    class Meta:
        model = Category
        exclude = ()


class PurchaseSerializer(serializers.ModelSerializer):
    """Serializer for a Purchase."""

    items = ItemSerializer(many=True)

    class Meta:
        model = Purchase
        exclude = ()


class CompositionSerializer(serializers.ModelSerializer):
    """Serializer for a Composition."""

    item = ItemSerializer()
    purchase = PurchaseSerializer()

    class Meta:
        model = Composition
        exclude = ()


class HistorySerializer(serializers.ModelSerializer):
    """Serializer for purchase history."""

    items = CompositionSerializer(many=True, read_only=True,
                                  source='composition_set')

    class Meta:
        model = Purchase
        fields = ('id', 'date', 'items')


class DoPurchaseItemSerializer(serializers.Serializer):
    """Serializer for purchasing an Item."""

    item = ItemSerializer()
    quantity = serializers.IntegerField()
