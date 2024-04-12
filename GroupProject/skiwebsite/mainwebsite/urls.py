from django.contrib import admin
from django.urls import path, include
from mainwebsite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Employee URLs
    path('employees/', views.EmployeeList.as_view(), name='employee_list'),
    path('employeeadd/', views.EmployeeAdd.as_view(), name='employee_form'),
    path('employeeedit/<int:pk>/', views.EmployeeUpdate.as_view(), name='employee_edit'),
    path('employees/delete/<int:pk>/', views.EmployeeDelete.as_view(), name='employee_delete'),
    # Customer URLs
    path('customers/', views.CustomerList.as_view(), name='customer_list'),
    path('customers/add/', views.CustomerAdd.as_view(), name='customer_add'),
    path('customers/edit/<int:pk>/', views.CustomerUpdate.as_view(), name='customer_edit'),
    path('customers/delete/<int:pk>/', views.CustomerDelete.as_view(), name='customer_delete'),
    # Product
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('products/add/', views.ProductAdd.as_view(), name='product_add'),
    path('products/edit/<int:pk>/', views.ProductUpdate.as_view(), name='product_edit'),
    path('products/delete/<int:pk>/', views.ProductDelete.as_view(), name='product_delete'),
    


]
