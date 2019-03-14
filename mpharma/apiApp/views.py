from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from .serializers import CdicodeSerializer
from rest_framework.pagination import PageNumberPagination

from rest_framework import viewsets
from apiApp.models import icdCode 
# import requests
from celery.decorators import task


import csv
import urllib
from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task






class LargeResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 10000


class CdicodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed,edited,delete.
    """
    queryset = icdCode.objects.all().order_by('-full_code')
    serializer_class = CdicodeSerializer
    pagination_class = LargeResultsSetPagination



# """
# Function that reads the csv file from github and update the database every 15 minutes.
# """
@shared_task
@periodic_task(run_every=(crontab(minute='*/5')))
def CsvView():
	
	data = "https://raw.githubusercontent.com/kamillamagna/ICD-10-CSV/master/codes.csv"
	webpage = urllib.urlopen(data)
	datareader = csv.reader(webpage)

	for row in datareader:
		check=icdCode.objects.filter(category_code=row[0],diagnosis_code=row[1],full_code=row[2],abbreviated_description=row[3],full_description=row[4],category_title=row[5]).count()
		if check<1:
			icd=icdCode()
			icd.category_code=row[0]
			icd.diagnosis_code=row[1]
			icd.full_code=row[2]
			icd.abbreviated_description=row[3]
			icd.full_description=row[4]
			icd.category_title=row[5]
			icd.save()
	return HttpResponse("updates done ")