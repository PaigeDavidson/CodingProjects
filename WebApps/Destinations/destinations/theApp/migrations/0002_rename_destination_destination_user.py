# Generated by Django 4.2.6 on 2023-10-25 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='destination',
            old_name='destination',
            new_name='user',
        ),
    ]
