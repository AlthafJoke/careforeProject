# Generated by Django 4.1.1 on 2022-09-17 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_subcategory_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='Subcategory_image',
            field=models.ImageField(blank=True, null=True, upload_to='photos/categories'),
        ),
    ]
