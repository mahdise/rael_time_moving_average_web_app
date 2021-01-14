from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


#from rest_framework import viewsets
from . serializers import employeesSerializer
from . models import employees




class employeeList(APIView):

    def get(self, request):
        # employees1=employees.objects.all()
        # serializer=employeesSerializer(employees1, many=True)
        print(request.data)
        return Response('hello world')

    def post(self):
        pass
