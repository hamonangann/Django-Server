from .models import Promo
from .forms import PromoForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
import json
from django.shortcuts import render


def index(request):
    posts = Promo.objects.all()
    response = {'posts':posts}
    return render(request,'promo_list.html',response)

@login_required(login_url='/hello')
def add_promo(request):
    form = PromoForm(request.POST or None)
    if (form.is_valid() and request.method=='POST'):
        form.save()
        return HttpResponseRedirect('')

    response = {'form':form}
    return render(request,'promo_form.html',response)

# @login_required()
# def delete_konten(request):