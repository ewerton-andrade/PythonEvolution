class Saida:
    """
    Classe criada para lidar com a informacao de data e horario de saida
    """
    def __init__(self, dataHoraSaida):
        self.__dataHoraSaida = dataHoraSaida

    @property
    def __pegaSaida(self):
        return self.__dataHoraSaida
    
    