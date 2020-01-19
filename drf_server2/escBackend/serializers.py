from django.contrib.auth.models import *
from rest_framework import serializers
from .models import *

class EngineerTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineerTitle
        fields = ['id', 'FullName', 'Abbreviation']
    
class ProcessKindSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessKind
        fields = ['id', 'FullName', 'Abbreviation']
    
class StageKindSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageKind
        fields = ['id', 'FullName', 'Abbreviation']

class EngineerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engineer
        fields = ['id', 'Alias', 'Name', 'Title', 'EngineerLatestProcess', 'EngineerLatestStage', 'IsReviewer']

class ReviewerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviewer
        fields = ['id', 'Alias', 'Name', 'Title']

class ProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Process
        fields = ['id', 'Kind', 'ProcessOwner', 'ProcessReviewer','ProcessComments', 'ProcessCurrentStage', 'Stage1TryTimes', 'Stage2TryTimes', 'Stage3TryTimes', 'Stage4TryTimes']

class ProcessReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessReview
        fields = ['id', 'Process', 'Reviewer']
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'Stage', 'Writer', 'Context','Edited', 'Submited']
class ProcessCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessComments
        fields = ['id', 'Process', 'Comment']