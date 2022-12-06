from .models import Promo
from .forms import PromoForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
import json
from django.shortcuts import redirect, render
import datetime

def index(request):
    form = PromoForm(request.POST or None)
    if (form.is_valid() and request.method=='POST'):
        form.save()
        return redirect("/promo/")
    posts = Promo.objects.all()
    response = {'posts':posts, 'form': form}
    return render(request,'promo_list.html',response)

def create_promo(request):
    print("dsajnbhdjnsa")
    if request.method == "POST":
        nama_promo = request.POST.get("nama_promo")
        gambar_promo = request.POST.get("gambar_promo")
        details_promo = request.POST.get("details_promo")
        tanggal_berakhir = request.POST.get("tanggal_berakhir")
        print(datetime.datetime.strptime(tanggal_berakhir, "%Y-%m-%d").date())

        list_promo = Promo.objects.all()
        promo = Promo(len(list_promo) + 1, nama_promo, gambar_promo, details_promo, datetime.datetime.strptime(tanggal_berakhir, "%Y-%m-%d").date())
        promo.save()
        return HttpResponse(serializers.serialize('json', [promo, ]), content_type='application/json')

    return JsonResponse({"error": "Edit Failed"}, status=400)


def renderJSON(request):
    promo = Promo.objects.all()
    data = serializers.serialize('json', promo)
    return HttpResponse(data, content_type="application/json")


# @login_required()
# def delete_konten(request):