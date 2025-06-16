# importar modulos Python
import json


class Administrador():
    def __init__(self):
        self.name = "administrador"
        self.data = None
        # abrir el archivo JSON
        with open('data.json', 'r') as file:
            self.data = json.load(file)
