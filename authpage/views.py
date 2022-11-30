from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"Berhasil login sebagai {username}.")
                return HttpResponseRedirect('/hello')
            else:
                messages.error(request,"Gagal login, username atau password invalid.")

        else:
            messages.error(request,"Gagal login, username atau password invalid.")

    form = AuthenticationForm()
    return render(request, "lambda.html", {"form":form})

@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "Berhasil log out.")
    return HttpResponseRedirect('/hello')
