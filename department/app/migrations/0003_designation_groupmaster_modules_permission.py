# Generated by Django 4.2.7 on 2023-11-04 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_department_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation_name', models.CharField(max_length=100)),
                ('designation_description', models.CharField(max_length=1000)),
                ('designation_status', models.CharField(default=True, max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=100)),
                ('group_description', models.CharField(max_length=1000)),
                ('group_status', models.CharField(default=True, max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(max_length=100)),
                ('module_description', models.CharField(max_length=1000)),
                ('module_status', models.CharField(default=True, max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_name', models.CharField(max_length=100)),
                ('permission_description', models.CharField(max_length=1000)),
                ('permission_status', models.CharField(default=True, max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
