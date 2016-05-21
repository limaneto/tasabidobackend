from django.contrib import admin
from .models import Duvida, Ajuda, Materia, Subtopico, User

# Register your models here.
admin.site.register(User)
admin.site.register(Duvida)
admin.site.register(Ajuda)
admin.site.register(Materia)
admin.site.register(Subtopico)