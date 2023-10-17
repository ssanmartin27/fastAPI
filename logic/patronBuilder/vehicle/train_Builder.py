from .vehicle_Builder import VehicleBuilder
from .train_concrete_builder import Train

class TrainBuilder(VehicleBuilder):
    """Clase para construir un tren"""
    
    def __init__(self) -> None:
        self.reset()
    
    def reset (self):
        self._train = Train()

    def setCapacity(self, capacity = 32) -> None:
        self._train.capacity = capacity

    def setFuel(self, fuel = 22) -> None:
        self._train.fuel = fuel

    @property
    def getVehicle (self): 
        train = self._train
        self.reset()
        return train