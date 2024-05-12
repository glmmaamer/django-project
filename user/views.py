from django.shortcuts import render,redirect
from .fomrs import create_account, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = create_account(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'{username}تم تسجيل الدخول بنجاح')
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
    return render(reqeust, 'user/login.html', context={
                      'title':'تسجيل الدخول',
                      'form':form
                  })
def logout_user(request):
    logout(request)
    return render(request, 'user/logout.html',context={
        'title':'تسجيل الخروج'
    })