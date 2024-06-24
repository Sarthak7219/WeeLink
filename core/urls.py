from django.urls import path
from .views import *




urlpatterns = [
    path('', home, name='home'),
    path('profile/<int:id>/', profile_view, name='profile'),
    path('profile-edit/', update_profile, name='update_profile'),
    path('create-post/', create_post, name='create_post'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),
    path('post/<int:post_id>/like-dislike', addLike, name='like-dislike'),
    path('create-comment/<int:post_id>/', create_comment, name='create_comment'),
    path('profile-search/', profile_search, name='profile_search'),

]

