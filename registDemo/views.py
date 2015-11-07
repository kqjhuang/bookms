#coding:utf-8
# Create your views here.

from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.shortcuts import render,render_to_response
from django.core.urlresolvers import reverse

# app specific files

from .models import *
from .forms import *
from .forms import UserForm


def regist(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            Person.objects.create(name= username,password=password)
            return HttpResponse('regist success!!')
    else:
        uf = UserForm()
    return render_to_response('regist.html',{'uf':uf},context_instance=RequestContext(request))


def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = Person.objects.filter(name__exact = username,password__exact = password)
            if user:
                response = HttpResponseRedirect('/registDemo/index')
                response.set_cookie('username',username,3600)
                return response
        else:
            return HttpResponseRedirect('/registDemo/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(request))

def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('index.html' ,{'username':username})

def logout(req):
    response = HttpResponse('logout !!')
    # 清理cookie
    response.delete_cookie('username')
    return response

def create_person(request):
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = PersonForm()

    t = get_template('registDemo/create_person.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def list_person(request):

    list_items = Person.objects.all()
    paginator = Paginator(list_items ,10)


    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('registDemo/list_person.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_person(request, id):
    person_instance = Person.objects.get(id = id)

    t=get_template('registDemo/view_person.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_person(request, id):

    person_instance = Person.objects.get(id=id)

    form = PersonForm(request.POST or None, instance = person_instance)

    if form.is_valid():
        form.save()

    t=get_template('registDemo/edit_person.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))
