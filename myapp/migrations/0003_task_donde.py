# Generated by Django 4.1.5 on 2023-01-17 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='donde',
            field=models.BooleanField(default=False),
        ),
    ]
