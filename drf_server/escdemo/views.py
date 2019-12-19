
from .models import *
from .serializers import *
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class EngineerViewSet(viewsets.ModelViewSet):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer

class HighLvlViewSet(viewsets.ModelViewSet):
    queryset = HighLvl.objects.all()
    serializer_class = HighLvlSerializer

class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ProcessLinkStageViewSet(viewsets.ModelViewSet):
    queryset = ProcessLinkStage.objects.all()
    serializer_class = ProcessLinkStageSerializer

class StageLinkCommentViewSet(viewsets.ModelViewSet):
    queryset = StageLinkComment.objects.all()
    serializer_class = StageLinkCommentSerializer

class MakeCommentOnViewSet(viewsets.ModelViewSet):
    queryset = MakeCommentOn.objects.all()
    serializer_class = MakeCommentOnSerializer