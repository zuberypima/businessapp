# Generated by Django 4.2 on 2023-05-30 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceNo', models.CharField(max_length=255, unique=True)),
                ('orderDetails', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='register.order')),
            ],
        ),
    ]