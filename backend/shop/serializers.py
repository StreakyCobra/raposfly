# -*- coding: utf-8 -*-
"""Serializers for the shop application."""

from rest_framework import serializers

from .models import Category, Item, Purchase, Composition


class ItemSerializer(serializers.ModelSerializer):
    """Serializer for an Item."""

    class Meta:
        model = Item
        exclude = ()


class PurchaseItemSerializer(serializers.ModelSerializer):
    """Serializer for purchasing an Item."""

    quantity = serializers.IntegerField()

    class Meta:
        model = Item
        fields = ('name', 'price', 'quantity')


class CategorySerializer(serializers.ModelSerializer):
    """Serializer for a Category."""

    items = ItemSerializer(many=True, source='item_set')

    class Meta:
        model = Category
        exclude = ()


class CompositionSerializer(serializers.ModelSerializer):
    """Serializer for a Composition."""

    item = ItemSerializer()

    class Meta:
        model = Composition
        exclude = ()


class PurchaseSerializer(serializers.ModelSerializer):
    """Serializer for a Purchase."""

    items = CompositionSerializer(many=True, read_only=True,
                                  source='composition_set')

    class Meta:
        model = Purchase
        fields = ('id', 'date', 'items')
