from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets


class StudentModelViewSet(viewsets.ModelViewSet): #this is a viewset for the Student model
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
