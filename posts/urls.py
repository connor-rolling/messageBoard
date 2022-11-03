#!/usr/bin/env python
__author__ = "Connor Rolling"

from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]