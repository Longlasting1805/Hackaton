from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('fullname', 'score', 'created_at')
        model = Student
