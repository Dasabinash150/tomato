# Generated by Django 5.0.4 on 2024-06-07 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='item_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]