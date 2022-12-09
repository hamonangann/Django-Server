from django.shortcuts import render, redirect
from .models import Konten
from .forms import KontenForm
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages


def index(request):
    posts = Konten.objects.all()
    isAdmin = request.user.is_authenticated
    response = {'posts':posts, 'isAdmin':isAdmin}
    return render(request,'landing_page.html',response)

def indexAturKonten(request):
    posts = Konten.objects.all()
    response = {'posts':posts}
    return render(request,'atur_konten.html',response)

def detail_konten(request, idKonten):
    konten = Konten.objects.all().get(idKonten=idKonten)
    response = {'konten':konten}
    return render(request,'detail_konten.html',response)

@login_required(login_url='/hello')
def add_konten(request):
    form = KontenForm(request.POST or None)
    if (form.is_valid() and request.method=='POST'):
        form.save()
        messages.success(request,'Success')
        return HttpResponseRedirect(reverse('aturKonten'))
    
    response = {'form':form}
    return render(request,'konten_form.html',response)

@login_required(login_url='/hello')
def delete_konten(request, idKonten):
    data = Konten.objects.get(idKonten=idKonten)
    data.delete()
    return HttpResponseRedirect(reverse('aturKonten'))
