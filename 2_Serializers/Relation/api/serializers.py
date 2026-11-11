from .models import Singer, Song
from rest_framework import serializers

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        # fields = '__all__'
        fields = ['id', 'title', 'singer', 'duration']

class SingerSerializer(serializers.ModelSerializer):
    # serializer relations: to get info of parent/child models 
    # song = serializers.StringRelatedField(many=True, read_only=True) # string based read only representation
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True) # primary key representaion
    # song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='song-detail') # creates hyperlink representaion
    song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='title') # unique slug representaion
    # song = serializers.HyperlinkedIdentityField(view_name='song-detail') 
    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']
        