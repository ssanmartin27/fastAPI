from logic.patronBuilder.microservice.microservice_Builder import MicroserviceBuilder
from typing import Union

class MicroserviceDirector:
    def __init__(self) -> None:
        self._builder: Union[MicroserviceBuilder, None] = None

    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder (self, builder: MicroserviceBuilder) -> None:
        self._builder = builder

    def makeMicroservice(self, rule:str = 'rule', schedules: str = 'schedules', routes: str = 'routes') -> None:
        self.builder.configRules(rule)
        self.builder.configSchedules(schedules)
        self.builder.configRoutes(routes)

        