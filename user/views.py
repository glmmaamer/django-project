from django.shortcuts import render,redirect
from .fomrs import create_account, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from blog.models import Post


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = create_account(request.POST)
        if form.is_valid():
            now_user = form.save(commit=False)
            #username = form.cleaned_data['username']
            now_user.set_password(form.cleaned_data['password1'])
            now_user.save()
            messages.success(request, f'{now_user}تم تسجيل الدخول بنجاح')
        return redirect('home')

    else:
        form = create_account()
    return render(request, 'user/register.html',{
        'title':'title',
        'form':form,
    })

def login_user(reqeust):
    if reqeust.method == 'POST':
        form = LoginForm()
        username  = reqeust.POST['username']
        password = reqeust.POST['password']
        user = authenticate(reqeust, username=username , password=password)
        if user is not None:
            login(reqeust, user)
            return redirect('home')
        else:
            messages.warning(reqeust, 'يوجد خطأفي إسم المستخدم أو كلمة المرور')
    else:
        form = LoginForm()
    return render(reqeust, 'user/login.html', {
                      'title':'تسجيل الدخول',
                      'form':form
                  })
def logout_user(request):
    logout(request)
    return render(request, 'user/logout.html',{
        'title':'تسجيل الخروج'
    })



def profile(reqeust):
    post = Post.objects.filter(user_post=reqeust.user)
    return render(reqeust, 'user/profile.html',{
        'title':'الملف اشخصي',
        'posts':post,
    })