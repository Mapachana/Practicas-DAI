# Generated by Django 3.2 on 2021-12-10 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galerias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuadro',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='img/'),
        ),
    ]
