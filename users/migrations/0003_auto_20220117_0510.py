# Generated by Django 3.2.3 on 2022-01-17 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='users',
            name='lastname',
        ),
    ]