# Generated by Django 2.1.3 on 2018-12-11 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banksite', '0002_auto_20181122_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='value',
            field=models.FloatField(),
        ),
    ]
