from django.http import HttpResponse
from django.shortcuts import render
from django.templatetags.static import static
from web.models import Banda, Evento, Noticia
from django.core.mail import send_mail
from brigadas_metalicas.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage 
from django.db.models import Q 
# Create your views here.

def index(request):
    fotos_bandas = [
        { "url_foto": static("web/images/eroica.png"), "nombre": "EROICA" },
        { "url_foto": static("web/images/lady_macbeth.png"), "nombre": "LADY MACBETH" },
        { "url_foto": static("web/images/ironia.png"), "nombre": "IRONIA" },
        { "url_foto": static("web/images/nystagmos.png"), "nombre": "NYSTAGMOS" },
    ]
    noticias = Noticia.objects.all().order_by("-fecha_alta")[:6]
    eventos = Evento.objects.all().order_by("fecha_evento")[:2]
    contexto = {
        "fotos_bandas": fotos_bandas,
        "noticias" : noticias,
        "eventos" : eventos
    }
    return render(request, "web/index.html", context=contexto)

def about(request):
    return render(request, "web/nosotros.html")

def our_music(request):
    return render(request, "web/index-2.html")

def bandas(request):
    bandas = Banda.objects.all()
    contexto = {
        "bandas": bandas
    }
    return render(request, "web/bandas.html", context=contexto)

def galeria(request):
    return render(request, "web/galeria.html")

def eventos(request):
    noticias = Noticia.objects.all().order_by("-fecha_alta")
    ultima_noticia = noticias[0]
    noticias = noticias[1:7]
    eventos = Evento.objects.all().order_by("fecha_evento")[:7]
    contexto = {
        "ultima_noticia" : ultima_noticia,
        "noticias": noticias,
        "eventos" : eventos
    }
    return render(request, "web/eventos.html", context=contexto)

def contacto(request):
    return render(request, "web/contacto.html")

def buscar_banda(request):
    busqueda = request.POST.get("busqueda")
    bandas = Banda.objects.filter(
        Q(nombre__icontains=busqueda) | Q(estilo__icontains=busqueda) | Q(residencia__icontains=busqueda) | Q(integrantes__icontains=busqueda)
    )
    print(bandas.query)
    contexto = {
        "bandas": bandas,
        "busqueda": busqueda 
    }
    return render(request, "web/busqueda.html", context=contexto)      

def enviar_correo(request): 
    nombre = request.POST["nombre"]
    email_remitente = request.POST["email_remitente"]
    contenido = request.POST["contenido"]

    email = EmailMessage(
        "Asunto del mensaje",
        "De {} <{}>\n\nEscribio:\n\n{}".format(nombre, email_remitente, contenido),
        email_remitente,
        [EMAIL_HOST_USER],
        reply_to=[email_remitente]
    )

    contexto = {
        "mensaje" : "Gracias por contactarnos"
    }

    try:
        email.send()
    except:
        contexto["mensaje"] = "Se rompió un cuerda, mandanos un mail"
    
    return render(request, "web/contacto.html", context=contexto)
