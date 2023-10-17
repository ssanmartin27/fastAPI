class Train:
    """Concrete Builder para el vehiculo Tren"""

    def __init__(self) -> None:
        self.capacity = 0
        self.fuel = 0
    
    def listComponents(self) -> None:
        print(f'Los componentes del Tren: Capacidad: {self.capacity}, Fuel: {self.fuel}')
