# Generated by Django 3.2 on 2023-12-20 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_post_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='descripcion_articulo',
            field=models.TextField(blank=True, null=True),
        ),
    ]