# Generated by Django 4.0 on 2021-12-15 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bienvenido', '0005_rename_autor_post_contenido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='fecha_creado',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]