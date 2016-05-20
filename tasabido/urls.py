from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from tasabido import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^listar_usuarios/', views.UsuariosList.as_view()),
    url(r'^listar_duvidas/', views.DuvidasList.as_view()),
    url(r'^listar_ajudas/', views.AjudasList.as_view()),
    url(r'^listar_materias/', views.MateriasList.as_view()),
    url(r'^listar_subtopicos/', views.SubtopicosList.as_view()),
    url(r'^cadastrar_usuario/', views.cadastrar_usuario),
    url(r'^cadastrar_duvida/', views.cadastrar_duvida),
    url(r'^cadastrar_ajuda/', views.cadastrar_ajuda),
    url(r'^cadastrar_materia/', views.cadastrar_materia),
    url(r'^cadastrar_subtopico/', views.cadastrar_subtopico),
    url(r'^autenticar_usuario/', views.autenticar_usuario),
]

urlpatterns = format_suffix_patterns(urlpatterns)