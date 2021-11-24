import django
from django.http import response
from django.shortcuts import redirect, render
from django.http.response import HttpResponse, HttpResponseRedirect
from register.forms import CategoriasTrabajoForm, ContactForm, CvForm, EditaPerfil, EmpresasForm, ofertasEmpleoForm
from .models import CV, CategoriasTrabajo, Empresa, Estado, Genero, OfertaDeEmpleo, Postulante, PruebaPostulante
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator
from django.core.mail import send_mail, BadHeaderError
from django. conf import settings
from django.db.models import Q
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.


def index(response):
    ct = CategoriasTrabajo.objects.all()
    s = response.user.groups.filter(name="Solicitante").exists()
    r = response.user.groups.filter(name="Reclutador").exists()
    a = response.user.groups.filter(name="Administrador").exists()

    return render(response, "main/home.html", {"ct": ct, "s": s, "r": r, "a": a})


def home(response):
    ct = CategoriasTrabajo.objects.all()
    s = response.user.groups.filter(name="Solicitante").exists()
    r = response.user.groups.filter(name="Reclutador").exists()
    a = response.user.groups.filter(name="Administrador").exists()
    # queryset = response.GET.get("categoria")
    # print(queryset)
    # if queryset:
    #     cat = CategoriasTrabajo.objects.filter(nombre=queryset).first()
    #     ofertas = OfertaDeEmpleo.objects.filter(
    #         Q(categoria=cat)
    #     ).distinct()
    #     print(ofertas)
    #     return render(response, 'main/consultatrabajos.html', {"s": s, "r": r, "a": a, "ofertas": ofertas})
    return render(response, "main/home.html", {"ct": ct, "s": s, "r": r, "a": a})


def create(response):
    return render(response, "main/create.html")


def empresas(response):
    empresa = Empresa.objects.all()
    paginator = Paginator(empresa, 3)
    page = response.GET.get('page')
    empresa = paginator.get_page(page)
    s = response.user.groups.filter(name="Solicitante").exists()
    r = response.user.groups.filter(name="Reclutador").exists()
    a = response.user.groups.filter(name="Administrador").exists()
    return render(response, 'main/empresas.html', {"s": s, "r": r, "a": a, "empresa": empresa})


def correo(response):
    return render(response, "main/correo.html", {})


def cvs(request, user_name):
    usuario = CV.objects.filter(id_usuario__username=user_name).first()
    form = CvForm()

    if request.method == "POST":
        if usuario:
            form = CvForm(request.POST, request.FILES or None,
                          instance=usuario)
        else:
            form = CvForm(request.POST, request.FILES or None,
                          initial={'id_usuario': request.user})
        if form.is_valid:
            # genero = Genero.objects.filter(
            #     nombre=request.POST.get('id_sexo')).first()
            # form.sexo = genero
            form.save()
            ct = CategoriasTrabajo.objects.all()
            s = request.user.groups.filter(name="Solicitante").exists()
            r = request.user.groups.filter(name="Reclutador").exists()
            a = request.user.groups.filter(name="Administrador").exists()
            return render(request, 'main/empresas.html', {"s": s, "r": r, "a": a, "ct": ct})
    else:
        usuario = CV.objects.filter(id_usuario__username=user_name).first()
        if usuario:
            form = CvForm(instance=usuario)
            return render(request, 'main/cv.html', {"form": form})
        else:
            print('si')
            form = CvForm(
                initial={'id_usuario': User.objects.get(id=request.user.id)})
            return render(request, 'main/cv.html', {"form": form})
    return render(request, 'main/cv.html', {"form": form})


def detallesCv(response, id_user):
    ct = CategoriasTrabajo.objects.all()
    s = response.user.groups.filter(name="Solicitante").exists()
    r = response.user.groups.filter(name="Reclutador").exists()
    a = response.user.groups.filter(name="Administrador").exists()
    cv = CV.objects.filter(id_usuario=id_user).first()
    if cv:
        return render(response, 'main/detallecv.html', {"s": s, "r": r, "a": a, "cv": cv})
    else:
        return render(response, 'main/home.html', {"s": s, "r": r, "a": a, "ct": ct})


