# Generated by Django 4.0.4 on 2022-05-19 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion1', '0002_alumno_generacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Correo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=100)),
                ('mensaje', models.TextField()),
            ],
        ),
    ]