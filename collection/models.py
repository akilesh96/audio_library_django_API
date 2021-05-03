from django.db import models

class SongDetails(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    upload_time = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = "song_details"

class PodcastDetails(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    upload_time = models.DateTimeField(auto_now_add = True)
    host = models.CharField(max_length=100)
    participants = models.CharField(max_length=1200, blank=True)

    class Meta:
        db_table = "podcast_details"

class AudiobookDetails(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration = models.IntegerField()
    upload_time = models.DateTimeField(auto_now_add = True)

    class Meta:
        db_table = "audiobook_details"