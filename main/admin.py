from django.contrib import admin

from main.models import CV, CategoriasTrabajo, Empresa, Estado, Genero, OfertaDeEmpleo, Perfiles, Postulante, PruebaPostulante, TipoDeTrabajo

# Register your models here.
admin.site.register(CategoriasTrabajo)
admin.site.register(Empresa)
admin.site.register(Perfiles)
admin.site.register(Genero)
admin.site.register(TipoDeTrabajo)
admin.site.register(OfertaDeEmpleo)
admin.site.register(CV)
admin.site.register(Postulante)
admin.site.register(PruebaPostulante)
admin.site.register(Estado)
