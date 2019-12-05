from django.shortcuts import render
from django.views import generic
from .models import *

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'jadeK/index.html'
    context_object_name = 'latest_process_list'

    def get_queryset(self):
        return Process.objects.order_by('title')[:5]


class ProcessView(generic.DetailView):
    model = Process
    template_name = 'jadeK/process.html'

class StageView(generic.DetailView):
    model = Stage
    template_name = 'jadeK/stage.html'