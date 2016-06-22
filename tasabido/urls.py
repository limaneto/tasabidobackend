from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from tasabido import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^listar_usuarios/', views.UsuariosModelViewSet.as_view({'get': 'list'})),
    url(r'^listar_duvidas/', views.DuvidaModelViewSet.as_view({'get':'list'})),
    url(r'^listar_materias/', views.MateriasModelViewSet.as_view({'get':'list'})),
    url(r'^listar_subtopicos/', views.SubtopicosModelViewSet.as_view({'get':'list'})),
    url(r'^listar_monitorias/', views.MonitoriaModelViewSet.as_view({'get':'list'})),
    url(r'^listar_moedas/', views.MoedaListView.as_view({'get':'list'})),
    url(r'^cadastrar_usuario/', views.cadastrar_usuario),
    url(r'^cadastrar_duvida/', views.cadastrar_duvida),
    url(r'^cadastrar_materia/', views.cadastrar_materia),
    url(r'^cadastrar_subtopico/', views.cadastrar_subtopico),
    url(r'^autenticar_usuario/', views.autenticar_usuario),
    url(r'^cadastrar_monitoria/', views.cadastrar_monitoria),
    url(r'^atualizar_duvida/', views.atualizar_duvida),
    url(r'^pagamento/', views.pagamento)
]

urlpatterns = format_suffix_patterns(urlpatterns)