from django.contrib import admin

from .models import Cliente, Curso


class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'descricao')


class ClienteAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
            obj.save()
        super(ClienteAdmin, self).save_model(request, obj, form, change)
    list_display = ('nome', 'sobrenome', 'email')


admin.site.register(Curso, CursoAdmin)
admin.site.register(Cliente, ClienteAdmin)
