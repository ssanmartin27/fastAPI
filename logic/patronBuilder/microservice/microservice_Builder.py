from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class MicroserviceBuilder(ABC):    
    @property
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def configRules(self) -> None:
        pass
    
    @abstractmethod
    def configSchedules(self) -> None:
        pass
    
    @abstractmethod
    def configRoutes(self) -> None:
        pass

