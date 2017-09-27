from django.shortcuts import render
from django.utils import timezone
from .models import Post,Topic

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    context={'posts': posts}
    return render(request, 'blog/index.html', context)

def topics(request):
    topics=Topic.objects.order_by('date_added')
    context={'topics': topics}
    return render(request, 'blog/topics.html',context)

def article(request,post_id):
    post=Post.objects.get(id=post_id)
    context={'post': post}
    return render(request, 'blog/article.html',context)

def about(request):
    return  render(request, 'blog/about.html')

def topic(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    posts=topic.post_set.order_by('-published_date')
    context={'topic':topic,'posts':posts}
    return render(request,'blog/topic.html',context)