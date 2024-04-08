import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skiwebsite.settings')

django.setup()

from skiwebsite.models import Payment, Employee, Customer, Order, Product, Shipping, Return, RawMaterial, OrderLine


# Deleting all records from Payments
all_payments = payment.objects.all()
for payment in all_payments:
    payment.delete()

# Deleting all records from Employees
all_employees = employee.objects.all()
for employee in all_employees:
    employee.delete()
    
# Deleting all records from Customers
all_customers = customer.objects.all()
for customer in all_customers:
    customer.delete()

# Deleting all records from Orders
all_orders = order.objects.all()
for order in all_orders:
    order.delete()


# Deleting all records from Products
all_products = product.objects.all()
for product in all_products:
    product.delete()
    
# Deleting all records from Shipping
all_shippings = shipping.objects.all()
for shipping in all_shippings:
    shipping.delete()
    
# Deleting all records from Return
all_returns = return.objects.all()
for return_obj in all_returns:
    return_obj.delete()
    
# Deleting all records from RawMaterials
all_raw_materials = RawMaterial.objects.all()
for raw_material in all_raw_materials:
    raw_material.delete()
    
# Deleting all records from OrderLines
all_order_lines = OrderLine.objects.all()
for order_line in all_order_lines:
    order_line.delete()

###Adding 20 rows for payments
import random
from faker import Faker
from skiwebsite.models import Payment, Order, Customer
from datetime import datetime, timedelta

fake = Faker()

# Create 20 fake payment records
for _ in range(20):
    date = fake.date_between(start_date='-1y', end_date='today')
    order = Order.objects.order_by('?').first()  # Randomly select an order
    customer = order.customer  # Get customer associated with the order
    credit_card = fake.credit_card_number()

    # Create Payment instance and save to database
    payment = Payment.objects.create(
        date=date,
        order_id=order,
        cust_id=customer,
        credit_card=credit_card
    )
    payment.save()

###Adding 20 rows for Employees
import random
from faker import Faker
from skiwebsite.models import Employee

fake = Faker()

# Create 20 fake employee records
for _ in range(20):
    last_name = fake.last_name()
    first_name = fake.first_name()
    position = fake.job()

    # Create Employee instance and save to database
    employee = Employee.objects.create(
        last=last_name,
        first=first_name,
        position=position
    )
    employee.save()

### Adding 20 rows for Customer
import random
from faker import Faker
from skiwebsite.models import Customer

fake = Faker()

# Create 20 fake customer records
for _ in range(20):
    first_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.address()

    # Create Customer instance and save to database
    customer = Customer.objects.create(
        first=first_name,
        last=last_name,
        address=address
    )
    customer.save()

###Adding 20 rows for Order

import random
from faker import Faker
from skiwebsite.models import Order, Employee, Customer, Payment
from datetime import datetime, timedelta

fake = Faker()

# Get all existing employees, customers, and payments
employees = Employee.objects.all()
customers = Customer.objects.all()
payments = Payment.objects.all()

# Create 20 fake order records
for _ in range(20):
    # Randomly select an employee, customer, and payment
    employee = random.choice(employees)
    customer = random.choice(customers)
    payment = random.choice(payments)

    date = fake.date_between(start_date='-1y', end_date='today')
    total_price = fake.random_number(digits=5)  # Random total price for the order

    # Create Order instance and save to database
    order = Order.objects.create(
        emp_id=employee,
        cust_id=customer,
        date=date,
        total_price=total_price,
        pmt_id=payment
    )
    order.save()

###Adding 20 rows for Product

import random
from faker import Faker
from skiwebsite.models import Product

fake = Faker()

# Create 20 fake product records
for _ in range(20):
    prod_name = fake.word()
    prod_type = fake.word()
    size_pricing = fake.word()
    makeup = fake.word()
    manufacturing_cost = round(random.uniform(10, 1000), 2)  # Random manufacturing cost
    ski_name = fake.word()
    dimensions = fake.word()

    # Create Product instance and save to database
    product = Product.objects.create(
        prod_name=prod_name,
        prod_type=prod_type,
        size_pricing=size_pricing,
        makeup=makeup,
        manufacturing_cost=manufacturing_cost,
        ski_name=ski_name,
        dimensions=dimensions
    )
    product.save()

###Adding 20 rows for Shipping

import random
from faker import Faker
from skiwebsite.models import Shipping
from datetime import datetime, timedelta

fake = Faker()

# Create 20 fake shipping records
for _ in range(20):
    ship_date = fake.date_between(start_date='-1y', end_date='today')
    delivery_date = fake.date_between_dates(date_start=ship_date, date_end=ship_date + timedelta(days=30))  # Assume delivery within 30 days
    cost = round(random.uniform(10, 1000), 2)  # Random shipping cost

    # Create Shipping instance and save to database
    shipping = Shipping.objects.create(
        ship_date=ship_date,
        delivery_date=delivery_date,
        cost=cost
    )
    shipping.save()

###Adding 20 random rows for Return Table
    
import random
from faker import Faker
from skiwebsite.models import Return, Order
from datetime import datetime, timedelta

fake = Faker()

# Get all existing orders
orders = Order.objects.all()

# Create 20 fake return records
for _ in range(20):
    date = fake.date_between(start_date='-1y', end_date='today')
    order = random.choice(orders)  # Randomly select an order
    quantity = random.randint(1, 10)  # Random quantity returned (between 1 and 10)

    # Create Return instance and save to database
    ret = Return.objects.create(
        date=date,
        order=order,
        quantity=quantity
    )
    ret.save()

###Creating 20 random rows for RawMaterials
import random
from faker import Faker
from skiwebsite.models import RawMaterial
from datetime import datetime, timedelta

fake = Faker()

# Create 20 fake raw material records
for _ in range(20):
    cast = fake.word()
    date_purchased = fake.date_between(start_date='-1y', end_date='today')
    quantity = random.randint(1, 100)  # Random quantity purchased (between 1 and 100)
    material_name = fake.word()

    # Create RawMaterial instance and save to database
    raw_material = RawMaterial.objects.create(
        cast=cast,
        date_purchased=date_purchased,
        quantity=quantity,
        material_name=material_name
    )
    raw_material.save()
###Creating 20 random rows for OrderLine
import random
from faker import Faker
from skiwebsite.models import OrderLine

fake = Faker()

# Get all existing orders and products
orders = Order.objects.all()
products = Product.objects.all()

# Create 20 fake order line records
for _ in range(20):
    order = random.choice(orders)  # Randomly select an order
    product = random.choice(products)  # Randomly select a product
    quantity = random.randint(1, 10)  # Random quantity (between 1 and 10)
    price = round(random.uniform(10, 100), 2)  # Random price (between 10 and 100)

    # Create OrderLine instance and save to database
    order_line = OrderLine.objects.create(
        order=order,
        product=product,
        quantity=quantity,
        price=price
    )
    order_line.save()



