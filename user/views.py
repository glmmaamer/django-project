from django.shortcuts import render,redirect
from .fomrs import create_account, LoginForm
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
    form = LoginForm()
    return render(reqeust, 'user/login.html', context={
                      'title':'تسجيل الدخول',
                      'from':form
                  })