def agregarOfertaDeEmpleo(request):
    s = request.user.groups.filter(name="Solicitante").exists()
    r = request.user.groups.filter(name="Reclutador").exists()
    a = request.user.groups.filter(name="Administrador").exists()
    form = ofertasEmpleoForm()
    if request.method == "POST":
        form = ofertasEmpleoForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('', {"s": s, "r": r, "a": a, "form": form})
    else:
        print("No es post")
        form = ofertasEmpleoForm()
        return render(request, 'main/agregaroferta.html', {"s": s, "r": r, "a": a, "form": form})
    return render(request, 'main/agregaroferta.html', {"s": s, "r": r, "a": a, "form": form})


def detalleEmpresa(response, id):
    empresa = Empresa.objects.get(id=id)
    propuestas = OfertaDeEmpleo.objects.all().filter(empresa=id).count()
    print(propuestas)
    s = response.user.groups.filter(name="Solicitante").exists()
    r = response.user.groups.filter(name="Reclutador").exists()
    a = response.user.groups.filter(name="Administrador").exists()
    return render(response, 'main/detallempresa.html', {"empresa": empresa, "s": s, "r": r, "a": a, "propuesta": propuestas})


def modificaEmpresa(request, id):
    empresa = Empresa.objects.filter(id=id).first()
    form = EmpresasForm(instance=empresa)
    s = request.user.groups.filter(name="Solicitante").exists()
    r = request.user.groups.filter(name="Reclutador").exists()
    a = request.user.groups.filter(name="Administrador").exists()
    if request.method == "POST":
        form = EmpresasForm(
            request.POST, request.FILES or None, instance=empresa)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('', {"s": s, "r": r, "a": a, "form": form})
    else:
        form = EmpresasForm(instance=empresa)
        return render(request, 'main/modificaempresa.html', {"a": a, "s": s, "r": r, "form": form})
    return render(request, 'main/modificaempresa.html', {"a": a, "s": s, "r": r, "form": form})


def agregarEmpresa(request):
    form = EmpresasForm()
    s = request.user.groups.filter(name="Solicitante").exists()
    r = request.user.groups.filter(name="Reclutador").exists()
    a = request.user.groups.filter(name="Administrador").exists()
    print(a)
    if request.method == "POST":
        form = EmpresasForm(request.POST, request.FILES or None)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('', {"s": s, "r": r, "a": a, "form": form})
        else:
            form = EmpresasForm()
            return render(request, 'main/agregarEmpresa.html', {"s": s, "r": r, "a": a, "form": form})
    return render(request, 'main/agregarEmpresa.html', {"s": s, "r": r, "a": a, "form": form})


def eliminarEmpresa(request, id):
    ct = CategoriasTrabajo.objects.all()
    s = request.user.groups.filter(name="Solicitante").exists()
    r = request.user.groups.filter(name="Reclutador").exists()
    a = request.user.groups.filter(name="Administrador").exists()
    empresa = Empresa.objects.get(id=id)
    empresa.delete()
    return render(request, 'main/home.html', {"s": s, "r": r, "a": a, "ct": ct})


def consultaOfertaDeEmpleo(response):
    s = response.user.groups.filter(name="Solicitante").exists()
    r = response.user.groups.filter(name="Reclutador").exists()
    a = response.user.groups.filter(name="Administrador").exists()

    ofertas = OfertaDeEmpleo.objects.filter(estado=1)
    misodertas = Postulante.objects.filter(usuario=response.user)
    paginator = Paginator(ofertas, 3)
    page = response.GET.get('page')
    ofertas = paginator.get_page(page)
    form = CategoriasTrabajoForm()
    queryset = response.GET.get("categoria")
    if queryset:
        ofertas = OfertaDeEmpleo.objects.filter(
            estado=1).filter(categoria=queryset)
        misodertas = Postulante.objects.filter(usuario=response.user)
        paginator = Paginator(ofertas, 3)
        page = response.GET.get('page')
        ofertas = paginator.get_page(page)
        return render(response, 'main/consultatrabajos.html', {"s": s, "r": r, "a": a, "ofertas": ofertas, "misofertas": misodertas, "form": form})
    return render(response, 'main/consultatrabajos.html', {"s": s, "r": r, "a": a, "ofertas": ofertas, "misofertas": misodertas, "form": form})


