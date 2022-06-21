"""emcali URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Home import views

from Home.views import CamView, HelloView, EstView, SerView
from Home.views import NewView, ApView, SolView, SunView, IntView,AboutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HelloView.as_view()),
    path('statics/', NewView.as_view()),
    path('campanario/', CamView.as_view()),
    path('aprotec/', ApView.as_view()),
    path('energiaSolar/', SolView.as_view()),
    path('sunnyFuture/', SunView.as_view()),
    path('integral/', IntView.as_view()),
    path('estacion/', EstView.as_view()),
    path('servidor/', SerView.as_view()),
    path('registro/', views.home),
    path('registros/', views.registros),
    path('aboutUs/', AboutView.as_view()),
    path("editarPersona/", views.editarPersona),
    path('registro/eliminarPersona/<Documento>', views.eliminarPersona),
    path('registro/edicionPersona/<Documento>', views.edicionPersona),
]

#registros/ es la coneccion del backend con el frontend
#NO SE PUEDE MODIFICAR REGISTRO O REGISTROS!!!