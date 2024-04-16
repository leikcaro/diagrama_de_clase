from encuesta import Encuesta

class EncuestaLimitadaPorRegion(Encuesta):
    def __init__(self, region:int, listado_region=regiones):
        self.__region= region


    def agregar_listado_respuestas(self, region, listado_region):
        if region in regiones:
            print("El listado de respuestas es:", listado_region)
        else:
            printt("Su region no es parte de las regiones habilitadas")    
            

if __name__ == "__main__":

	regiones = [
		1,5,9,11
	]