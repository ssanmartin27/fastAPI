from __future__ import annotations
from abc import abstractmethod

class VehicleBuilder:
    """ Clase para construir un vehiculo"""
    @property
    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def setCapacity(self) -> None:
        pass
    
    @abstractmethod
    def setFuel (self) -> None:
        pass

