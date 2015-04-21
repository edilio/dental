from rest_framework import serializers
from .models import *


class LeadSerializer(serializers.ModelSerializer):
    ad_type = serializers.IntegerField(source='get_ad_type')

    class Meta:
        model = Lead


class CallSerializer(serializers.Serializer):
    entered_date = serializers.DateField(format="%m/%d/%Y")
    count = serializers.IntegerField()