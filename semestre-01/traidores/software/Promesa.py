class Promesa():
    def __init__(self, nombre):
        self.nombre = nombre
        self.fechaPromesa = None
        self.personaEmite = ''
        self.personaRecibe = ''
        self.fechaRotura = None
        self.comentarios = ''

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

    def getComentarios(self):
        return self.comentarios

    def setNombre(self, nombre):
        self.nombre = nombre

    def setFechaPromesa(self, fecha):
        self.fechaPromesa = fecha

    def setPersonaEmite(self, persona):
        self.personaEmite = persona

    def setPersonaRecibe(self, persona):
        self.personaRecibe = persona

    def setFechaRotura(self, fecha):
        self.fechaRotura = fecha

    def setComentarios(self, comentarios):
        self.comentarios = comentarios
