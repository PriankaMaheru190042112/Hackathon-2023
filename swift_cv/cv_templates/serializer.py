
from rest_framework import serializers
from .models import CV_template

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = CV_template
        fields = ['temp_id', 'name', 'type']
