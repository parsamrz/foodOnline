# Generated by Django 4.2 on 2023-05-03 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='foodItem',
            new_name='fooditem',
        ),
    ]