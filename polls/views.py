from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .model.process import Process

import os
import django
from polls.models import Comment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings");
django.setup()

def index(request):
    context = {
        'latest_question_list': 'lêu lêu',
    }
    return render(request, 'polls/index.html', context)


def delete(request):
    Comment.objects.all().delete()
    return HttpResponse("Deleted")


def results(request):
    context = {
        'name': request.POST['name'],
        'comment': request.POST['comment'],
        'predicted': Process.test(request.POST['comment']),
    }

    c = Comment(name=context['name'], comment=context['comment'], predict=context['predicted'])
    c.save()
    return render(request, 'polls/results.html', context)


def full(request):

    data = []
    for x in Comment.objects.all():
        data.append({
            'id': x.id,
            'name': x.name,
            'comment': x.comment,   
            'predicted': x.predict,
        })
    context = {
        'data': data,
    }
    return render(request, 'polls/thongke.html', context)

def update(request):
    rid = request.GET['rid']
    data = []
    for x in Comment.objects.filter(id__gt=rid):
        data.append({
            'id': x.id,
            'name': x.name,
            'comment': x.comment,   
            'predicted': x.predict,
        })
    context = {
        'data': data,
    }
    return render(request, 'polls/update.html', context)
