from django.shortcuts import render

# Create your views here.
posts = [
    {'title': 'التدوينة الاولة'},
    {'description':'تم نشر هذه التدوينة من طرف غالم معمر'},
    {'date':'2024/05/02'},
    {'auther':'ghalem maamer'},
]

def home(request):
    
    return render(request, 'blog/home.html')

def index(request):
    context = {
        'title':'الصفحة الرئيسية',
        'posts': posts
    }
    return render(request, 'blog/index.html',context)


