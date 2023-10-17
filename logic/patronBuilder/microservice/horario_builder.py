from logic.patronBuilder.microservice.microservice_Builder import MicroserviceBuilder
from logic.patronBuilder.microservice.horario_concrete_builder import Horario
from logic.patronBuilder.microservice.ruta import Ruta

class HorarioBuilder(MicroserviceBuilder):
    """Clase para construir un horario"""
    
    def __init__ (self) -> None:
        """Constructor de la clase"""
        self.reset()
    
    def reset(self):
        """Reseta el horario"""
        self._horario = Horario()

    def configRules(self, rule = 'Rule') -> None:
        self._horario.addRules(rule)

    def configSchedules(self, schedule = 'Schedules') -> None:
        self._horario.addSchedules(schedule)

    def configRoutes(self, route: Ruta) -> None:
        self._horario.addRoutes(route)

    @property
    def getMicroservice(self) -> Horario:
        """Obtiene el microservicio del horario"""
        horario = self._horario
        self.reset()
        return horario