from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from tasabido import views

# router = routers.DefaultRouter()
# router.register(r'criar_usuario', views.UsuarioViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^usuarios/$', views.usuarios, name='usuarios'),
    url(r'^duvidas/$', views.duvidas, name='duvidas'),
    url(r'^usuarios_lista/$', views.UsuarioList.as_view()),
    url(r'^usuario_detalhe/(?P<pk>[0-9]+)/$', views.UsuarioDetail.as_view()),
    url(r'^criar_usuario/$', views.criar_usuario),
]

urlpatterns = format_suffix_patterns(urlpatterns)