# Generated by Django 4.1.1 on 2022-09-28 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_alter_productattribute_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productattribute',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
