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
    # Order URLs
    path('orders/', views.OrderList.as_view(), name='order_list'),

    path('orders/add/', views.OrderAdd.as_view(), name='order_form'),
    path('orders/update/<int:pk>/', views.OrderUpdate.as_view(), name='order_update'),
    path('orders/delete/<int:pk>/', views.OrderDelete.as_view(), name='order_delete'),
    # Payment URLs
    path('payment/', views.PaymentList.as_view(), name='payment_list'),
    path('payment/add/', views.PaymentAdd.as_view(), name='payment_add'),
    path('payment/add/', views.PaymentAdd.as_view(), name='payment_form'),
    path('payment/delete/<int:pk>/', views.PaymentDelete.as_view(), name='payment_delete'),
    path('payment/update/<int:pk>/', views.PaymentUpdate.as_view(), name='payment_update'),
    path('payment/delete/<int:pk>/', views.PaymentDelete.as_view(), name='payment_delete'),
path('payment/list/', views.PaymentList.as_view(), name='Payment_list'),


]
