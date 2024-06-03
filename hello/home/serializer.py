from rest_framework import serializers
from .models import Person
from django.contrib.auth.models import User




class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model= Person
        fields= '__all__'

class RegisterSerializer(serializers.Serializer):
    username= serializers.CharField()
    email= serializers.EmailField()
    password= serializers.CharField()

    def validate(self, data):
        if data['username']:
            if User.objects.filter(username= data['username']).exists():
                raise serializers.ValidationError('Username Not Available')
        if data['email']:
            if User.objects.filter(email= data['email']).exists():
                raise serializers.ValidationError('Email Already In Use')
        return data
    
    def create(self, validated_data):
        user= User.objects.create(username= validated_data['username'],email=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
    
class LoginSerializer(serializers.Serializer):
    username= serializers.CharField()
    password= serializers.CharField()