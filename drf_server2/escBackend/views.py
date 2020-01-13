from .models import *
from .serializers import *
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


class EngineerTitleViewSet(viewsets.ModelViewSet):
    queryset = EngineerTitle.objects.all()
    serializer_class = EngineerTitleSerializer

class ProcessKindViewSet(viewsets.ModelViewSet):
    queryset = ProcessKind.objects.all()
    serializer_class = ProcessKindSerializer

class StageKindViewSet(viewsets.ModelViewSet):
    queryset = StageKind.objects.all()
    serializer_class = StageKindSerializer

class EngineerViewSet(viewsets.ModelViewSet):
    queryset = Engineer.objects.all()
    serializer_class = EngineerSerializer

class ReviewerViewSet(viewsets.ModelViewSet):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer

class ProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = ProcessSerializer

class ProcessReviewViewSet(viewsets.ModelViewSet):
    queryset = ProcessReview.objects.all()
    serializer_class = ProcessReviewSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
