from django.contrib import admin

# Register your models here.
from api import models


class ProcedimientosAdmin(admin.ModelAdmin):
    readonly_fields = ('fechaFin',)

class ActividadesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'fechaInicio', 'dias', 'fechaFin', 'post_usuario', 'jerarquia', 'valor')

    def post_usuario(self, obj):
        return obj.idProcedimientoFk

    post_usuario.short_description = "Usuario"

admin.site.register(models.Procedimientos)
admin.site.register(models.Actividades, ActividadesAdmin)