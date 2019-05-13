from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


'''Each class inherited from the django libraries django.views.generic in order to get a list of all the blogs(PostListView)
and each blog can be modified(PostUpdateView/PostDeleteView) and a new blog can be created(PostCreateView) for the Post model.
and user can select a particular blog in order to see details related to that particular blog(PostDetailView) 
'''


# PostListView class is used to display all the added blogs into the model Post
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']  # Order by latest post
    # paginate_by = 2


# Each blog post can be viewed separately by accessing the primary key from the database
class PostDetailView(DetailView):
    model = Post


# To create a new post for the model Post,It will validate and assign a user while creating a new post
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# Allows user to updated the post, created by the user himself
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# User can delete their post, and once deleted application will redirect to the homepage as success message
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
