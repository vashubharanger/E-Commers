# Generated by Django 4.0.3 on 2022-03-23 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_address_order_customer_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='customer_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customer_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customer_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='customer_phone',
            new_name='phone',
        ),
    ]
