# Generated by Django 5.0.4 on 2024-06-10 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_cartitems_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='total_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
