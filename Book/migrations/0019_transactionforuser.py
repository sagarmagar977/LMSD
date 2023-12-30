# Generated by Django 3.2.23 on 2023-12-27 17:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0018_alter_transaction_transaction_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionForUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('Borrow', 'Borrow'), ('Return', 'Return')], max_length=10)),
                ('transaction_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('user', models.CharField(blank=True, max_length=255, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Book.bookinfo')),
            ],
        ),
    ]
