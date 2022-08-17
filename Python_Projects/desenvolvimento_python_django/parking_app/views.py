from django.shortcuts import get_object_or_404, render
from .models import Carro

# Create your views here.
def index(request):
    placas = Carro.objects.all()

    dados = {
        'placas': placas
    }
    return render(request,'index.html', dados) #Funcao comando para mostrar na aplicacao criada com conteudo html para formatacao da pagina escrito no arquivo index.html na pasta templates dentro da aplicacao parking_app

def carro(request, carro_id):
    carro = get_object_or_404(Carro, pk= carro_id)
    placa_a_exibir = {
        'carro': carro
    }
    return render(request, 'carro.html', placa_a_exibir)