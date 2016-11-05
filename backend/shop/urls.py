# -*- coding: utf-8 -*-
"""URLs for the shop application."""
from django.conf.urls import url

from .views import ListItems

urlpatterns = [
    url(r'^items/', ListItems.as_view()),
]
