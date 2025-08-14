from django.db import models

# Create your models here.
from employees.models import Employee

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Late', 'Late'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attendances")
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.employee.name} - {self.date} - {self.status}"

class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="performances")
    rating = models.IntegerField()  # 1-5 scale
    review_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} - {self.rating} ({self.review_date})"
