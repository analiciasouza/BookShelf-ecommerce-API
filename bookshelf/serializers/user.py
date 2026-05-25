from models.user import User
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
      
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    password2 = serializers.CharField(write_only=True)
    
    class Meta:
        model  = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({'password': 'As senhas não coincidem.'})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')  
        return User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)  

    class Meta:
        model  = User
        fields = ['id', 'first_name', 'last_name', 'full_name', 'email', 'phone', 'avatar']
    
    