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
<<<<<<< HEAD
    # Product
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('products/add/', views.ProductAdd.as_view(), name='product_add'),
    path('products/edit/<int:pk>/', views.ProductUpdate.as_view(), name='product_edit'),
    path('products/delete/<int:pk>/', views.ProductDelete.as_view(), name='product_delete'),
    
=======
    # Order URLs
    path('orders/', views.OrderList.as_view(), name='order_list'),
<<<<<<< HEAD
=======
    path('orders/add/', views.OrderAdd.as_view(), name='order_add'),
    path('orders/add/', views.OrderAdd.as_view(), name='order_form'),
    path('orders/delete/<int:pk>/', views.EmployeeDelete.as_view(), name='employee_delete'),
    # Raw Material 
    path('rawmaterials/', views.RawMaterialList.as_view(), name='rawmaterial_list'),
    path('rawmaterials/add/', views.RawMaterialAdd.as_view(), name='rawmaterial_add'),
    path('rawmaterials/edit/<int:pk>/', views.RawMaterialUpdate.as_view(), name='rawmaterial_edit'),
    path('rawmaterials/delete/<int:pk>/', views.RawMaterialDelete.as_view(), name='rawmaterial_delete'),
>>>>>>> 0a5ab0478f906519dd2175942292e1ae89576aa1

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
>>>>>>> 424aebb59af09ba0c3ff3f581fbc89337432825f


]
