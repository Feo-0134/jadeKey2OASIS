from django.contrib.auth.models import *
from rest_framework import serializers
from .models import *

class EngineerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engineer
        fields = ['id', 'user', 'name', 'title']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'engineer', 'stageTitle', 'result', 'comment_text']

class HighLvlSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighLvl
        fields = ['id', 'user', 'name', 'related_comment']

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = ['id', 'engineer', 'title', 'status', 'commitee_num', 'related_comment']

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ['id', 'title', 'engineer', 'status', 'stage']

class ProcessLinkStageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessLinkStage
        fields = ['id', 'process', 'stage']

class StageLinkCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageLinkComment
        fields = ['id', 'stage', 'comment']
    
class MakeCommentOnSerializer(serializers.ModelSerializer):
    class Meta:
        model = MakeCommentOn
        fields = ['id', 'highlvl', 'comment']
