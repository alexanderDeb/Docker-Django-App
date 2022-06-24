from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
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
    path('accounts/', include('django.contrib.auth.urls'))
]