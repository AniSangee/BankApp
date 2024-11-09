# Generated by Django 5.1.2 on 2024-11-06 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Homepage', '0003_account_alter_registerform_account_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('account_type', models.CharField(choices=[('SAVINGS', 'Savings'), ('CURRENT', 'Current'), ('FIXED', 'Fixed Deposit')], max_length=20)),
                ('initial_deposit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='RegisterForm',
        ),
    ]