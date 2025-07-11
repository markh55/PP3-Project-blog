from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('posts/<int:id>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:id>/', views.post_detail, name='post_detail'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]