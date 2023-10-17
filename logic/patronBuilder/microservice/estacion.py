

class Estacion:
    def __init__(self, _idEstacion, _ubicacion, _nombre, _estado=''):
        self.idEstacion = _idEstacion
        self.ubicacion = _ubicacion
        self.nombre = _nombre
        self.estado = _estado

    def setEstado(self, estado):
        self.estado = estado

    def setId(self, idEstacion):
        self.idEstacion = idEstacion

    def setUbicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getEstacion (self, estacion):
        for i in estacion: 
            print(i)

    def __str__(self):
        return f"ID: {self.idEstacion}, Ubicación: {self.ubicacion}, Nombre: {self.nombre}, Estado: {self.estado if self.estado else 'No especificado'}"
 
 

