import calendar
from datetime import datetime, timedelta, time

#Uteis para trabalhar com data e hora

#Metodo para pegar o tempo atual em segundos
def getCurrentTime():
    return time.time()
#Obs: O tempo para o sistema unix conta a partir de Janeiro 1, 1970, 00:00:00

#Metodo para extrair a hora de qualquer data
def getDateHour(date:datetime):
    return date.hour

#Metodo para extrair os minutos de qualquer data
def getDateMinute(date:datetime):
    return date.minute

#Metodo para extrair os segundos de qualquer data
def getDateSecond(date:datetime):
    return date.second

#Metodo para extrair o dia da semana de qualquer data
def getWeekDay(date: datetime):
    return calendar.day_name[date.weekday()]

#Metodo para extrair o periodo da diferenca entre duas datas
def getPeriod(dataInicial: datetime, dataFinal: datetime):
    td = dataFinal - dataInicial
    return td

#Metodo para extrair um tipo de parametro de um periodo de tempo
def getXPeriod(date: timedelta, param: str):
    """
    days: para extrair o(s) dia(s) de um determinado periodo
    seconds: para extrair os segundos de um determinado periodo
    microseconds: para extrair microsegundos
    total_seconds: retorna o valor total do periodo em segundos
    """
    match param:
        case "days":
            return date.days
        case "seconds":
            return date.seconds
        case "microseconds":
            return date.microseconds
        case "total_seconds":
            return date.total_seconds()
        case _:
            print("====>>>> Check your param name")

#Retorna o dia de uma determinada data
def retornaDataDia(data: datetime) -> str:
    return data.strftime("%d")

def retornaDataMes(data: datetime) -> str:
    return data.strftime("%m")