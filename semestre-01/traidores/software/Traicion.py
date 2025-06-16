# importar modulos
from Promesa import Promesa


class Traicion():
    # variable de clase para contar cuantas traiciones
    nTraiciones = 0

    # constructor
    def __init__(self):
        # nombre de la traicion
        self.name = "traicion"

        # sumar 1 al contador
        Traicion.nTraiciones = Traicion.nTraiciones + 1

    # finalizer
    def __del__(self):
        # restar 1 al contador
        Traicion.nTraiciones = Traicion.nTraiciones - 1

    # definir promesa
    def setPromesa(self):
        self.promesa = Promesa()
