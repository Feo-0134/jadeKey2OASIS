from django.urls import path, include
from rest_framework.routers import DefaultRouter
from escapp import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'engineer', views.EngineerViewSet)
router.register(r'process', views.ProcessViewSet)
router.register(r'stage', views.StageViewSet)
router.register(r'comment', views.CommentViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]