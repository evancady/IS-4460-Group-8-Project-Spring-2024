from django.contrib import admin
from django.urls import path, include
from skiwebsite import views

urlpatterns = [
    path('admin/', admin.site.urls),
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
    # Including app's URLConf for any additional routing within 'myapp'
    path('myapp/', include('myapp.urls')),
]
