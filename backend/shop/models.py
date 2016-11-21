# -*- coding: utf-8 -*-
"""Models for the shop application."""

from django.db import models
from colorful.fields import RGBColorField
from .utils import UploadHashedTo


class Category(models.Model):
    """A category of the shop."""

    name = models.CharField(max_length=255)
    order = models.IntegerField(default=9999)

    def __str__(self):
        """Return the string representation of a Category."""
        return "{name}".format(**self.__dict__)

    class Meta:
        ordering = ('order',)
        verbose_name_plural = "Categories"


class Item(models.Model):
    """An item of the shop."""

    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    image = models.FileField(blank=True, null=True,
                             upload_to=UploadHashedTo('items'))
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    color = RGBColorField(blank=True, null=True, default="#ffffff")
    order = models.IntegerField(default=9999)

    def __str__(self):
        """Return the string representation of an Item."""
        return "{name}".format(**self.__dict__)

    class Meta:
        ordering = ('order',)


class Purchase(models.Model):
    """A purchase in the shop."""

    items = models.ManyToManyField(Item, through='Composition')
    date = models.DateTimeField()

    def __str__(self):
        """Return the string representation of a Purchase."""
        return "{id} - {date}".format(**self.__dict__)

    class Meta:
        ordering = ('date',)


class Composition(models.Model):
    """The composition of a purchase in the shop."""

    item = models.ForeignKey(Item, related_name='items_set')
    purchase = models.ForeignKey(Purchase)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        """Return the string representation of a Composition."""
        return "{} | {}".format(self.purchase, self.item)
