class MementoHorario:
    def __init__(self, idHorario, ruta, tiemposSalida):
        self.idHorario = idHorario
        self.ruta = ruta
        self.tiemposSalida = tiemposSalida.copy()

    def getEstado(self):
        return f"Horario: {self.idHorario}, Ruta: {self.ruta.getEstado()}, Tiempos de Salida: {self.tiemposSalida}"
