from pregunta import Pregunta

class Encuesta:
    def __init__(self, nombre: str, listado_preguntas: list, listado_respuestas=None):
        self.nombre = nombre
        self.listado_preguntas = [
			Pregunta(dicc["enunciado"],dicc["ayuda"]) for dicc in listado_preguntas
		]
        if listado_respuestas is None:
            self.listado_respuestas = []
        else:
            self.listado_respuestas = listado_respuestas

    def mostrar_encuesta(self):
        print(f"Encuesta: {self.nombre}")
        print("Preguntas:")
        for pregunta in self.listado_preguntas:
            print(f"- {pregunta}")
        print("Respuestas:")
        if self.listado_respuestas:
            for respuesta in self.listado_respuestas:
                print(f"- {respuesta}")
        else:
            print("No hay respuestas aún.")
