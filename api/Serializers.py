from rest_framework import serializers
from .models import *

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('__all__')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Fields
        fields = '__all__'
class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = '__all__'