from django.shortcuts import render
from django.views.generic import (
    ListView,
    DeleteView,
    DetailView,
    CreateView,
    UpdateView
)
from .models import Post
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView): #GET Request -> List
    # template_name attribute renders a specific html file
    template_name = "post/list.html"
    # model attribute let django know from which model (table) we want to retrieve the data
    model = Post
    # context_object_name attribute allow us to change the variable on how we call it inside of the templates
    context_object_name = "posts"
class PostDetailView(DetailView):  # GET request -> object
    template_name = "post/detail.html"
    model = Post
    context_object_name = "single_post"

class PostCreateView(CreateView): # Post Request -> form (Html)
    template_name = "post/new.html"
    model = Post
    # fields attribute is a list that allows us to enable/disable the inputs to render in the html
    fields = ["title","subtitle","body"]

    def form_valid(self, form):
        form.instance.author = User.objects.last()
        return super().form_valid(form)
    
class PostUpdateView(UpdateView): # POST Request -> filled form (HTML)
    template_name = "post/edit.html"
    model = Post
    fields = ["title","subtitle","body"]

class PostDeleteView(DeleteView): # Post Request -> html
    template_name = "post/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")