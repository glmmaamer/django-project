from django.shortcuts import render
from .fomrs import create_account


# Create your views here.


def register(request):
    form = create_account()
    return render(request, 'user/register.html',{
        'title':'title',
        'form':form,
    })

