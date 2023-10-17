from logic.patronMemento.memento_Ruta import MementoRuta
from logic.patronMemento.historial_ruta import HistorialRuta

class Ruta:
    def __init__(self):
        self.idRuta = ''
        self.longitud = 0  # Agregué el atributo longitud aquí
        self.origen = ''
        self.destino = ''
        self.descripcion = ''
        self.estacion = []
        self.historial = HistorialRuta()

    def setOrigen(self, origen):
        self.origen = origen

    def setDestino(self, destino):
        self.destino = destino

    def setIdRuta(self, idRuta):
        self.idRuta = idRuta

    def setDescripcion(self, descripcion):
        self.descripcion = descripcion

    def setLongitud(self, longitud): 
        self.longitud = longitud

    def setEstacion(self, estacion):
        self.estacion.append(estacion)

    def guardar(self):
        memento = MementoRuta(self.idRuta, self.longitud, self.origen, self.destino, self.descripcion, self.estacion)
        self.historial.agregarMemento(memento)

    def restaurar(self, memento):
        self.idRuta = memento.idRuta
        self.longitud = memento.longitud
        self.origen = memento.origen
        self.destino = memento.destino
        self.descripcion = memento.descripcion
        self.estacion = memento.estaciones.copy()
    
    def getEstado(self):
        return f"Ruta: {self.idRuta}, Longitud: {self.longitud}, Origen: {self.origen}, Destino: {self.destino}, Descripción: {[print(_) for _ in self.estacion]}"
