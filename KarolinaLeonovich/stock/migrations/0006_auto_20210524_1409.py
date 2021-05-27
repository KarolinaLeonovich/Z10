# Generated by Django 3.2.3 on 2021-05-24 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_auto_20210523_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='comment',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='pizza',
            name='creator',
            field=models.CharField(default='admin', max_length=255),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]