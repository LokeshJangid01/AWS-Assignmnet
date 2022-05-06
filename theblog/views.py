
from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Category, Post
from .forms import PostForm,UpdateForm
from django.urls import reverse_lazy




class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_time']

class ArticalView(DetailView):
    model = Post
    template_name = 'details.html'

class AddPosts(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'Add_Post.html'

class AddCategory(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'Add_category.html'

    fields = '__all__'

    
def Catagoryview(request,cats):
    category_posts = Post.objects.filter(category = cats)
    return render(request,'category.html',{'cats':cats.title(),'category_posts':category_posts} )



class UpdatePost(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update.html'
    # fields = ['title','title_tag','body']

class DeletePost(DeleteView):
    model = Post   
    template_name = 'delete.html'
    success_url = reverse_lazy('home')