from datetime import time

class Interval:
    """
        valorIntervalo é um dicionário de tupla(s) no qual deve conter as informações 
        dos intervalos, conforme o exemplo abaixo:
        
        valorIntervalo_X=(2, time(hour=8,minute=0,second=0),time(hour=12,minute=0,second=0),["Monday","Tuesday","Wednesday","Thursday","Friday"])

        -Na primeira posição da tupla deve estar o valor inteiro do custo (R$) do intervalo;
        -Na segunda posição da tupla deve estar o limite inferior do intervalo de tempo (classe time);
        -Na terceira posição da tupla deve estar o limite superior do intervalo de tempo (classe time);
        -Na quarta posição da tupla deve conter uma lista com os dias da semana em string 
        em que sao validos o intervalo;
        """
    def __init__(self, custo:int, limiteInferiorHora:time, limiteSuperiorHora:time, diasSemana:list):
        self.__custo = custo
        self.__limiteInferiorHora=limiteInferiorHora
        self.__limiteSuperiorHora=limiteSuperiorHora
        self.__diasSemana=diasSemana
    
    @property
    def custo(self):
        return self.__custo
    
    @property
    def limiteInferiorHora(self):
        return self.__limiteInferiorHora
    
    @property
    def limiteSuperiorHora(self):
        return self.__limiteSuperiorHora
    
    @property
    def diasSemana(self):
        return self.__diasSemana