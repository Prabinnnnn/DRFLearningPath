from .models import Singer, Song
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'Singer', 'duration']
class SingerSerializer(serializers.ModelSerializer):
    # songs = serializers.StringRelatedField(many=True, read_only=True)
    #songs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    songs = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail',)
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'songs'] #here songs should be a name same as the one written in related_name