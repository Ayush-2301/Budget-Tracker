# Generated by Django 3.0.3 on 2020-05-06 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_app', '0003_auto_20200505_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetitem',
            name='amount',
            field=models.FloatField(),
        ),
    ]