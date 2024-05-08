from django import template
from blog.models import Post,Comment



register = template.Library()
@register.inclusion_tag('blog/show_post.html')
def show_5_postes():
    context = {
        'show_postes': Post.objects.all()[0:5]
    }
    return context

@register.inclusion_tag('blog/show_comment.html')
def show_5_comments():
    context = {
        'show_comments': Comment.objects.all()[0:5]
    }
    return context

