from django.urls import path
from . import views

app_name = 'noticias'

# Urls de app noticias
urlpatterns = [

    path('', views.inicio, name="inicio"),

    # url para el detalle de la noticia por pk
    path('inicio<int:pk>', views.Inicio_Noticias, name='inicio'),

    # url del formulario de contacto
    path('contacto', views.contacto, name="contacto"),

    path ('comentario' , views.Comentar_Noticia, name='comentar')


]
