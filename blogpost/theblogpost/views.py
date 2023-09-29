from django.shortcuts import render, redirect
from django.http import  HttpResponse, request
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Post
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     return render(request,'home.html', {})
#
# def index(request):
#     return  HttpResponse("<h1>Hello me<h1>")

class HomeView(ListView):
    model= Post
    template_name = 'home.html'
    ordering = ['-post_date']

class DetailsView(DetailView):
    model = Post
    template_name = 'details.html'

class AddPostView(CreateView):

    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # fields = '__all__'
    # fields = ('title', 'body')

class UpdatePostView(UpdateView):

    model = Post
    template_name = "update_post.html"
    form_class = EditForm
    # fields = ['title', 'title_tag', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')






