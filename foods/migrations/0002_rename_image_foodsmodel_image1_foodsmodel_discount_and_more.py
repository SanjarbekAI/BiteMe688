# Generated by Django 5.0.1 on 2024-01-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodsmodel',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='foodsmodel',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='foodsmodel',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='foodsmodel',
            name='image2',
            field=models.ImageField(default=1, upload_to='foods'),
            preserve_default=False,
        ),
    ]
