from django.contrib import admin
from .models import Duvida, Materia, Subtopico, Monitoria, Moeda
from django.contrib.auth.models import User


class SubtopicoInline(admin.StackedInline):
    model = Subtopico
    extra = 0


class DuvidaInline(admin.StackedInline):
    model = Duvida
    extra = 0


class SubtopicoAdmin(admin.ModelAdmin):
    inlines = (DuvidaInline,)


class MateriaAdmin(admin.ModelAdmin):
    inlines = (SubtopicoInline,)


class DuvidaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "subtopico",)

class MonitoriaAdmin(admin.ModelAdmin):
    list_display = ("titulo",)


# Register your models here.
admin.site.register(Duvida, DuvidaAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Monitoria, MonitoriaAdmin)
admin.site.register(Subtopico, SubtopicoAdmin)
admin.site.register(Moeda)
