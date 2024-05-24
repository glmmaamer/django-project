from django.urls import path
from .import views
from .views import Post_Creat_view, Post_update_view

urlpatterns = [
    path('',views.home, name='home'),
    path('detail/<int:post_id>/',views.post_detail, name='detail'),
    path('newpost/', Post_Creat_view.as_view(), name='newpost'),
    path('detail/<slug:pk>/update', Post_update_view.as_view(), name='update')
]