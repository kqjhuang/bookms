
from django.conf.urls import url
from .models import *
from .views import *

urlpatterns =[

    url(r'^person/create/$', create_person, name='create_person'),
    url(r'^person/list/$', list_person, name='list_person'),
    url(r'^person/edit/(?P<id>[^/]+)/$', edit_person, name='edit_person'),
    url(r'^person/view/(?P<id>[^/]+)/$', view_person, name='view_person'),

    url(r'^$', login, name='login'),
    url(r'^login/$',login,name = 'login'),
    url(r'^regist/$',regist,name = 'regist'),
    url(r'^index/$',index,name = 'index'),
    url(r'^logout/$',logout,name = 'logout'),

]
