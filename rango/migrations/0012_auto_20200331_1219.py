# Generated by Django 2.1.5 on 2020-03-31 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0011_auto_20200331_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='fkID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rango.Film'),
        ),
    ]