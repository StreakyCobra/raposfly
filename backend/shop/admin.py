# -*- coding: utf-8 -*-
"""Admin for the shop application."""

from django.contrib import admin

from .models import Category, Composition, Item, Purchase

admin.site.register(Category)
admin.site.register(Composition)
admin.site.register(Item)
admin.site.register(Purchase)
