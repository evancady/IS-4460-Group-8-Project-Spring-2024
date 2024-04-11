from rest_framework import serializers
from .models import Employee, Customer, Order, Product, Payment, ReturnObj, RawMaterial


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    # Nested serializers allow for including related model data in the API response
    employee = EmployeeSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)
    payment = serializers.SlugRelatedField(slug_field='pmt_id', read_only=True)

    class Meta:
        model = Order
        fields = ['order_id', 'employee', 'customer', 'date', 'total_price', 'payment']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class ReturnSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReturnObj
        fields = '__all__'


class RawMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawMaterial
        fields = '__all__'
