# -*- coding: utf-8 -*-
"""URLs for the shop application."""
from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'purchases', views.PurchaseViewSet)

urlpatterns = [
    url(r'^buy/', views.BuyView.as_view()),
    url(r'^stats/', views.StatsView.as_view()),
    url(r'^history/', views.HistoryView.as_view()),
    url(r'^store/', views.StoreView.as_view()),
    url(r'^config/', views.ConfigView.as_view()),
]

urlpatterns += router.urls
