# Create your views here.
from escapp.models import *
from escapp.serializers import *

from rest_framework import generics

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets

class EngineerViewSet(viewsets.ModelViewSet):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer

class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer

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