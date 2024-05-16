from django.shortcuts import render, get_object_or_404
from .models import Post,Comment
from .forms import NowComment
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

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
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html')

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

