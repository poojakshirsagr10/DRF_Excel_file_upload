from django.shortcuts import render
from rest_framework import viewsets
from .serializers import Student1Serializer,SchoolSerializer,School,Student1
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
class SchoolViewSet(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School.objects.all()


class Student1ViewSet(viewsets.ModelViewSet):
    serializer_class = Student1Serializer
    queryset = Student1.objects.all()


class FilterViewSet(viewsets.ModelViewSet):
    serializer_class = Student1Serializer
    queryset = Student1.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['school']

