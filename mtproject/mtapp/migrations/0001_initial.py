# Generated by Django 5.0.6 on 2024-06-01 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='enter the name')),
                ('age', models.IntegerField(max_length=30, verbose_name='enter the age')),
            ],
        ),
    ]
