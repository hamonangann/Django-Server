from django.shortcuts import render
from .models import Katalog
from .forms import KatalogForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
import json
from django.contrib import messages
from django.http import HttpResponse, Http404


def index(request):
    posts = Katalog.objects.all()
    response = {'posts':posts}
    return render(request,'katalog_list.html',response)

@login_required(login_url='/hello')
def add_katalog(request):
    form = KatalogForm(request.POST or None)
    if (form.is_valid() and request.method=='POST'):
        try :
            form.save()
            # messages.success(request, '.')
            return render(request, 'katalog_forms.html', {"success": "valid", 'form': form})
        except :
            return render(request, 'katalog_forms.html', {"success": "invalid", 'form': form})

    response = {'form':form, "success":"None"}
    return render(request,'katalog_forms.html',response)

def detail_katalog(request, idKatalog):
    try:
        katalog = Katalog.objects.get(pk=idKatalog)
    except Katalog.DoesNotExist:
        raise Http404("Katalog not found")

    return render(request, "detail_katalog.html", context={"katalog":katalog} )