from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from rest_framework import generics

from .models import Student
from .serializers import StudentSerializer


class StudentList(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
