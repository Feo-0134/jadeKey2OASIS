# Create your views here.
from escapp.models import *
from escapp.serializers import *

from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework import renderers

from django.core import serializers
from django.shortcuts import get_object_or_404


class EngineerViewSet(viewsets.ModelViewSet):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def process_list(self, request, pk):
        engineer = get_object_or_404(Engineer,pk=pk)
        own_process =  serializers.serialize("json", engineer.process_set.all())
        return Response(own_process)
    
class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def stage_list(self, request, pk):
        process = get_object_or_404(Process,pk=pk)
        own_stage = serializers.serialize("json", process.stage_set.all())
        return Response(own_stage)


class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def comments_list(self, request, pk):
        stage = get_object_or_404(Stage,pk=pk)
        own_comments = serializers.serialize("json", stage.comment_set.all())
        return Response(own_comments)
    
        
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'engineer': reverse('engineer-list', request=request, format=format),
        'process': reverse('process-list', request=request, format=format),
        'stage': reverse('stage-list', request=request, format=format),
        'comment': reverse('comment-list', request=request, format=format)
    })