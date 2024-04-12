<<<<<<< HEAD
from mainwebsite.models import Employee, Customer, Order, Product, Payment
from mainwebsite.forms import EmployeeForm, CustomerForm, OrderForm, PaymentForm

from .forms import PaymentForm
from .models import Payment
from .serializers import EmployeeSerializer, CustomerSerializer, OrderSerializer, PaymentSerializer
=======
from mainwebsite.models import Employee, Customer, Order, Product, RawMaterial
from mainwebsite.forms import EmployeeForm, CustomerForm, OrderForm, RawMaterialForm
from .serializers import EmployeeSerializer, CustomerSerializer, OrderSerializer
>>>>>>> 0a5ab0478f906519dd2175942292e1ae89576aa1
from rest_framework import generics
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django import forms
from django.views.generic import FormView
from django.views.generic import ListView
from django.db.models import Sum, Count



class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'id'


class EmployeeList(View):
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, 'employees/employee_list.html', {'employees': employees})


class EmployeeAdd(View):
    def get(self, request):
        form = EmployeeForm()
        return render(request, 'employees/employee_add.html', {'form': form})

    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
        return render(request, 'employees/employee_add.html', {'form': form})


class EmployeeUpdate(View):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        form = EmployeeForm(instance=employee)
        return render(request, 'employees/employee_update.html', {'form': form, 'employee': employee})

    def post(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
        return render(request, 'employees/employee_update.html', {'form': form, 'employee': employee})


class EmployeeDelete(View):
    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return redirect('employee_list')


class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'id'


class CustomerList(View):
    def get(self, request):
        customers = Customer.objects.all()
        return render(request, 'customers/customer_list.html', {'customers': customers})


class CustomerAdd(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'customers/customer_add.html', {'form': form})

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        return render(request, 'customers/customer_add.html', {'form': form})


class CustomerUpdate(View):
    def get(self, request, id):
        customer = get_object_or_404(Customer, pk=id)
        form = CustomerForm(instance=customer)
        return render(request, 'customers/customer_update.html', {'form': form, 'customer': customer})

    def post(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        return render(request, 'customers/customer_update.html', {'form': form, 'customer': customer})


class CustomerDelete(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        customer.delete()
        return redirect('customer_list')


class SalesReportForm(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()


class SalesReportView(FormView, ListView):
    template_name = 'admin/sales_report.html'
    form_class = SalesReportForm
    queryset = Order.objects.none()  # Default to no orders

    def form_valid(self, form):
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        self.queryset = Order.objects.filter(date__range=(start_date, end_date)) \
            .annotate(total_sales=Sum('total_price')) \
            .order_by('-date')
        return self.get(self.request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(self.request.GET or None)
        return context


class ProductPopularityReportView(ListView):
    template_name = 'admin/product_popularity_report.html'
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.annotate(
            total_sold=Sum('orderline__quantity'),
            orders_count=Count('orderline'),
        ).order_by('-total_sold')


class OrderList(View):
    def get(self, request):
        orders = Order.objects.all()
        return render(request, 'orders/order_list.html', {'orders': orders})


class OrderAdd(View):
    def get(self, request):
        form = OrderForm()
        return render(request, 'orders/order_add.html', {'form': form})

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
        return render(request, 'orders/order_add.html', {'form': form})


class OrderDelete(View):
    def get(self, request, pk):
        order = get_object_or_404(Employee, pk=pk)
        order.delete()
        return redirect('order_list')


class OrderUpdate(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        form = OrderForm(instance=order)
        return render(request, 'orders/order_update.html', {'form': form, 'order': order})

    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
        return render(request, 'orders/order_update.html', {'form': form, 'order': order})

<<<<<<< HEAD
class PaymentList(View):
    def get(self, request):
        payments = Payment.objects.all()
        return render(request, 'payment/payment_list.html', {'payments': payments})

class PaymentAdd(View):
    def get(self, request):
        form = PaymentForm()
        return render(request, 'payment/payment_add.html', {'form': form})

    def post(self, request):
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
        return render(request, 'payment/payment_add.html', {'form': form})

class PaymentDelete(View):
    def get(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        payment.delete()
        return redirect('payment_list')

class PaymentUpdate(View):
    def get(self, request, pk):
        order = get_object_or_404(Order, pk=pk)
        form = PaymentForm(instance=Payment)
        return render(request, 'payment/payment_update.html', {'form': form, 'payment': Payment})

    def post(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        form = OrderForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
        return render(request, 'payment/payment_update.html', {'form': form, 'payment': payment})
=======

class RawMaterialList(View):
    def get(self, request):
        rawmaterials = RawMaterial.objects.all()
        return render(request, 'rawmaterials/rawmaterial_list.html', {'rawmaterials': rawmaterials})


class RawMaterialAdd(View):
    def get(self, request):
        form = RawMaterialForm()
        return render(request, 'rawmaterials/rawmaterial_add.html', {'form': form})

    def post(self, request):
        form = RawMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rawmaterials_list')
        return render(request, 'rawmaterials/rawmaterial_add.html', {'form': form})


class RawMaterialDelete(View):
    def get(self, request, pk):
        rawmaterial = get_object_or_404(Employee, pk=pk)
        rawmaterial.delete()
        return redirect('order_list')


class RawMaterialUpdate(View):
    def get(self, request, pk):
        rawmaterial = get_object_or_404(RawMaterial, pk=pk)
        form = RawMaterialForm(instance=rawmaterial)
        return render(request, 'rawmaterials/rawmaterial_update.html', {'form': form, 'rawmaterial': rawmaterial})

    def post(self, request, pk):
        rawmaterial = get_object_or_404(RawMaterial, pk=pk)
        form = RawMaterialForm(request.POST, instance=rawmaterial)
        if form.is_valid():
            form.save()
            return redirect('rawmaterial_list')
        return render(request, 'rawmaterials/rawmaterial_update.html', {'form': form, 'rawmaterial': rawmaterial})
>>>>>>> 0a5ab0478f906519dd2175942292e1ae89576aa1
