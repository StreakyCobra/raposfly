# -*- coding: utf-8 -*-
"""Models for the shop application."""

from colorful.fields import RGBColorField
from constance import config
from django.db import models

from .utils import UploadHashedTo


class Category(models.Model):
    """A category of the shop."""

    name = models.CharField(max_length=255)
    image = models.FileField(blank=True, null=True,
                             upload_to=UploadHashedTo('categories'))
    color = RGBColorField(blank=True, null=True, default="#000000")
    order = models.IntegerField(default=9999)

    def clean(self):
        """Clean the model."""
        if self.color == '#000000':
            self.color = None

    def color_categorie_or_default(self):
        """Return the color of the item or of category if not existing."""
        if self.color:
            return self.color
        return config.DEFAULT_ITEM_COLOR

    def __str__(self):
        """Return the string representation of a Category."""
        return "{name}".format(**self.__dict__)

    class Meta:
        ordering = ('order',)
        verbose_name_plural = "Categories"


class Item(models.Model):
    """An item of the shop."""

    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category)
    image = models.FileField(blank=True, null=True,
                             upload_to=UploadHashedTo('items'))
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    color = RGBColorField(blank=True, null=True, default="#000000")
    individual_tickets = models.BooleanField(
        verbose_name="Print individual ticket", default=True)
    group_tickets = models.BooleanField(
        verbose_name="Group individuals tickets in one", default=False)
    order = models.IntegerField(default=9999)

    def image_item_or_categorie(self):
        """Return the image of the item or of category if not existing."""
        if self.image:
            return self.image
        return self.category.image

    def color_item_or_categorie(self):
        """Return the color of the item or of category if not existing."""
        if self.color:
            return self.color
        return self.category.color_categorie_or_default()

    def clean(self):
        """Clean the model."""
        if self.color == '#000000':
            self.color = None

    def __str__(self):
        """Return the string representation of an Item."""
        return "{name}".format(**self.__dict__)

    class Meta:
        ordering = ('order',)


class Purchase(models.Model):
    """A purchase in the shop."""

    items = models.ManyToManyField(Item, through='Order')
    date = models.DateTimeField()

    def __str__(self):
        """Return the string representation of a Purchase."""
        return "{id} - {date}".format(**self.__dict__)

    class Meta:
        ordering = ('-date',)


class Order(models.Model):
    """An order in the shop."""

    item = models.ForeignKey(Item, related_name='orders')
    purchase = models.ForeignKey(Purchase, related_name='orders')
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        """Return the string representation of a Order."""
        return "{} | {}".format(self.purchase, self.item)
