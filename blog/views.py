from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from .models import Post,Topic,Messge
from django.core.paginator import  Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import MessForm

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator)
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'blog/topics.html',context)

def article(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    context = {'post': post}
    return render(request, 'blog/article.html',context)

def about(request):
    return  render(request, 'blog/about.html')

def topic(request,topic_id):
    topic = get_object_or_404(Topic,id=topic_id)
    posts = topic.post_set.order_by('-published_date')
    context = {'topic':topic,'posts':posts}
    return render(request,'blog/topic.html',context)

def messge(request):
    if request.method != 'POST':
        form = MessForm()
    else:
        form = MessForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:messge'))
    messger = Messge.objects.order_by('-time')
    paginator = Paginator(messger, 6)
    page = request.GET.get('page')
    try:
        messger = paginator.page(page)
    except PageNotAnInteger:
        messger = paginator.page(1)
    except EmptyPage:
        messger = paginator.page(paginator)
    context = {'form':form,'messger':messger}
    return render(request,'blog/messge.html',context)