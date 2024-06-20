from django.urls import path
from .views import *




urlpatterns = [
    path('', home, name='home'),
    path('profile/<int:id>/', profile_view, name='profile'),
    path('create-post/', create_post, name='create_post'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),
    path('post/<int:post_id>/like-dislike', addLike, name='like-dislike'),
    path('profile-search/', profile_search, name='profile_search'),

]

