# Generated by Django 4.0.4 on 2023-08-26 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healtrail', '0002_service_remove_product_pub_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
    ]