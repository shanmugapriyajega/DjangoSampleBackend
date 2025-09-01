from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model
User=get_user_model()

class otherdetailsserializer(serializers.ModelSerializer):
    password=models.CharField(max_length=100)
    class  Meta:
        model=otherdetails
        fields='__all__'

    def create(self,validatate_data):
        password=validatate_data.pop("password")
        user=User.objects.create_user(password=password,**validatate_data)
        return user