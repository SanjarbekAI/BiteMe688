# Generated by Django 5.0.1 on 2024-01-25 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventsmodel',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]