#Serializer to convert your model to jason data
from rest_framework import serializers
from .models import employees

class employeesSerializer(serializers.HyperlinkedModelSerializer):
    """Meta class"""
    class Meta:
        model= employees
        #fields= ('firstname', 'lastname')  #we do this if we need to selected info from a model
        fields= '__all__'