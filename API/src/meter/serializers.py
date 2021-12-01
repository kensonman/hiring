# -*- coding: utf-8 -*-
# File: src/meter/serializers.py
# Date: 2021-12-01 15:52
# Author: Kenson Man <kenson@kenson.idv.hk>
# Usage: Provide the JSON Serializers
from .models import *
from rest_framework import serializers

class ReadingSerializer(serializers.ModelSerializer):
   class Meta:
      model = Reading 
      fields = ['id', 'customerId', 'serialNumber', 'meterType', 'readingType', 'registerId', 'value', 'readDate']
