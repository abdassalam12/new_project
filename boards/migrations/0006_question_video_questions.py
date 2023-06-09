# Generated by Django 4.1.7 on 2023-04-19 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_video_minature'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('choice1', models.CharField(max_length=255)),
                ('choice2', models.CharField(max_length=255)),
                ('choice3', models.CharField(max_length=255)),
                ('choice4', models.CharField(max_length=255)),
                ('answer', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='questions',
            field=models.ManyToManyField(to='boards.question'),
        ),
    ]
