from rest_framework import serializers
from .models import User, Observation, Request

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = '__all__'
        fields = ['id', 'username']
        
        #fields = ['id', 'username', 'email', 'location','role']

class ObservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Observation
        fields = '__all__'
        read_only_fields = ('user',)  # Make the user field read-only
   

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'