from django.http import Http404
from django.forms import ModelForm
from django.http import HttpResponse
from rest_framework import generics
from tasabido.serializers import UsuarioSerializer
from .models import Usuario, Duvida, Ajuda

# Create your views here.
def index(requests):
	return HttpResponse("Bem vindo maxo!")

def criar_usuario(request):
	if request.method == 'POST':
		serializer = UsuarioSerializer(data=request.DATA)
          serializer.save()
         

def usuarios(request):
	usuarios = UsuarioSerializer(Usuario.objects.all(), many=True).data
	# usuarios = Usuario.objects.all()
	# return render(request, 'tasabido/detail.html', {'usuarios': usuarios})
	return Response({
        'usuarios': usuarios,
    })


def duvidas(request):
	duvidas = Duvidas.objects.all()
	return render(request, 'tasabido/duvidas.html', {'duvidas': duvidas})

class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)