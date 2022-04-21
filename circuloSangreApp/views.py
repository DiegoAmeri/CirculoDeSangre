from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "circuloSangreApp/home.html")


def bancoSangre(request):

    return render(request, "circuloSangreApp/bancoSangre.html")


def pago(request):

    return render(request, "circuloSangreApp/pago.html")


def contacto(request):

    return render(request, "circuloSangreApp/contacto.html")

def login(request):

    return render(request, "circuloSangreApp/login.html")

