from escapp.models import *
from rest_framework import serializers


class EngineerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engineer
        fields = ['id', 'title', 'name']

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ['id', 'title', 'created', 'engineer', 'status']

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ['id', 'title', 'created', 'process', 'status']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'stage', 'created', 'result', 'author', 'comment_text']