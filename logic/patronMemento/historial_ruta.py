class HistorialRuta:
    def __init__(self):
        self.historial = []

    def agregarMemento(self, memento):
        self.historial.append(memento)

    def deshacer(self):
        if self.historial:
            return self.historial.pop()
        else:
            return None