# Generated by Django 3.2.5 on 2022-06-17 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='correo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
    ]