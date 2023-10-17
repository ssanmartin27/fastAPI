class Bus:
    """Concrete Builder para el vehiculo bus"""
    def __init__ (self) -> None:
        self.capacity  = 0
        self.fuel = 0
    
    def listComponents(self) -> None:
        print(f'Los componentes del Bus: Capacidad: {self.capacity}, Fuel: {self.fuel}')
