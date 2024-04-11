from django import forms
from .models import Employee, Customer, Order, Product, Payment, ReturnObj, RawMaterial

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

class ReturnForm(forms.ModelForm):
    class Meta:
        model = ReturnObj
        fields = '__all__'

class RawMaterialForm(forms.ModelForm):
    class Meta:
        model = RawMaterial
        fields = '__all__'
