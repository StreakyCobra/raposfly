# -*- coding: utf-8 -*-
"""Serializers for the shop application."""

from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    """Serializer for an Item."""

    class Meta:
        model = Item
        exclude = ()
