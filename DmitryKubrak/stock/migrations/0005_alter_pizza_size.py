# Generated by Django 3.2.2 on 2021-05-16 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_rename_submitted_pizza_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.CharField(max_length=20),
        ),
    ]
