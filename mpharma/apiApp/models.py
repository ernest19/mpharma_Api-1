# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class icdCode(models.Model): 
    category_code = models.CharField(max_length=90, blank=True, null=True)
    diagnosis_code = models.CharField(max_length=300, blank=True, null=True)  # Field renamed because it ended with '_'.
    full_code = models.CharField(max_length=300, blank=False,primary_key=True ,default="na")
    abbreviated_description = models.CharField(max_length=300, blank=True, null=True)
    full_description = models.CharField(max_length=300, blank=True, null=True)
    category_title = models.CharField(max_length=300, blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)