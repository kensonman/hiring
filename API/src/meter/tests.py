# -*- coding: utf-8 -*-
# File: src/meter/tests.py
# Date: 2021-12-01 16:20
# Author: Kenson Man <kenson@kenson.idv.hk>
# Usage: Provide the test case
from django.test import TestCase
from rest_framework.test import APIClient
from .models import *
import logging, json

class ReadingTestCases(TestCase):
   def setUp(self):
      self.logger=logging.getLogger('test.meter.ReadingTestCases')
      self.factory=APIClient()
      self.URL='/meter-read'

   def test_00_list_emtpy_reading(self):
      '''
      Before all tests, make sure the framework is running as normal. It will be done by make a simple query, it should return a empty list due to no data has been created.
      '''
      self.logger.info('Listing the empty reading...')
      rep=self.factory.get(self.URL)
      self.logger.debug('Result: %s'%rep.status_code)
      self.assertTrue(200 <= rep.status_code < 300)
   
   def test_01_crud(self):
      '''
      Test the simple Create/Read/Update/Delete method.

      Due to the requirement, the update and delete is not necessary.
      - read - It will return a list of Reading object (in JSON format).
      - create - It will save the reading object and return the saved ids. Due to the denormalization, the provided sample will save into two separated reading.
      '''
      self.logger.info('Saving the sample into testing database...')
      sample=None
      with open('sample.json', 'r') as fp:
         sample=json.loads(fp.read())
         self.logger.debug('Sample: ')
         self.logger.debug(sample)

      #Create - The post method is used to create. Returns a list of array that created reading
      rep=self.factory.post(self.URL, json.dumps(sample), content_type="application/json")
      self.logger.debug('Result: %s'%rep.status_code)
      self.logger.debug(rep.data)
      self.assertTrue(200 <= rep.status_code < 300)#Status code
      self.assertIsInstance(rep.data, list)
      self.assertTrue(len(rep.data)==2)
      savedId=rep.data

      #Read
      self.logger.debug('Checking the saved instance...')
      rep=self.factory.get(self.URL)
      self.assertTrue(200 <= rep.status_code < 300)#Status code
      self.logger.debug(rep.data)
      for d in rep.data:
         self.assertTrue(d['id'] in savedId)
         self.assertTrue(d['customerId']==sample['customerId'])
         self.assertTrue(d['serialNumber']==sample['serialNumber'])

      #Update
      #   Not supported

      #Delete
      #   Not supported
      Reading.objects.all().delete() #clean up the testing

   def test_02_query(self):
      self.logger.info('Testing the query feature...')
      sample=None
      with open('sample.json', 'r') as fp:
         sample=json.loads(fp.read())
         self.logger.debug('Sample: ')
         self.logger.debug(sample)

      #Create - The post method is used to create. Returns a list of array that created reading
      rep=self.factory.post(self.URL, json.dumps(sample), content_type="application/json")
      self.logger.debug('Result: %s'%rep.status_code)
      self.logger.debug(rep.data)
      self.assertTrue(200 <= rep.status_code < 300)#Status code
      self.assertIsInstance(rep.data, list)
      self.assertTrue(len(rep.data)==2)
      savedId=rep.data

      rep=self.factory.get(self.URL, {'customerId': 'ident'})
      self.assertTrue(200 <= rep.status_code < 300)#Status code
      self.assertIsInstance(rep.data, list)
      self.assertTrue(len(rep.data)==2)

      rep=self.factory.get(self.URL, {'customerId': 'abcde'})
      self.assertTrue(200 <= rep.status_code < 300)#Status code
      self.assertIsInstance(rep.data, list)
      self.assertTrue(len(rep.data)==0)

      rep=self.factory.get(self.URL, {'mprn': '1458'})
      self.assertTrue(200 <= rep.status_code < 300)#Status code
      self.assertIsInstance(rep.data, list)
      self.assertTrue(len(rep.data)==2)

      rep=self.factory.get(self.URL, {'mpan': '1458'})
      self.assertTrue(200 <= rep.status_code < 300)#Status code
      self.assertIsInstance(rep.data, list)
      self.assertTrue(len(rep.data)==0)

      rep=self.factory.get(self.URL, {'meterType': 'GAS'})
      self.assertTrue(200 <= rep.status_code < 300)#Status code
      self.assertIsInstance(rep.data, list)
      self.assertTrue(len(rep.data)==2)

      rep=self.factory.get(self.URL, {'meterType': 'ELECTRIC'})
      self.assertTrue(200 <= rep.status_code < 300)#Status code
      self.assertIsInstance(rep.data, list)
      self.assertTrue(len(rep.data)==0)

      rep=self.factory.get(self.URL, {'readingType': 'ANYTIME'})
      self.assertTrue(200 <= rep.status_code < 300)#Status code
      self.assertIsInstance(rep.data, list)
      self.assertTrue(len(rep.data)==1)
