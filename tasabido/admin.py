from django.contrib import admin
from .models import Usuario, Duvida, Ajuda, Materia, Subtopico

# Register your models here.


admin.site.register(Usuario)
admin.site.register(Duvida)
admin.site.register(Ajuda)
admin.site.register(Materia)
admin.site.register(Subtopico)