from django.db import models


class Payment(models.Model):
    pmt_id = models.AutoField(primary_key=True)
    date = models.DateField()
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE)
    cust_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    credit_card = models.CharField(max_length=19)


class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    last = models.CharField(max_length=50)
    first = models.CharField(max_length=50)
    position = models.CharField(max_length=50)


class Customer(models.Model):
    cust_id = models.AutoField(primary_key=True)
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)
    address = models.TextField()


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    emp_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    cust_id = models.ForeignKey('Customer', on_delete=models.CASCADE)
    date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    pmt_id = models.ForeignKey('Payment', on_delete=models.CASCADE, related_name='orders')

class Product(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=100)
    prod_type = models.CharField(max_length=50)
    size_pricing = models.CharField(max_length=50)
    makeup = models.CharField(max_length=50)
    manufacturing_cost = models.DecimalField(max_digits=10, decimal_places=2)
    ski_name = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=100)


class Shipping(models.Model):
    ship_id = models.AutoField(primary_key=True)
    ship_date = models.DateField()
    delivery_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)


class Return(models.Model):
    return_id = models.AutoField(primary_key=True)
    date = models.DateField()
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    quantity = models.IntegerField()


class RawMaterial(models.Model):
    material_id = models.AutoField(primary_key=True)
    cast = models.CharField(max_length=100)
    date_purchased = models.DateField()
    quantity = models.IntegerField()
    material_name = models.CharField(max_length=100)


class OrderLine(models.Model):
    line_id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
