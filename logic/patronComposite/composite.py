from .component import Component

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def listComponents(self):
        for child in self.children:
            child.listComponents()
    
    def operation(self):
        pass

    def update(self, new_data):
        print(f"Updating composite with new data: {new_data}")
        for child in self.children:
            child.update(new_data)

    def getChild(self):
        pass