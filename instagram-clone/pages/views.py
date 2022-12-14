from django.shortcuts import render, redirect
from myuser.models import MyUser
from posts.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.loader import render_to_string
from django.http import JsonResponse
from actions.models import Action
from django.db.models import Count

def home(request):
    user = request.user
    if user.is_authenticated:
        posts = Post.objects.filter(user=user).order_by("-created")
        if user.following.all():
            for friend in user.following.all():
                friends_posts = Post.objects.filter(user=friend)
                posts |= friends_posts
                
        paginator = Paginator(posts, 6)
        try:
            page = request.GET.get("page")
            if page:
                posts = paginator.page(page)
                return JsonResponse({
                    "status": render_to_string("pages/ajax_posts.html", {"posts": posts}, request=request)
                })
            else:
                posts = paginator.page(1)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            return JsonResponse({"status": "empty"})
        actions = Action.objects.exclude(user=user).order_by("-created")
        following_ids = user.following.values_list("id", flat=True)
        if following_ids:
            actions = actions.filter(user_id__in=following_ids)[:10]
        user_followings = MyUser.objects.filter(id__in=following_ids)
        suggest_list = MyUser.objects.none()
        for follow in user_followings.all():
            for suggest_user in follow.following.all():
                if not suggest_user.id in following_ids and suggest_user != user:
                    suggest_user = MyUser.objects.filter(id=suggest_user.id)
                    suggest_list |= suggest_user
        suggest_list = suggest_list[:5]
    else:
        return redirect("login")
    return render(request, "pages/home.html", {"posts": posts, "actions": actions, "suggests": suggest_list})

def explore(request):
    posts = Post.objects.order_by("-total_likes")
    return render(request, "pages/explore.html", {"posts": posts})
