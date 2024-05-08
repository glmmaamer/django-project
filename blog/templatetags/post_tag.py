from django import template
from blog.models import Post



register = template.Library()
@register.inclusion_tag('blog/show_post.html')
def show_5_postes():
    context = {
        'l_postes': Post.objects.all()[0:5]
    }
    return context