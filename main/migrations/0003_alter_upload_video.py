# Generated by Django 3.2.9 on 2023-01-07 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='video',
            field=models.FileField(upload_to='main/media/'),
        ),
    ]