# -*- coding: utf-8 -*-
# File: src/meter/views.py
# Date: 2021-12-01 15:55
# Author: Kenson Man <kenson@kenson.idv.hk>
# Usage: Provide the view for meter project
from datetime import datetime
from django.db import transaction
from django.shortcuts import render, get_object_or_404 as getObj
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import ReadingSerializer
import logging

logger=logging.getLogger('meter.ReadingView')

class ReadingView(APIView):
   
   def get_queryset(self):
      return Reading.objects.all()

   def getClientIP( self, req ):
      '''
      Get the client ip address

      @param req The request;
      '''
      if callable(req): req=req()
      xForwardedFor=req.META.get('HTTP_X_FORWARDED_FOR')
      if xForwardedFor:
         ip=xForwardedFor.split(',')[0]
      else:
         ip=req.META.get('REMOTE_ADDR')
      return ip

   def get(self, req, format=None):
      target=self.get_queryset()
      if 'customerId' in req.GET: target=target.filter(customerId__contains=req.GET['customerId'])
      if 'serialNumber' in req.GET: target=target.filter(serialNumber__contains=req.GET['serialNumber'])
      if 'mpan' in req.GET: target=target.filter(meterType=Reading.METER_ELECTRIC, meterPointNumber__contains=req.GET['mpan'])
      if 'mprn' in req.GET: target=target.filter(meterType=Reading.METER_GAS, meterPointNumber__contains=req.GET['mprn'])
      if 'GAS'==req.GET.get('meterType', None):target=target.filter(meterType=Reading.METER_GAS)
      if 'ELECTRIC'==req.GET.get('meterType', None):target=target.filter(meterType=Reading.METER_ELECTRIC)
      if 'readingType' in req.GET: target=target.filter(readingType=req.GET['readingType'])
      if 'registerId' in req.GET: target=target.filter(registerId__contains=req.GET['registerId'])
      target=target.order_by(*req.GET.get('ordering', '-readDate').split(','))
      return Response(ReadingSerializer(target, many=True).data)

   def post(self, req, format=None):
      raise RuntimeError('Not implemented yet')

   def delete(self, req, format=None):
      raise RuntimeError('Not implemented yet')

   def put(self, req, format=None):
      data=req.data
      with transaction.atomic():
         #Idempotency check
         hid=req.headers.get('Idempotency-Key', uuid.uuid4())
         logger.debug('Idempotency-Key: %s'%hid)
         history=None
         try:
            history=History.objects.get(id=hid)
            logger.debug('loaded the saved reading')
            ids=[]
            ids.append(str(history.stored.id))
            for ch in Reading.objects.filter(parent=history.stored):
               ids.append(str(ch.id))
            logger.info(ids)
            return Response(ids)
         except History.DoesNotExist:
            logger.debug('going to create new reading')
         history=History(id=hid, data=data, ipaddr=self.getClientIP(req))#Save the history
         history.save()

         ids=[]
         parent=None
         target=getObj(Reading, id=data['id']) if 'id' in data else Reading()
         target.customerId=data['customerId']
         target.serialNumber=data['serialNumber']
         if 'mpan' in data:
            target.meterType=Reading.METER_ELECTRIC
            target.meterPointNumber=data['mpan']
         else:
            target.meterType=Reading.METER_GAS
            target.meterPointNumber=data.get('mprn', data.get('mpxn', None))
         time=data['readDate']
         if time.endswith('z') or time.endswith('Z'):time=time[:-1]
         target.readDate=datetime.fromisoformat(time)
         for rd in data['read']:
            if parent:
               target.parent=parent
            target.id=None
            target.readingType=rd['type']
            target.registerId=rd['registerId']
            target.value=int(rd['value'])
            target.save()
            if not parent:
               parent=Reading.objects.get(id=target.id)
               history.stored=parent
               history.save()
            ids.append(str(target.id))
         return Response(ids)
