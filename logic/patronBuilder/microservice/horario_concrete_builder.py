from __future__ import annotations
from logic.patronMemento.historial_horario import HistorialHorario
from logic.patronMemento.memento_horario import MementoHorario
from logic.patronBuilder.microservice.ruta import Ruta
from typing import Any

class Horario:
    def __init__(self):
        self.idHorario = ''
        self.rules = []
        self.ruta = []
        self.Schedules = []  # Tiempo de salida
        self.historial = HistorialHorario()

    def addRules(self, rule: Any):
        self.rules.append(rule)

    def addRoutes(self, route: Ruta):
        self.ruta.append(route)

    def addSchedules(self, schedule: Any):
        self.Schedules.append(schedule)

    def setId(self, idHorario):
        self.idHorario = idHorario

    def guardar(self):
        memento = MementoHorario(self.idHorario, self.ruta[-1], self.Schedules)
        self.historial.agregarMemento(memento)

    def restaurar(self, memento):
        self.idHorario = memento.idHorario
        self.ruta = memento.ruta
        self.Schedules = memento.tiemposSalida.copy()
