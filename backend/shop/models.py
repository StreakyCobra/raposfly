# -*- coding: utf-8 -*-
"""Models for the shop application."""

from django.db import models


class Item(models.Model):
    """An item in the shop."""

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        """Return the string representation of an Item."""
        return "{name}".format(**self.__dict__)
