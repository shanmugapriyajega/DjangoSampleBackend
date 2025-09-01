from rest_framework import serializers
from .models import *
class student_serializer(serializers.ModelSerializer):
    class Meta:
        model=student_table
        fields='__all__'