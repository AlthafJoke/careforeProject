# Generated by Django 4.1.1 on 2022-09-22 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_subcategory_product_subcategorys_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
