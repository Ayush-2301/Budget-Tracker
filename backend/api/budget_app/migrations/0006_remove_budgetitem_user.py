# Generated by Django 3.0.3 on 2020-08-13 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0005_auto_20200506_2302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budgetitem',
            name='user',
        ),
    ]
