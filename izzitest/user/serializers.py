"""
User serializer for API
"""
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    User serializer for API
    """
    class Meta:
        model = User
        fields = ['name', 'surname', 'birthday', 'registration_date']
