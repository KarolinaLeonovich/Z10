# Generated by Django 3.2.2 on 2021-05-16 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_alter_pizza_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
