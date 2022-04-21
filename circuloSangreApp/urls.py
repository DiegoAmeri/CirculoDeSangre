from django.urls import path
from circuloSangreApp import views

urlpatterns = [
    
    path('', views.home, name="home"),
    path('bancoSangre', views.bancoSangre, name="bancoSangre"),
    path('pago', views.pago, name="pago"),
    path('contacto', views.contacto, name="contacto"),
    path('login', views.login, name="login"),

]