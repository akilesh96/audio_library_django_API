from rest_framework import serializers
from collection.models import SongDetails, PodcastDetails, AudiobookDetails

class SongDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SongDetails
        fields = '__all__'

class PodcastDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcastDetails
        fields = '__all__'

class AudiobookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudiobookDetails
        fields = '__all__'
