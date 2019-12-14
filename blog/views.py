from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.models import User
from .models import AllBlogs


# Create your views here.
def home(request):
    context = {
        'blogs' : AllBlogs.objects.all()
    }
    return render(request, 'blog/home.html', context)

def likes(request, blog_id):
    if request.method == 'POST':
        blog = get_object_or_404(AllBlogs, pk=blog_id)
        blog.like_num += 1
        blog.save()
        return redirect('/blog/' + str(blog.id))


class AllBlogsListView(ListView):
    model = AllBlogs
    template_name = 'blog/home.html'
    context_object_name = 'blogs'
    ordering = ['-pub_date']
    paginate_by = 5


class UserAllBlogsListView(ListView):
    model = AllBlogs
    template_name = 'blog/user_blogs.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return AllBlogs.objects.filter(blogger=user).order_by('-pub_date')


class AllBlogsDetailView(DetailView):
    model = AllBlogs
    #template_name = 'blog/detail.html'

class AllBlogsCreateView(LoginRequiredMixin, CreateView):
    model = AllBlogs
    fields = ['title', 'body', 'image']
    #template_name = 'blog/blog_form.html'

    def form_valid(self, form):
        form.instance.blogger = self.request.user
        return super().form_valid(form)


class AllBlogsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AllBlogs
    fields = ['title', 'body', 'image']
    #template_name = 'blog/blog_form.html'

    def form_valid(self, form):
        form.instance.blogger = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.blogger:
            return True
        return False


class AllBlogsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AllBlogs
    success_url = '/'
    #template_name = 'blog/confirm_delete.html'

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.blogger:
            return True
        return False
