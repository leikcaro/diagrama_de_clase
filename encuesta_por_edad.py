from encuesta import Encuesta

class EncuestaLimitadaPorEdad(Encuesta):
    def __init__(self, edad_min:int, edad_max:int):
        self.__edad_minima = edad_min
        self.__edad_maxima = edad_max


    def agregar_listado_respuestas(self, edad, edad_minima, edad_maxima, listado_respuestas):
        if edad <= edad_maxima and edad >= edad_minima:
            print("El listado de respuestas es:", listado_respuestas)