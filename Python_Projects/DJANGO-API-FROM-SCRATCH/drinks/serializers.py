from rest_framework import serializers ## To send data through the API
from .models import Drink ## This is the data we gonna send trough the API

#This class is what enable this API to send data of the class Drink
class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description'] ## Fields in data (JSON)

