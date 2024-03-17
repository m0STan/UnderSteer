from django.http import Http404,HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.urls import reverse


def index(request):
    latest_posts_list = Post.objects.order_by('-posted_date')[:10]
    return render(request,'blogs/list.html',{'latest_posts_list':latest_posts_list})

def detail(request,post_id):
    try:
        p = Post.objects.get(id = post_id)
    except:
        raise Http404("Запись не найдена")
    latest_comments_list = p.comment_set.order_by('-id')
    return render(request, 'blogs/detail.html',{'post':p,'latest_comments_list':latest_comments_list})

def leave_comment(request,post_id):
    try:
        p = Post.objects.get(id = post_id)
    except:
        raise Http404("Запись не найдена")
    
    p.comment_set.create(author_name=request.POST['name'],comment_text = request.POST['text'],comment_date = timezone.now())
    return HttpResponseRedirect(reverse('blogs:detail',args=(p.id,)))