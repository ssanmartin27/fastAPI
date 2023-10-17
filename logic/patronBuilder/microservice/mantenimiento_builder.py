from logic.patronBuilder.microservice.microservice_Builder import MicroserviceBuilder
from logic.patronBuilder.microservice.mantenimiento_concrete_builder import Mantenimiento

class MantenimientoBuilder(MicroserviceBuilder):
    """Clase para construir un MantenimientoPago """

    def __init__ (self) -> None:
        """Constructor de la clase"""
        self.reset()
    
    def reset(self):
        """Reseta el mantenimiento"""
        self._mantenimiento = Mantenimiento()

    def configRules(self, rule = 'Rule') -> None:
        self._mantenimiento.addRule(rule)

    def configSchedules(self, schedule = 'Schedules') -> None:
        self._mantenimiento.addSchedule(schedule)

    def configRoutes(self, route = 'routes') -> None:
        self._mantenimiento.addRoutes(route)

    @property
    def getMicroservice(self) -> Mantenimiento:
        """Obtiene el microservicio del mantenimiento"""
        mantenimiento = self._mantenimiento
        self.reset()
        return mantenimiento