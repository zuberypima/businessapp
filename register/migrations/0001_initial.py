# Generated by Django 4.2 on 2023-06-04 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phoneNumber', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderNo', models.CharField(max_length=255, unique=True)),
                ('quantity', models.IntegerField()),
                ('amountpaid', models.FloatField()),
                ('transId', models.CharField(max_length=255, unique=True)),
                ('orderstatus', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('stock', models.IntegerField()),
                ('expireDate', models.DateField()),
                ('costPrice', models.FloatField()),
                ('selingPrice', models.IntegerField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transId', models.CharField(max_length=255, unique=True)),
                ('customerDetails', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='register.customer')),
                ('orderDetails', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='register.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.product'),
        ),
    ]
