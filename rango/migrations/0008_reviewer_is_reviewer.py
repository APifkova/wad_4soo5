# Generated by Django 2.1.5 on 2020-03-29 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0007_auto_20200329_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewer',
            name='is_reviewer',
            field=models.BooleanField(default=True),
        ),
    ]
