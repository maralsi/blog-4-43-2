from django.http import HttpResponse
from django.shortcuts import render
import random
from posts.models import Post

"""
Model.objects.all() = отдает все объекты из таблицы
Model.objects.get() = отдает только один объект по определенному условию
Model.objects.filter() = отдает се объекты по определенному условию

"""


# Create your views here.
def hello_world(request):
    return HttpResponse('Hello World!')


def main_view(request):
    return render(request, 'posts/main.html')


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', context={'posts': posts})

def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})

