from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, UpdateForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage

# Create your views here.

def CategoryView(request, dogs):
    category_posts = Post.objects.filter(category=dogs.replace('-', ' '))
    return render(request, 'categories.html', {'dogs': dogs.title().replace('-', ' '), 'category_posts':category_posts})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date', '-post_time']

    def get_context_data(self, *args, **kwargs):
        dog_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["dog_menu"] = dog_menu
        return context


class ArticleDetail(DetailView):
    model = Post
    template_name = 'article_details.html'


    def get_context_data(self, *args, **kwargs):
        dog_menu = Category.objects.all()
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()


        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True


        context["dog_menu"] = dog_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

    def get_context_data(self, *args, **kwargs):
        dog_menu = Category.objects.all()
        context = super(AddPost, self).get_context_data(*args, **kwargs)
        context["dog_menu"] = dog_menu
        return context

class UpdatePost(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

