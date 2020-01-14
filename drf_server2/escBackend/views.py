from .models import *
from .serializers import *
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

templateProcessId = 2
templateEngineerId = 1
templateReviewerId = 1
templateCommentId = 1


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
    def perform_create(self, serializer):
        serializer.save()
        pid = serializer.data['id']
        processReviewTemplate = {
            "Process": pid,
            "Reviewer": templateReviewerId
        }
        processReviewSerializer = ProcessReviewSerializer(data = processReviewTemplate)
        processReviewSerializer.is_valid()
        processReviewSerializer.save()
        processCommentsTemplate = {
            "Process": pid,
            "Comment": templateCommentId
        }
        processCommentsSerializer = ProcessCommentsSerializer(data = processCommentsTemplate)
        processCommentsSerializer.is_valid()
        processCommentsSerializer.save()

class ProcessReviewViewSet(viewsets.ModelViewSet):
    queryset = ProcessReview.objects.all()
    serializer_class = ProcessReviewSerializer

class ProcessCommentsViewSet(viewsets.ModelViewSet):
    queryset = ProcessComments.objects.all()
    serializer_class = ProcessCommentsSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer