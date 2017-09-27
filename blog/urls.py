from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^topics/$',views.topics,name='topics'),
    url(r'article/(?P<post_id>\d+)/$',views.article,name='article'),
    url(r'^about/$',views.about,name='about'),
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic')
]