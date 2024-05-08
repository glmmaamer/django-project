from django.shortcuts import render, get_object_or_404
from .models import Post,Comment
from .forms import NowComment

# Create your views here.

def home(request):
    myhome = {
        'title':'الصفحة الرئيسية',
        'postes':Post.objects.all()
    }
    
    return render(request, 'blog/home.html',myhome)

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

