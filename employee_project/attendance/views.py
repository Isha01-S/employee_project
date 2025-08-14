from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Attendance, Performance
from .serializers import AttendanceSerializer, PerformanceSerializer
from rest_framework.decorators import api_view
from django.db.models.functions import TruncMonth
from rest_framework.response import Response
from django.db.models import Avg

# API endpoint to return performance data
@api_view(['GET'])
def performance_data(request):
    qs = (
        Performance.objects
        .annotate(month=TruncMonth('review_date'))
        .values('month')
        .annotate(avg_rating=Avg('rating'))
        .order_by('month')
    )

    months = sorted({row['month'] for row in qs if row['month'] is not None})
    labels = [m.strftime("%b %Y") for m in months]
    data = [next((row['avg_rating'] for row in qs if row['month'] == m), 0) for m in months]

    return Response({"labels": labels, "data": data})


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all().order_by('-date')
    serializer_class = AttendanceSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['date', 'status', 'employee']
    ordering_fields = ['date', 'status']
    search_fields = ['employee__name'] 

class PerformanceViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given attendance record.

    list:
    Return a list of all attendance records.

    create:
    Create a new attendance record.

    update:
    Update an existing attendance record.

    partial_update:
    Partially update an attendance record.

    delete:
    Delete an attendance record.
    """

    queryset = Performance.objects.all().order_by('-review_date')
    serializer_class = PerformanceSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['rating', 'review_date', 'employee']
    ordering_fields = ['review_date', 'rating']
    search_fields = ['employee__name']
