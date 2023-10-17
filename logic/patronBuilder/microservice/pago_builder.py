from logic.patronBuilder.microservice.microservice_Builder import MicroserviceBuilder
from logic.patronBuilder.microservice.pago_concrete_builder import Pago

class PagoBuilder (MicroserviceBuilder):
    """Clase para construir un Pago"""

    def __init__ (self) -> None:
        """Constructor de la clase"""
        self.reset()
    
    def reset(self):
        """Reseta el Pago"""
        self._Pago = Pago([],[],[])

    def configRules(self, rule = 'Rule') -> None:
        self._Pago.addRule(rule)

    def configSchedules(self, schedule = 'Schedules') -> None:
        self._Pago.addSchedule(schedule)

    def configRoutes(self, route = 'routes') -> None:
        self._Pago.addRoutes(route)

    def getMicroservice(self) -> Pago:
        """Obtiene el microservicio del Pago"""
        Pago = self._Pago
        self.reset()
        return Pago