# Generated by Django 3.2.23 on 2023-12-22 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0009_bookhis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('Borrow', 'Borrow'), ('Return', 'Return')], max_length=10),
        ),
    ]
