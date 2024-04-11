# Generated by Django 5.0.1 on 2024-03-22 01:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('cust_id', models.AutoField(primary_key=True, serialize=False)),
                ('first', models.CharField(max_length=50)),
                ('last', models.CharField(max_length=50)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('last', models.CharField(max_length=50)),
                ('first', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('prod_name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('size_pricing', models.CharField(max_length=50)),
                ('makeup', models.CharField(max_length=50)),
                ('manufacturing_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ski_name', models.CharField(max_length=100)),
                ('dimensions', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('material_id', models.AutoField(primary_key=True, serialize=False)),
                ('cast', models.CharField(max_length=100)),
                ('date_purchased', models.DateField()),
                ('quantity', models.IntegerField()),
                ('material_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('ship_id', models.AutoField(primary_key=True, serialize=False)),
                ('ship_date', models.DateField()),
                ('delivery_date', models.DateField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainwebsite.customer')),
                ('emp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainwebsite.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('pmt_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('credit_card', models.CharField(max_length=19)),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainwebsite.customer')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainwebsite.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='pmt_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainwebsite.payment'),
        ),
        migrations.CreateModel(
            name='OrderLine',
            fields=[
                ('line_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainwebsite.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainwebsite.product')),
            ],
        ),
        migrations.CreateModel(
            name='Return',
            fields=[
                ('return_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainwebsite.order')),
            ],
        ),
    ]
