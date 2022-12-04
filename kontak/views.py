from django.shortcuts import render
from kontak.models import Kontak

from django.http import HttpResponse, HttpResponseNotFound


from django.core import serializers


# Create your views here.

def kontak(request):
    return render(request, "index_kontak.html")

def get_kontak_json(request):
    kontak_item = Kontak.objects.all()
    return HttpResponse(serializers.serialize('json', kontak_item))

def add_kontak(request):
    if request.method == 'POST':
        nama = request.POST.get("nama")
        alamat = request.POST.get("alamat")
        no_telpon= request.POST.get("no_telpon")
        email = request.POST.get("email")
        link = ""

        new_barang = Kontak(nama=nama, alamat=alamat, no_telpon=no_telpon, email=email, link=link)
        new_barang.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()
