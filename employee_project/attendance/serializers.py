from rest_framework import serializers
from .models import Attendance, Performance
from employees.models import Employee

class AttendanceSerializer(serializers.ModelSerializer):
    employee_id = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.all().order_by('id'), source='employee', write_only=True
    )
    employee = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'employee_id', 'date', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee_id'].queryset = self.Meta.model._meta.get_field('employee').related_model.objects.all()

class PerformanceSerializer(serializers.ModelSerializer):
    employee_id = serializers.PrimaryKeyRelatedField(
    queryset=Employee.objects.all().order_by('id'), source='employee', write_only=True
)
    employee = serializers.StringRelatedField(read_only=True)

    """
    Serializer for Employee model to convert model instances
    into JSON format and validate input data.
    """

    class Meta:
        model = Performance
        fields = ['id', 'employee', 'employee_id', 'rating', 'review_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['employee_id'].queryset = self.Meta.model._meta.get_field('employee').related_model.objects.all()

