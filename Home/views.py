from pydoc import render_doc
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Persona
from django.contrib.auth.decorators import login_required


class HelloView(TemplateView):
    template_name = "index.html"

class NewView(TemplateView):
    template_name = "statics.html"

class CamView(TemplateView):
    template_name = "campanario.html"

class ApView(TemplateView):
    template_name = "aprotec.html"

class SolView(TemplateView):
    template_name = "energiaSolar.html"

class AboutView(TemplateView):
    template_name = "aboutUs.html"

class SunView(TemplateView):
    template_name = "sunnyFuture.html"

class IntView(TemplateView):
    template_name = "integral.html"

class EstView(TemplateView):
    template_name = "laEstacion.html"

class SerView(TemplateView):
    template_name = "servidor.html"

def home(request):
    persona = Persona.objects.all()
    return render(request, "register.html", {"personas": persona})

def registros(request):
    Documento=request.POST['txtDocumento']
    Nombre=request.POST['txtNombre']
    Correo=request.POST['txtCorreo']

    persona=Persona.objects.create(documento=Documento, nombre=Nombre, correo=Correo)
    return redirect('/registro/')

def eliminarPersona(request,Documento):
    persona = Persona.objects.get(documento=Documento)
    persona.delete()
    return redirect('/registro/')

def editarPersona(request):
    Documento=request.POST['txtDocumento']
    Nombre=request.POST['txtNombre']
    Correo=request.POST['txtCorreo']

    persona = Persona.objects.get(documento=Documento)
    persona.nombre = Nombre
    persona.correo = Correo
    persona.save()

    return redirect('/registro/')



def edicionPersona(request,Documento):
    persona = Persona.objects.get(documento=Documento)
    return render(request, "edicionPersona.html", {"PERSONA":persona})