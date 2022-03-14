from audioop import reverse
from multiprocessing import context
from urllib import request
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import UpdateView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User

################
########## POSTS

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())
    posts = Post.objects.all().order_by('-created_at')[:20]         # get all posts, max 20
    return render(request, 'posts.html', {'posts': posts})         # display posts

def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit_post(request, post_id):#id
    posts = Post.objects.get(id = post_id)
    if request.method == "POST":
       form = PostForm(request.POST, request.FILES, instance=posts)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/')
       else:
            return HttpResponseRedirect('Not valid')
    return render(request, 'edit.html', {'posts' : posts})

def like(request, post_id):
    newlikecount= Post.objects.get(id = post_id)
    newlikecount.likes += 1
    newlikecount.save()
    return HttpResponseRedirect('/')