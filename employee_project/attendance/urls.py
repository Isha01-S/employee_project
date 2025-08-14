from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttendanceViewSet, PerformanceViewSet
from attendance.views import performance_data


router = DefaultRouter()
router.register(r'attendances', AttendanceViewSet)
router.register(r'performances', PerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('api/performance-data/', performance_data, name='performance-data')

]
