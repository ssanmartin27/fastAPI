class MementoRuta:
    def __init__(self, idRuta, longitud, origen, destino, descripcion, estaciones):
        self.idRuta = idRuta
        self.longitud = longitud
        self.origen = origen
        self.destino = destino
        self.descripcion = descripcion
        self.estaciones = estaciones.copy()

    def getEstado(self):
        return f"Ruta: {self.idRuta}, Longitud: {self.longitud}, Origen: {self.origen}, Destino: {self.destino}, Descripción: {self.descripcion}, Estaciones: {self.estaciones}"
