from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apiApp.models import * 



class CdicodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = icdCode
        fields = ('category_code', 'diagnosis_code', 'full_code', 'abbreviated_description', 'full_description', 'category_title')
