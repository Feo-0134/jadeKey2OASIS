from django.urls import path

from . import views

app_name = 'jadeK'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('<int:pk>/', views.ProcessView.as_view(), name='process'),
    path('stage/<int:pk>', views.StageView.as_view(), name='stage'),
]