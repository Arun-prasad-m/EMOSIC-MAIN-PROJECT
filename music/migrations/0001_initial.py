# Generated by Django 3.2.7 on 2023-03-21 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=150)),
                ('feedbacks', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='music_recommendation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=150)),
                ('musics', models.FileField(max_length=150, upload_to='')),
                ('emotion', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
            ],
        ),
    ]
