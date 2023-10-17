from .vehicle_Builder import VehicleBuilder
from .paratransit_concrete_builder import Paratransit

class ParatransitBuilder(VehicleBuilder):
    """ Clase para contruir un paratransito """

    def __init__ (self) -> None:
        self.reset()

    def reset (self):
        self._paratransit = Paratransit()
    
    def setCapacity(self, capaciy = 321) -> None:
        self._paratransit.capacity = capaciy 
    
    def setFuel(self, fuel = 123) -> None:
        self._paratransit.fuel = fuel

    @property
    def getVehicle (self):
        paratransit = self._paratransit
        self.reset()
        return paratransit