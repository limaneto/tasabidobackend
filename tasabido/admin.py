from django.contrib import admin
from .models import Duvida, Ajuda, Materia, Subtopico
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Duvida)
admin.site.register(Ajuda)
admin.site.register(Materia)
admin.site.register(Subtopico)