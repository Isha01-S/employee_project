"""
URL configuration for employee_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from employees.views import attendance_chart
from employees.views import performance_chart
from employees.views import analytics_dashboard
from attendance.views import performance_data


def home(request):
    return HttpResponse("Welcome to the Employee Management API!")




schema_view = get_schema_view(
   openapi.Info(
      title="Employee Management API",
      default_version='v1',
      description="API documentation for Employee Management System",
      contact=openapi.Contact(email="ishamca01@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),

   
   
)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/employees/', include('employees.urls')),
    path('api/attendance/', include('attendance.urls')),

    path('attendance-chart/', attendance_chart, name='attendance-chart'),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    path('performance-chart/', performance_chart, name='performance-chart'),
    path('api/performance-data/', performance_data, name='performance-data'),

    path('analytics-dashboard/', analytics_dashboard, name='analytics-dashboard'),

     # Swagger UI:
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # ReDoc UI (optional alternative):
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]