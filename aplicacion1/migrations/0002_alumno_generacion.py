# Generated by Django 4.0.4 on 2022-05-09 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='generacion',
            field=models.CharField(default=' ', max_length=15),
            preserve_default=False,
        ),
    ]