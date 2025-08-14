from rest_framework import serializers
from .models import Department, Employee

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)  # nested view
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), source='department', write_only=True
    )
    """
    Serializer for Employee model to convert model instances
    into JSON format and validate input data.
    """

    class Meta:
        model = Employee
        fields = ['id', 'name', 'email', 'phone_number', 'address', 'date_of_joining', 'department', 'department_id']
