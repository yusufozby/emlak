# Generated by Django 4.1.1 on 2023-03-01 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0009_rename_danışman_yeni_advisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yeni',
            name='advisor',
            field=models.CharField(max_length=100, verbose_name='Danışman'),
        ),
    ]
