# -*- coding: utf-8 -*-
"""URLs for the shop application."""
from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'purchases', views.PurchaseViewSet)

urlpatterns = [
    url(r'^shop-items/', views.ShopItemsView.as_view()),
    url(r'^do-purchase/', views.DoPurchaseItemsView.as_view()),
    url(r'^shop-stats/', views.ShopStatsView.as_view()),
]

urlpatterns += router.urls
