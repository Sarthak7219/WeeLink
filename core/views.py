from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages



@login_required
def home(request):

    user_profile = request.user.profile
    user_followed_profiles = user_profile.follows.all()
    user_followed_users = user_followed_profiles.values_list('user', flat=True)
    
    all_posts = Post.objects.filter(user__in=user_followed_users).order_by('-created_at')

    user_followed_profiles = user_profile.follows.exclude(pk=user_profile.pk)

    context = {
        'user_followed_profiles' :user_followed_profiles,
        'all_posts':all_posts,
       
    }
    return render(request, 'index.html', context)


@login_required
def profile_view(request, id):

    is_user = False
    user_profile = request.user.profile

    if id == request.user.profile.id:
        is_user = True


    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(id =id)


    if request.method == "POST":
        
        if 'follow' in request.POST or 'follow-friend' in request.POST:
            command = request.POST.get('follow') or request.POST.get('follow-friend')
            if command == "follow":
                user_profile.follows.add(profile)
            elif command == "unfollow":
                user_profile.follows.remove(profile)

    followed_profiles = profile.follows.exclude(pk=profile.pk)
    followed_by = profile.followed_by.exclude(pk=profile.pk)
    connected_profiles = followed_profiles | followed_by
    user_followed_profiles = user_profile.follows.exclude(pk=user_profile.pk)
    posts = profile.user.post.all().order_by('-created_at')

    

    profile_pic_url = "/static/images/user/default_profile.jpeg"
    if profile.image:
        profile_pic_url = profile.image.url

    profile_post_images = Image.objects.filter(post__user=profile.user)


    



    context = {
        'profile':profile,
        'profile_pic_url':profile_pic_url,
        'followed_profiles':followed_profiles,
        'followed_by':followed_by,
        'connected_profiles':connected_profiles,
        'following' : followed_profiles.count(),
        'followers' : followed_by.count(),
        'num_posts':posts.count(),
        'user_followed_profiles':user_followed_profiles,
        'posts': posts,
        'is_user': is_user,
        'profile_post_images':profile_post_images,
    }
    return render(request, 'profile.html', context)


@login_required
def create_post(request):

    if request.method == "POST":
        if 'post-text' in request.POST:
            body = request.POST.get('post-text')
    
            if 'post-image' in request.FILES:
              
                image = request.FILES['post-image']
                new_post = Post.objects.create(user=request.user, body=body)
                Image.objects.create(post=new_post, image=image)
                
            else:
                Post.objects.create(user=request.user, body=body)

        elif 'post-image' in request.FILES:
            image = request.FILES['post-image']
            new_post = Post.objects.create(user=request.user)
            Image.objects.create(post=new_post, image=image)

    return redirect('home')




@login_required
def delete_post(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id, user=request.user)
        post.delete()
        return redirect('profile', id=request.user.profile.id)


@login_required
def addLike(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    isLiked = False

    for like in post.likes.all():
        if like == user:
            isLiked = True

    if isLiked == True:
        post.likes.remove(user)

    else:
        post.likes.add(user)

    return redirect('home')


@login_required
def profile_search(request):
    profiles = Profile.objects.all()
    profile_list = []
    for profile in profiles:
        profile_list.append({
            'id': profile.id,
            'username': profile.user.username,
            'image_url': profile.image.url if profile.image else '/static/images/user/default_profile.jpeg'
        })
    return JsonResponse({'profiles': profile_list})

