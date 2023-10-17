from __future__ import annotations
from abc import abstractmethod


class VehicleDirector:
    def __init__(self) -> None:
        self._builder = None
    
    @property
    def builder (self):
        return self._builder
    
    @builder.setter
    def builder (self, builder) -> None:
        self._builder = builder

    def makeVehicle (self) -> None: 
        self.builder.setCapacity()
        self.builder.setFuel()


""" if __name__ == '__main__':    
    director = VehicleDirector()
    train_builder = TrainBuilder()
    director.builder = train_builder
    director.makeVehicle()
    train_builder.getVehicle.listComponents() """