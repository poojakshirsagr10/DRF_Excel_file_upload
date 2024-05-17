from rest_framework import serializers
from .models import School,Student1

class Student1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student1
        fields = "__all__"

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"