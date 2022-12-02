from django.shortcuts import render
from .models import Konten
from .forms import KontenForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
import json


def index(request):
    posts = Konten.objects.all()
    response = {'posts':posts}
    return render(request,'konten_list.html',response)

@login_required(login_url='/hello')
def add_konten(request):
    form = KontenForm(request.POST or None)
    if (form.is_valid() and request.method=='POST'):
        form.save()
        return HttpResponseRedirect('')
    
    response = {'form':form}
    return render(request,'konten_form.html',response)

# @login_required()
# def delete_konten(request):

