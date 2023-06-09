from main import app

from datetime import datetime, time

from main.utils import getWeekDay, getDateHour, getDateMinute


from main.classes.models.tabela import Tabela
from main.classes.models.tabel import Tabela2
from main.classes.models.interval import Interval

@app.route("/")
def hello_world():
    return {"success": "Hello World!"}

# @app.route("/valorPeriodo", methods=["POST"])
# def valor_periodo():
#     diaSemana = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#     diaFimSemana = ['Saturday', 'Sunday']
#     tabel = Tabela2(
#     valorIntervalo_1=Interval(2, time(hour=8,minute=0,second=0),time(hour=12,minute=0,second=0),diaSemana),
#     valorIntervalo_2=Interval(3, time(hour=12, minute=1, second=0), time(hour=18, minute=0, second=0),diaSemana),
#     valorIntervalo_3=Interval(2.5, time(hour=8,minute=0,second=0), time(hour=18, minute=0, second=0),diaFimSemana)
#     )
#     dataInicial=datetime(year=2023,month=6,day=9,hour=16, minute=0, second=0, microsecond=0)
#     # dataFinal=datetime(year=2023,month=6, day=10, hour=12, minute=3, second=0, microsecond=0)

#     return {"Comunicado":f"""O valor de tabela na {getWeekDay(date=dataInicial)} as {getDateHour(date=dataInicial)}:{getDateMinute(date=dataInicial)} custa R$ {tabel.valorTabela(data=dataInicial)} por hora."""}