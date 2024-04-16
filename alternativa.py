class Alternativa():
    def __init__(self, contenido, ayuda=''):
        __contenido = contenido
        __ayuda = ayuda
    @property
    def mostrar_alternativa(self, contenido, ayuda):
        print( 'El contenido es: ',contenido,', y la ayuda es:', ayuda)
        
if __name__ == "__main__":

    dicc = {
    "contenido": "contenidos1",
    "ayuda": "ayudita1"
    }
        
alternativa = Alternativa(dicc["contenido"],dicc["ayuda"])