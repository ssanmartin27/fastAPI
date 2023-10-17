from logic.patronBuilder.microservice.microservice_Builder import MicroserviceBuilder
from logic.patronBuilder.microservice.despacho_concrete_builder import  Despacho

class DespachoBuilder(MicroserviceBuilder): 
    """Clase para construir un despacho"""
    
    def __init__ (self) -> None:
        """Constructor de la clase"""
        self.reset()
    
    def reset(self):
        """Reseta el despacho"""
        self._despacho = Despacho([],[],[])

    def configRules(self, rule='Rule') -> None:
        if not self._despacho:
            self.reset()
        self._despacho.addRule(rule)

    def configSchedules(self, schedule='Schedules') -> None:
        if not self._despacho:
            self.reset()
        self._despacho.addSchedule(schedule)

    def configRoutes(self, route='routes') -> None:
        if not self._despacho:
            self.reset()
        self._despacho.addRoutes(route)

    # @property
    def getMicroservice(self):
        """Obtiene el microservicio del despacho"""
        despacho = self._despacho
        self.reset()
        return despacho
    
if __name__ == '__main__':
    despacho = DespachoBuilder()
    despacho._despacho.list_parts()
    despacho.configRoutes('hola')
    despacho.configRules('hola')
    despacho.configSchedules('hola')
    despacho._despacho.list_parts()

    despacho.reset()
    despacho._despacho.list_parts()