from rest_framework import serializers  
from sites.models import Site, Request

class SiteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Site
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Request
        fields = '__all__'