from datetime import datetime, time
from main.utils import getWeekDay
from main.classes.models.interval import Interval

class Tabela:
    """
    Esta classe foi criada para conter e entregar as outras classes
    as informacoes a respeito da tabela de preco do estacionamento recebendo um ou
    mais intervalos (classe Interval) como parametro de entrada (metodo valorTabela).
    A variavel limitePeriodoXY delimitam os horarios do periodo do dia hora/minuto.
    """
    def __init__(self, **valorIntervalo:Interval):
        """
        valorIntervalo é um dicionário que contem todas as informações 
        dos intervalos, conforme o exemplo abaixo:

        {
            valorIntervalo_1: Interval(2, time(hour=8,minute=0,second=0),time(hour=12,minute=0,second=0),["Monday","Tuesday","Wednesday","Thursday","Friday"]),
            valorIntervalo_2: Interval(3, time(hour=12,minute=1,second=0),time(hour=18,minute=0,second=0),["Monday","Tuesday","Wednesday","Thursday","Friday"]),
            ...
            valorIntervalo_X: Interval(2.5, time(hour=8,minute=0,second=0),time(hour=18,minute=0,second=0),["Saturday", "Sunday"])
        }

        Para mais informacoes sobre o objeto intervalo, ver a classe Interval
        """
        self.__valoresIntervalo=valorIntervalo

    def __adequaHoraMinuto(self, hora:int, minuto:int):
        """
        Metodo criado para adequar para o tipo time a hora e minuto de um dado 
        do tipo datetime. Para comparacao do intervalo de hora
        """
        return time(hour=hora, minute=minuto,second=0)

    def __estaDentroIntervaloHora(self, hourTarget: time, hourLimit1:time, hourLimit2:time):
        """
        Metodo criado para verificar se um dado do tipo time esta dentro de um intervalo 
        de hora.
        """
        return True if hourLimit1 <= hourTarget <= hourLimit2 else False
    
    #metodo para verificar se uma string esta dentro de uma lista e retornar true ou false
    def __estaDentroIntervaloSemanal(self, weekDay: str, weekList: list):
        """
        Metodo criado para verificar se o dia da semana esta dentro do intervalo 
        de dias da semana (lista de strings, weekList)
        """
        return True if weekDay in weekList else False
    
    def __estaDentroIntervalo(self, dataAlvo: datetime, dataLimite1: time, dataLimite2: time, weekInterval: list):
        """
        Metodo criado para verificar se uma data hora esta dentro de um 
        intervalo de data e hora
        """
        dentroIntervaloHora = self.__estaDentroIntervaloHora(
            hourTarget=self.__adequaHoraMinuto(hora=dataAlvo.hour, minuto=dataAlvo.minute),
            hourLimit1=self.__adequaHoraMinuto(hora=dataLimite1.hour, minuto=dataLimite1.minute), 
            hourLimit2=self.__adequaHoraMinuto(hora=dataLimite2.hour, minuto=dataLimite2.minute)
        )
        dentroIntervaloSemana = self.__estaDentroIntervaloSemanal(weekDay=getWeekDay(dataAlvo), weekList=weekInterval)
        return True if dentroIntervaloHora and dentroIntervaloSemana else False
    
    def __enquadraIntervalos(self, intervals:dict, data:datetime):
        """
        Esse metodo vai iterar entre todos os valores de intervalos recebidos na classe 
        e retornar uma lista de tuplas que possue o valor do custo daquele intervalo e 
        um valor logico se o perido recebido esta naquele intervalo ou nao
        """
        valorIntervalo=[]
        for k,v in intervals.items():
            intervalo:Interval = v
            if self.__estaDentroIntervalo(
                dataAlvo=data,
                dataLimite1=intervalo.limiteInferiorHora,
                dataLimite2=intervalo.limiteSuperiorHora,
                weekInterval=intervalo.diasSemana):
                valorIntervalo.append((intervalo.custo,True))
            else:
                valorIntervalo.append((intervalo.custo,False))
        return valorIntervalo
        
    def __retornaValor(self,intervalos:list):
        """
        Metodo criado para retornar o valor estipulado de acordo com o intervalo 
        recebido.

        Os respectivos intervalos pedidos no desafio sao:

        intervalo1: Segunda a Sexta e 8:00 às 12:00
        intervalo2: Segunda a Sexta e 12:01 às 18:00
        intervalo3: Sabado a Domingo e 8:00 às 18:00
        """
        for intervalo in intervalos:
            if intervalo[1] == True:
                return intervalo[0]

    def valorTabela(self, data: datetime):
        """
        Metodo principal, entrega o valor da hora pre estabelecido na classe
        """
        intervals = self.__enquadraIntervalos(intervals=self.__valoresIntervalo, data=data)
        return self.__retornaValor(intervalos=intervals)