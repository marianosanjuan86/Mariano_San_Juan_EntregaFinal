# Generated by Django 3.2.8 on 2021-10-21 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_banda_tema_presentacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banda',
            name='fotos',
            field=models.ImageField(blank=True, upload_to='bandas'),
        ),
    ]
