from __future__ import annotations
from typing import Any

class Despacho():
    def __init__ (self) -> None:
        self.rules = []
        self.schedules = []
        self.routes = []

    def addRule(self, rule: Any) -> None:
        self.rules.append(rule)
    
    def addSchedule(self, schedule: Any) -> None:
        self.schedules.append(schedule)

    def addRoutes(self, route: Any) -> None:
        self.routes.append(route)

    def list_parts(self) -> None:
        print (f"Microservicio con reglas: {self.rules}, horarios: {self.schedules}, rutas: {self.routes}")

    def __str__(self):
        """Devuelve una representación del microservicio."""
        return f"Microservicio con reglas: {self.rules}, horarios: {self.schedules}, rutas: {self.routes}"
