# Generated by Django 4.1.1 on 2022-10-10 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_rename_postal_code_order_post_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_total',
            new_name='total_price',
        ),
    ]
