
from .component import Component

class Leaf(Component): 
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def listComponents(self):
        self.vehicle.listComponents()
    
    def update(self, value):
        self.vehicle = value

    def operation(self):
        print(f'Hola')

