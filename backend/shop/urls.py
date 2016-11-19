# -*- coding: utf-8 -*-
"""URLs for the shop application."""
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^items/', views.ListItems.as_view()),
    url(r'^purchase/', views.PurchaseItems.as_view()),
    url(r'^purchases/', views.ListPurchases.as_view()),
    url(r'^stats/', views.Stats.as_view()),
]