def detalleOfertaDeEmpleo(response, id_oferta):
    oferta = OfertaDeEmpleo.objects.get(id=id_oferta)
    s = response.user.groups.filter(name="Solicitante").exists()
    r = response.user.groups.filter(name="Reclutador").exists()
    a = response.user.groups.filter(name="Administrador").exists()
    return render(response, 'main/detalletrabajo.html', {"s": s, "r": r, "a": a, "oferta": oferta})


def eliminaOferta(response, id_oferta):
    s = response.user.groups.filter(name="Solicitante").exists()
    r = response.user.groups.filter(name="Reclutador").exists()
    a = response.user.groups.filter(name="Administrador").exists()
    ct = CategoriasTrabajo.objects.all()
    ofertas = OfertaDeEmpleo.objects.get(id=id_oferta)
    ofertas.delete()
    return render(response, 'main/home.html', {"s": s, "r": r, "a": a, "ct": ct})


def agregaPostulante(response, id_oferta):
    ct = CategoriasTrabajo.objects.all()
    s = response.user.groups.filter(name="Solicitante").exists()
    r = response.user.groups.filter(name="Reclutador").exists()
    a = response.user.groups.filter(name="Administrador").exists()
    ofertas = PruebaPostulante.objects.filter(
        oferta=id_oferta).filter(usuario=response.user.id)
    if not ofertas:
        prueba = PruebaPostulante()
        prueba.oferta = OfertaDeEmpleo.objects.get(id=id_oferta)
        prueba.usuario = response.user
        prueba.save()
        return render(response, 'main/home.html', {"s": s, "r": r, "a": a, "ct": ct})
    else:
        return render(response, 'main/home.html', {"s": s, "r": r, "a": a, "ct": ct})


def muestraReclutados(response):
    s = response.user.groups.filter(name="Solicitante").exists()
    r = response.user.groups.filter(name="Reclutador").exists()
    a = response.user.groups.filter(name="Administrador").exists()
    postulantes = PruebaPostulante.objects.filter(
        estado=3).filter(oferta__reclutador=response.user.id).order_by('usuario')
    paginator = Paginator(postulantes, 4)
    page = response.GET.get('page')
    postulantes = paginator.get_page(page)
    if s:
        postulantes = PruebaPostulante.objects.filter(
            estado=3).order_by('usuario')
        paginator = Paginator(postulantes, 4)
        page = response.GET.get('page')
        postulantes = paginator.get_page(page)
        return render(response, 'main/reclutados.html', {"s": s, "r": r, "a": a, "postulantes": postulantes})
    return render(response, 'main/reclutados.html', {"s": s, "r": r, "a": a, "postulantes": postulantes})


def rechazaRecluta(response, id_postulacion):
    ct = CategoriasTrabajo.objects.all()
    s = response.user.groups.filter(name="Solicitante").exists()
    r = response.user.groups.filter(name="Reclutador").exists()
    a = response.user.groups.filter(name="Administrador").exists()
    postulacion = PruebaPostulante.objects.filter(id=id_postulacion).first()
    estado = Estado.objects.get(id=2)
    postulacion.estado = estado
    postulacion.save()
    postulantes = PruebaPostulante.objects.filter(estado=3)
    paginator = Paginator(postulantes, 4)
    page = response.GET.get('page')
    postulantes = paginator.get_page(page)
    return render(response, 'main/home.html', {"s": s, "r": r, "a": a, "ct": ct})


def aceptaRecluta(response, id_postulacion):
    ct = CategoriasTrabajo.objects.all()
    s = response.user.groups.filter(name="Solicitante").exists()
    r = response.user.groups.filter(name="Reclutador").exists()
    a = response.user.groups.filter(name="Administrador").exists()
    postulacion = PruebaPostulante.objects.filter(id=id_postulacion).first()
    estado = Estado.objects.get(id=1)
    postulacion.estado = estado
    postulacion.save()
    oferta = OfertaDeEmpleo.objects.get(id=postulacion.oferta.id)
    oferta.estado = 2
    oferta.save()
    postulantes = PruebaPostulante.objects.filter(estado=3)
    paginator = Paginator(postulantes, 4)
    page = response.GET.get('page')
    postulantes = paginator.get_page(page)
    return render(response, 'main/home.html', {"s": s, "r": r, "a": a, "ct": ct})


