# Generated by Django 2.0.7 on 2018-08-20 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoupload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='duration',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=1000),
        ),
    ]
