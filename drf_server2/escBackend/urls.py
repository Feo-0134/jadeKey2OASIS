from django.urls import path, include
from rest_framework.routers import DefaultRouter
from escBackend import views
from rest_framework import renderers

router = DefaultRouter()
router.register(r'engineer_title', views.EngineerTitleViewSet)
router.register(r'process_kind', views.ProcessKindViewSet)
router.register(r'stage_kind', views.StageKindViewSet)
router.register(r'engineer', views.EngineerViewSet)
router.register(r'reviewer', views.ReviewerViewSet)
router.register(r'process', views.ProcessViewSet)
router.register(r'process_review', views.ProcessReviewViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'process_comment', views.ProcessCommentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]