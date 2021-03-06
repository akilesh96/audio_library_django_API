# Generated by Django 3.2 on 2021-05-03 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudiobookDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('narrator', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'audiobook_details',
            },
        ),
        migrations.CreateModel(
            name='PodcastDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('host', models.CharField(max_length=100)),
                ('participants', models.CharField(blank=True, max_length=1200)),
            ],
            options={
                'db_table': 'podcast_details',
            },
        ),
        migrations.CreateModel(
            name='SongDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('duration', models.IntegerField()),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'song_details',
            },
        ),
    ]
