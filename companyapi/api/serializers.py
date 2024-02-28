from rest_framework import serializers
from .models import Company,Employee

# Creating serializer for model Company

class CompanySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Company
        fields='__all__'

#creating serializer for Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
