class ListaDeRespuesta:
    def __init__(self, correo:str, respuestas:list):
        self.__lista_respuestas = respuestas
        self.__correo = correo #como clave unica
