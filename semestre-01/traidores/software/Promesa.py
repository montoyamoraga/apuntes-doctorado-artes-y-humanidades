class Promesa():
    def __init__(self, ventana):
        self.ventana = ventana
        self.nombre = "promesa"
        self.fechaPromesa = None
        self.personaEmite = ''
        self.personaRecibe = ''
        self.fechaRotura = None

    def getNombre(self):
        return self.nombre

    def getFechaPromesa(self):
        return self.fechaPromesa

    def getPersonaEmite(self):
        return self.personaEmite

    def getPersonaRecibe(self):
        return self.personaRecibe

    def getFechaRotura(self):
        return self.fechaRotura
