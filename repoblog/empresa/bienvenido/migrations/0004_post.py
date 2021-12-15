# Generated by Django 4.0 on 2021-12-15 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bienvenido', '0003_alter_departamento_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=1000)),
                ('fecha_creado', models.DateTimeField(default=None)),
                ('categoria', models.CharField(max_length=15)),
            ],
        ),
    ]
