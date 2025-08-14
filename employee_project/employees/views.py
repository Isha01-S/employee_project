from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer
from django.db.models.functions import TruncMonth
from attendance.models import Attendance, Performance
from rest_framework.decorators import api_view
from django.db.models import Avg

def attendance_chart(request):
    return render(request, 'charts.html')

def performance_chart(request):
    return render(request, 'performance_charts.html')

def analytics_dashboard(request):
    return render(request, 'analytics_dashboard.html')



class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):

    """
    retrieve:
    Return the given employee.

    list:
    Return a list of all employees.

    create:
    Create a new employee instance.

    update:
    Update an existing employee.

    partial_update:
    Partially update an employee.

    delete:
    Delete an employee instance.
    """

    queryset = Employee.objects.all().order_by("id")
    serializer_class = EmployeeSerializer

    # ----- NEW: analytics endpoint -----
    @action(
        detail=False,
        methods=["get"],
        permission_classes=[AllowAny],  # public for charts page
        url_path="analytics/monthly-overview",
    )
    def monthly_overview(self, request):
        # aggregate counts by month & status
        qs = (
            Attendance.objects
            .annotate(month=TruncMonth("date"))
            .values("month", "status")
            .annotate(count=Count("id"))
            .order_by("month")
        )

        months = sorted({row["month"] for row in qs if row["month"] is not None})
        month_labels = [m.strftime("%b %Y") for m in months]

        statuses = ["Present", "Absent", "Late"]  # adapt if your choices differ

        # build datasets for Chart.js
        datasets = []
        for status in statuses:
            series = []
            for m in months:
                count = next(
                    (row["count"] for row in qs if row["month"] == m and row["status"] == status),
                    0,
                )
                series.append(count)
            datasets.append({
                "label": status,
                "data": series,
            })

        return Response({"labels": month_labels, "datasets": datasets})

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['department', 'date_of_joining']
    ordering_fields = ['name', 'date_of_joining']
    search_fields = ['name', 'email']
