from django.shortcuts import render
from .models import Katalog
from .forms import KatalogForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
import json
from django.contrib import messages


def index(request):
    posts = Katalog.objects.all()
    response = {'posts':posts}
    return render(request,'katalog_list.html',response)

@login_required(login_url='/hello')
def add_katalog(request):
    form = KatalogForm(request.POST or None)
    if (form.is_valid() and request.method=='POST'):
        form.save()
        # messages.success(request, '.')
        return HttpResponseRedirect('/list_katalog')

    response = {'form':form}
    return render(request,'katalog_form.html',response)