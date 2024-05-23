from django.shortcuts import render,redirect
from .fomrs import create_account, LoginForm, UpdateProfile, Update_img_profile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,  PageNotAnInteger, EmptyPage


# Create your views here.


def register(request):
    if request.method == 'POST':
        form = create_account(request.POST)
        if form.is_valid():
            now_user = form.save(commit=False)
            #username = form.cleaned_data['username']
            now_user.set_password(form.cleaned_data['password2'])
            now_user.save()
            messages.success(request, f'{now_user}تم تسجيل الدخول بنجاح')
        return redirect('login')

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
            return redirect('profile')
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


@login_required(login_url='login')
def profile(reqeust):
    posts = Post.objects.filter(user_post=reqeust.user)
    post_list = Post.objects.filter(user_post=reqeust.user)
    paginator = Paginator(post_list,2)
    page = reqeust.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_page)

    return render(reqeust, 'user/profile.html',{
        'title':'الملف اشخصي',
        'postes':posts,
        'page':page,
        'posts_list':post_list,
    })

def profile_update(request):
    if request.method == 'POST':
        user_form = UpdateProfile( request.POST ,instance=request.user)
        img_form = Update_img_profile( request.POST, request.FILES ,instance=request.user)
        if user_form.is_valid and img_form.is_valid:
            user_form.save()
            img_form.save()
            messages.success(request, 'تم تعديل ملفك الشخصي')
            return redirect('profile')
    else:
        user_form = UpdateProfile(instance=request.user)
        img_form = Update_img_profile(instance=request.user)
        messages.success(request,'هناك خطأ')
    

    context = {
        'title':'تعديل ملف شخصي',
        'user_form':user_form,
        'img_form':img_form,
    }

    return render(request, 'user/update_profile.html',context)