from django.shortcuts import render,redirect
from .fomrs import create_account
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

