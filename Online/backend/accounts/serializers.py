from rest_framework import serializers
from . models import User, Location, ServiceRequest, Message



class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=100, write_only=True)

    class Meta:
        model = User 
        fields = ['name', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(max_length=255)

    class Meta:
        model = User 
        fields = ['email', 'password']

    
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['email', 'password', 'name']
        
        
#Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'latitude', 'longitude', 'address', 'timestamp']




# Services request

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = '__all__'
        
        
        
# Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender_name', 'text', 'created_at']