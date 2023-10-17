
class Paratransit:
    """Concrete Builder para el vehiculo ParaTransito"""

    def __init__(self) -> None:
        self.capacity = 0
        self.fuel = 0
    
    def listComponents(self) -> None:
        print(f'Los componentes del Paratransito: Capacidad: {self.capacity}, Fuel: {self.fuel}')
