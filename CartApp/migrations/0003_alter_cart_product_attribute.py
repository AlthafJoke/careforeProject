# Generated by Django 4.1.1 on 2022-09-28 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_alter_productattribute_quantity'),
        ('CartApp', '0002_cart_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='product_attribute',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.productattribute'),
        ),
    ]
