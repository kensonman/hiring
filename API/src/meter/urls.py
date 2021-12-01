# -*- coding: utf-8 -*-
# File: src/meter/urls.py
# Date: 2021-12-01 16:02
# Author: Kenson Man <kenson@kenson.idv.hk>
# Usage: Provide the URL mapping
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import ReadingView


urlpatterns = [
   path('meter-read', ReadingView.as_view(), name='meter-read')
]
