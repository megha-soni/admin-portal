# Generated by Django 4.2.7 on 2023-11-03 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='status',
            field=models.CharField(default=True, max_length=20),
        ),
    ]
