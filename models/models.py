from pydantic import BaseModel
from typing import Union

class PagoIn (BaseModel):
    rules: list[str]
    schedules: list[str]
    routes: list[str]

class MicroserviceBuilderIn(BaseModel):
    pass

class PagoBuilderIn(MicroserviceBuilderIn):
    pago: PagoIn

class MicroserviceDirectorIn(BaseModel):
    """
    builder (MicroserviceBuilder): constructor object 'builder'
    """ 
    builder: Union[MicroserviceBuilderIn, None]
    pass

class DespachoIn(BaseModel):
    rules: list[str]
    schedules: list[str]
    routes: list[str]

class DespachoBuilder(MicroserviceBuilderIn):
    despacho: DespachoIn