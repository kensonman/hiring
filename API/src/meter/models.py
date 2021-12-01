# -*- coding: utf-8 -*-
# File: src/meter/model.py
# Date: 2021-12-01 15:08
# Author: Kenson Man <kenson@kenson.idv.hk>
# Usage: Create the data-model for the bluetel/hiring/API 
from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext as __
import uuid

class Reading(models.Model):
   '''
   The model to store the reading that submitted by user/meter. It is also used for query the result.

   Provided Schema
   ====
   {
      "customerId": "identifier123",
      "serialNumber": "27263927192",
      "mpxn": "14582749",
      "read": [
         {"type": "ANYTIME", "registerId": "387373", "value": "2729"},
         {"type": "NIGHT", "registerId": "387373", "value": "2892"}
      ],
      "readDate": "2017-11-20T16:19:48+00:00Z"
   }

   I had denormalized the "read" property. It will make the program lighter and easy to maintenance.
   '''
   class Meta(object):
      verbose_name         =_('meter.Reading')
      verbose_name_plural  =_('meter.Readings')

   METER_ELECTRIC = 0
   METER_GAS      = 1
   METER_TYPES    = (
      (METER_ELECTRIC, _('meter.types.electric')),
      (METER_GAS, _('meter.types.gas')),
   )

   id             = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_('meter.Reading.id'), help_text=_('meter.Reading.id.helptext'))
   customerId     = models.CharField(max_length=50, verbose_name=_('meter.Reading.customerId'), help_text=_('meter.Reading.customerId.helptext'))
   serialNumber   = models.CharField(max_length=50, verbose_name=_('meter.Reading.serialNumber'), help_text=_('meter.Reading.serialNumber.helptext'))
   meterType      = models.IntegerField(choices=METER_TYPES, default=METER_ELECTRIC, verbose_name=_('meter.Reading.meterType'), help_text=_('meter.Reading.meterType.helptext'))
   meterPointNumber= models.CharField(max_length=50, verbose_name=_('meter.Reading.meterPointNumber'), help_text=_('meter.Reading.meterPointNumber.helptext'))
   readingType    = models.CharField(max_length=20, verbose_name=_('meter.Reading.readingType'), help_text=_('meter.Reading.readingType.helptext'))
   registerId     = models.CharField(max_length=20, verbose_name=_('meter.Reading.registerId'), help_text=_('meter.Reading.registerId.helptext'))
   value          = models.IntegerField(verbose_name=_('meter.Reading.value'), help_text=_('meter.Reading.value.helptext'))
   parent         = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, verbose_name=_('meter.Reading.parent'), help_text=_('meter.Reading.parent.helptext'))
   readDate       = models.DateTimeField(verbose_name=_('meter.Reading.readDate'), help_text=_('meter.Reading.readDate.helptext'))

class History(models.Model):
   '''
   The model to store as the history or audit check.

   In the business envirnonment, the raw-data is so important and we cannot accept any error on it. So that I created this model
   to store all the raw-data (that user just submit the data). It also provide the ability to found out the issue if there have any 
   error/unexpected result.

   The id is also used for idempotency check to reduce any re-submit issue.
   '''
   class Meta(object):
      verbose_name         =_('meter.History')
      verbose_name_plural  =_('meter.Histories')

   id             = models.CharField(max_length=100, primary_key=True, verbose_name=_('meter.History.id'), help_text=_('meter.History.id.helptext'))
   data           = models.JSONField(verbose_name=_('meter.History.data'), help_text=_('meter.History.data.helptext'))
   ipaddr         = models.CharField(max_length=40, verbose_name=_('meter.History.ipaddr'), help_text=_('meter.History.ipaddr.helptext'))
   date           = models.DateTimeField(auto_now=True, verbose_name=_('meter.History.date'), help_text=_('meter.History.date.helptext'))
   stored         = models.ForeignKey(Reading, null=True, blank=True, verbose_name=_('meter.History.stored'), help_text=_('meter.History.stored.helptext'), on_delete=models.SET_NULL)
