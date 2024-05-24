from django.forms import BaseModelForm 
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post,Comment
from .forms import NowComment, post_ar
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

def home(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_page)
    context = {
        'title':'الصفحة الرئيسية',
        'postes': posts,
        'page':page,
    }
    return render(request, 'blog/index.html',context)



def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(active=True)
    # save data comments forms
    if request.method == 'POST':
        comment_forms = NowComment(data=request.POST)
        if comment_forms.is_valid():
            new_comment = comment_forms.save(commit=False)
            new_comment.post = post
            new_comment.save()
            comment_forms = NowComment()
    else:
        comment_forms = NowComment()
    context = {
        'title':post,
        'post': post,
        'comments':comments,
        'comment_forms':comment_forms,
    }
  
    return render(request, 'blog/detail.html', context)

class Post_Creat_view(LoginRequiredMixin ,CreateView):
    model  = Post
    template_name = 'blog/new_post.html'
    form_class = post_ar
    
    def form_valid(self, form):
        form.instance.user_post = self.request.user
        return super().form_valid(form)
    

class Post_update_view(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blog/post_update.html'
    form_class = post_ar

    def form_valid(self, form):
        form.instance.user_post = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user_post:
            return True
        else:
            return False
class Post_delet_views(UserPassesTestMixin ,LoginRequiredMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/confirm_delet_post.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user_post:
            return True
        return False
        

