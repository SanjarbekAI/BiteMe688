# Generated by Django 5.0.1 on 2024-01-25 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_rename_image_foodsmodel_image1_foodsmodel_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodsmodel',
            name='is_special',
            field=models.BooleanField(default=False),
        ),
    ]