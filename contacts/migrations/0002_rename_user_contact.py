# Generated by Django 3.2 on 2021-04-14 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Contact',
        ),
    ]