# Generated by Django 4.1.1 on 2023-03-01 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_yeni_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yeni',
            old_name='yazar',
            new_name='danışman',
        ),
    ]
