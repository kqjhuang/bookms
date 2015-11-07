
from django.conf.urls import url
from .models import *
from .views import *

urlpatterns =[

    url(r'^book/create/$', create_book, name='create_book'),
    url(r'^book/list/$', list_book, name='list_book'),
    url(r'^book/edit/(?P<id>[^/]+)/$', edit_book, name='edit_book'),
    url(r'^book/view/(?P<id>[^/]+)/$', view_book, name='view_book'),
    
]
