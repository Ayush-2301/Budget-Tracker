# Generated by Django 3.0.3 on 2020-08-27 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0011_auto_20200818_2255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='items',
            old_name='data',
            new_name='date',
        ),
    ]
