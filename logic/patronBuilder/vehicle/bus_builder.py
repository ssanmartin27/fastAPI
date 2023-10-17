from .vehicle_Builder import VehicleBuilder
from .bus_concrete_builder import Bus

class BusBuilder (VehicleBuilder):
    """Clase para construir un Bus"""

    def __init__ (self) -> None:
        self.reset()

    def reset (self):
        self._bus = Bus()
    
    def setCapacity(self, capacity = 123) -> None:
        self._bus.capacity = capacity

    def setFuel(self, fuel = 2322) -> None:
        self._bus.fuel = fuel

    @property
    def getVehicle(self):
        bus = self._bus
        self.reset()
        return bus
    
