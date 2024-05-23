from django.urls import path
from .import views
from .views import Post_Creat_view

urlpatterns = [
    path('',views.home, name='home'),
    path('detail/<int:post_id>/',views.post_detail, name='detail'),
    path('newpost/',views.Post_Creat_view.as_view(), name='newpost'),
]