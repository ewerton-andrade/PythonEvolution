from datetime import datetime
from main.classes.models.veiculo import Veiculo

class Entrada:
    """
    Classe criada para lidar com a informacao de registro de entrada:
    - data e hora de entrada
    - modelo do automovel

    """
    def __init__(self, veiculo: Veiculo):
        self.__dataHoraEntrada = datetime.now()
        self.__veiculo = veiculo
        self.__placaVeiculo = self.__retornaPlacaVeiculo()
        self.__modeloVeiculo = self.__retornaModeloVeiculo()
        self.__corVeiculo = self.__retornaCorVeiculo()

    
    @property
    def dataHoraEntrada(self):
        return self.__dataHoraEntrada
    
    @property
    def placaVeiculo(self):
        return self.__placaVeiculo
    
    @property
    def modeloVeiculo(self):
        return self.__modeloVeiculo
    
    @property
    def corVeiculo(self):
        return self.__corVeiculo
    
    def __retornaPlacaVeiculo(self):
        return self.__veiculo.placa
    
    def __retornaModeloVeiculo(self):
        return self.__veiculo.modelo
    
    def __retornaCorVeiculo(self):
        return self.__veiculo.cor
    

    
    
    
    #A-Posso criar metodos para separar o valor de data e hora
    #B- Metodos para retornar apenas o valor da data e/ou apenas 
    # o valor da hora
