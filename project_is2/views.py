from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    """Домашняя страница приложения project_is"""
    return render(request, 'project_is2/index.html')

def topics(request):
    """Выводит полный список всех тем"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'project_is2/topics.html', context)

def topic(request, topic_id):
    """Выводит все записи по одной теме"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'project_is2/topic.html', context)