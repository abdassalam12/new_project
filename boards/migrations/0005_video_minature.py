# Generated by Django 4.1.7 on 2023-04-19 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0004_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='minature',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
