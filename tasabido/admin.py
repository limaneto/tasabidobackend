from django.contrib import admin
from .models import Duvida, Materia, Subtopico, Monitoria, Moeda
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Duvida)
admin.site.register(Materia)
admin.site.register(Monitoria)
admin.site.register(Subtopico)
admin.site.register(Moeda)