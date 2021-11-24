from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.home, name="home"),
    path('create/', views.create, name="create"),
    # path('empresas/baja', views, name="empresas/baja"),
    path('empresas/', views.empresas, name="empresas"),
    path('contacto/', views.correo, name="contacto"),
    path('cv/<str:user_name>', views.cvs, name="cvs"),
    path('detallecv/<int:id_user>', views.detallesCv, name="detalleCv"),
    path('ofertas/', views.agregarOfertaDeEmpleo, name="ofertaempleo"),
    path('detallesoferta/<int:id_oferta>',
         views.detalleOfertaDeEmpleo, name="detalleoferta"),
    path('empresas/<int:id>', views.detalleEmpresa, name="detallempresa"),
    path('modicacion/<int:id>', views.modificaEmpresa, name="modificaempresa"),
    path('agregarEmpresa/', views.agregarEmpresa, name="agregarempresa"),
    path('eliminarEmpresa/<int:id>', views.eliminarEmpresa, name="eliminarempresa"),
    path('trabajos/', views.consultaOfertaDeEmpleo, name="ofertasempleo"),
    path('<int:id_oferta>', views.agregaPostulante, name="agregapostulante"),
    path('postulantes/',  views.muestraReclutados, name="reclutados"),
    path('rechazado/<int:id_postulacion>',
         views.rechazaRecluta, name="rechazarecluta"),
    path('aceptado/<int:id_postulacion>',
         views.aceptaRecluta, name="aceptarecluta"),
    path('perfil/', views.editarPerfil, name="perfil"),
    path('contact/', views.enviaCorreo, name="contactus"),
    path('mispostulaciones/', views.misPostulaciones, name="postulaciones"),
    path('preguntas/', views.preguntas, name='preguntas'),
    path('borraOferta/<int:id_oferta>',
         views.eliminaOferta, name="eliminaOferta"),
    path('modificaOferta/<int:id>', views.modificaOfertaDeTrabajo,
         name="modificaOfertaEmpleo"),
    path('passwordchange/', views.password_change, name="passwordchange"),
    path('respaldo/', views.respaldo, name="respaldo")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
