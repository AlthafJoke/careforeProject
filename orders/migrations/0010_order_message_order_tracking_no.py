# Generated by Django 4.1.1 on 2022-10-10 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='tracking_no',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
