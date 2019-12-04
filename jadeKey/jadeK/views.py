from django.shortcuts import render
from django.views import generic
from .models import Process

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'jadeK/index.html'
    context_object_name = 'latest_process_list'

    def get_queryset(self):
        return Process.objects.order_by('-start_date')[:5]
