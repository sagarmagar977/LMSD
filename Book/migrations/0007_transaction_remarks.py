# Generated by Django 3.2.23 on 2023-12-22 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0006_remove_borrowedbookinfo_returned_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='remarks',
            field=models.TextField(default=None, null=True),
        ),
    ]
