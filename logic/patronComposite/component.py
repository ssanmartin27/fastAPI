from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Component(ABC):
    @property
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def listComponents(self):
        pass

    @abstractmethod
    def operation(self):
        pass
