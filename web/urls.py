from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
    path("our_music", views.our_music, name="our_music"),
    path("bandas", views.bandas, name="bandas"),
    path("galeria", views.galeria, name="galeria"),
    path("eventos", views.eventos, name="eventos"),
    path("contacto", views.contacto, name="contacto"),
    path("enviar_correo", views.enviar_correo, name="enviar_correo"),
    path("buscar_banda", views.buscar_banda, name="buscar_banda"),

]

urlpatterns += static (settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)