"""
URL configuration for skiwebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'skistore'  # This is for namespacing your app's URLs

urlpatterns = [
    # Employee URLs
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employees/add/', views.EmployeeAddView.as_view(), name='employee_add'),
    path('employees/edit/<int:pk>/', views.EmployeeUpdateView.as_view(), name='employee_edit'),
    path('employees/delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='employee_delete'),

    # Customer URLs
    path('customers/', views.CustomerListView.as_view(), name='customer_list'),
    path('customers/add/', views.CustomerAddView.as_view(), name='customer_add'),
    path('customers/edit/<int:pk>/', views.CustomerUpdateView.as_view(), name='customer_edit'),
    path('customers/delete/<int:pk>/', views.CustomerDeleteView.as_view(), name='customer_delete'),
]