def editarPerfil(response):
    s = response.user.groups.filter(name="Solicitante").exists()
    r = response.user.groups.filter(name="Reclutador").exists()
    a = response.user.groups.filter(name="Administrador").exists()
    usuario = User.objects.get(id=response.user.id)
    form = EditaPerfil(instance=usuario)
    if response.method == "POST":
        form = EditaPerfil(response.POST, instance=usuario)
        if form.is_valid:
            form.save()
        else:
            return HttpResponseRedirect('', {"s": s, "r": r, "a": a, "form": form})
    else:
        form = EditaPerfil(instance=usuario)
        return render(response, 'main/perfil.html', {"s": s, "r": r, "a": a, "form": form})
    return render(response, 'main/perfil.html', {"s": s, "r": r, "a": a, "form": form})


def enviaCorreo(request):
    s = request.user.groups.filter(name="Solicitante").exists()
    r = request.user.groups.filter(name="Reclutador").exists()
    a = request.user.groups.filter(name="Administrador").exists()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "contacto"
            email = request.POST.get('email_address')
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values())
            desde = settings.EMAIL_HOST_USER

            try:
                send_mail(subject, message, email,
                          ['proyectoprograweb2@gmail.com'])
                print("enviado")
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('', {"s": s, "r": r, "a": a, "form": form})

    form = ContactForm()
    return render(request, "main/contacto.html", {"s": s, "r": r, "a": a, "form": form})


def misPostulaciones(response):
    s = response.user.groups.filter(name="Solicitante").exists()
    r = response.user.groups.filter(name="Reclutador").exists()
    a = response.user.groups.filter(name="Administrador").exists()
    postulantes = PruebaPostulante.objects.filter(usuario=response.user.id)
    paginator = Paginator(postulantes, 4)
    page = response.GET.get('page')
    postulantes = paginator.get_page(page)
    return render(response, 'main/mispostulaciones.html', {"s": s, "r": r, "a": a, "postulantes": postulantes})


def preguntas(response):
    s = response.user.groups.filter(name="Solicitante").exists()
    r = response.user.groups.filter(name="Reclutador").exists()
    a = response.user.groups.filter(name="Administrador").exists()
    return render(response, 'main/preguntas.html', {"s": s, "r": r, "a": a})


def modificaOfertaDeTrabajo(request, id):
    empresa = OfertaDeEmpleo.objects.filter(id=id).first()
    form = ofertasEmpleoForm(instance=empresa)
    s = request.user.groups.filter(name="Solicitante").exists()
    r = request.user.groups.filter(name="Reclutador").exists()
    a = request.user.groups.filter(name="Administrador").exists()
    if request.method == "POST":
        form = ofertasEmpleoForm(
            request.POST, instance=empresa)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('', {"s": s, "r": r, "a": a, "form": form})
    else:
        form = ofertasEmpleoForm(instance=empresa)
        return render(request, 'main/modificaoferta.html', {"a": a, "s": s, "r": r, "form": form})
    return render(request, 'main/modificaoferta.html', {"a": a, "s": s, "r": r, "form": form})


def password_change(request):
    ct = CategoriasTrabajo.objects.all()
    s = request.user.groups.filter(name="Solicitante").exists()
    r = request.user.groups.filter(name="Reclutador").exists()
    a = request.user.groups.filter(name="Administrador").exists()
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            print('si')
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect('', {"ct": ct, "s": s, "r": r, "a": a})
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'main/passwordchange.html', {"a": a, "s": s, "r": r, "form": form})
    return render(request, 'main/passwordchange.html', {"a": a, "s": s, "r": r, "form": form})

def respaldo(response):
    s = response.user.groups.filter(name="Solicitante").exists()
    r = response.user.groups.filter(name="Reclutador").exists()
    a = response.user.groups.filter(name="Administrador").exists()
    return render(response, 'main/respaldo.html', {"a": a, "s": s, "r": r})    