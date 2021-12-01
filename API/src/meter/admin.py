# -*- coding: utf-8 -*-
# File: src/meter/admin.py
# Date: 2021-12-01 15:31
# Author: Kenson Man <kenson@kenson.idv.hk>
# Usage: Provide the admin-tools for debug and testing
from django.contrib import admin
from .models import *

@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
   fields         = ('id', 'customerId', 'serialNumber', 'meterType', 'meterPointNumber', 'readingType', 'registerId', 'value', 'parent', 'readDate')
   list_display   = ('id', 'customerId', 'serialNumber', 'meterType', 'meterPointNumber', 'readingType', 'registerId', 'value', 'parent', 'readDate')
   list_filter    = ('meterType', 'readingType', 'readDate')
   ordering       = ('-readDate',)
   readonly_fields=('id', 'readDate', 'parent',)
   search_field   =('id', 'customerId', 'serialNumber', 'meterPointNumber', 'registerId', 'value', 'readDate', 'parnet')

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
   fields         = ('id', 'data', 'ipaddr', 'date', 'stored')
   list_display   = ('id', 'data', 'ipaddr', 'date', 'stored')
   list_filter    = ('ipaddr', 'date')
   ordering       = ('-date',)
   readonly_fields=('id', 'date', 'stored')
   search_field   =('id', 'data', 'ipaddr', 'date', 'stored')
