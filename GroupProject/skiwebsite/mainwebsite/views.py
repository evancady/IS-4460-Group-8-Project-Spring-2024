from mainwebsite.models import Employee, Customer, Order, Product
from mainwebsite.forms import EmployeeForm, CustomerForm
from .serializers import EmployeeSerializer, CustomerSerializer
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
    def get(self, request, id):
        employee = get_object_or_404(Employee, pk=id)
        form = EmployeeForm(instance=employee)
        return render(request, 'employees/employee_update.html', {'form': form, 'employee': employee})

    def post(self, request, id):
        employee = get_object_or_404(Employee, pk=id)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
        return render(request, 'employees/employee_update.html', {'form': form, 'employee': employee})


class EmployeeDelete(View):
    def get(self, request, id):
        employee = get_object_or_404(Employee, pk=id)
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

    def post(self, request, id):
        customer = get_object_or_404(Customer, pk=id)
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
        return render(request, 'customers/customer_update.html', {'form': form, 'customer': customer})


class CustomerDelete(View):
    def get(self, request, id):
        customer = get_object_or_404(Customer, pk=id)
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
