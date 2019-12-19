from django.urls import path, include
from rest_framework.routers import DefaultRouter
from escdemo import views
from rest_framework import renderers


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'engineer', views.EngineerViewSet)
router.register(r'highlvl', views.HighLvlViewSet)
router.register(r'process', views.ProcessViewSet)
router.register(r'stage', views.StageViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'pls', views.ProcessLinkStageViewSet)
router.register(r'slc', views.StageLinkCommentViewSet)
router.register(r'mkcmton', views.MakeCommentOnViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]