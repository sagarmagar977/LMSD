# Generated by Django 3.2.23 on 2023-12-22 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0007_transaction_remarks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowedbookinfo',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='borrowedbookinfo',
            name='due_status',
        ),
    ]
