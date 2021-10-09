
class Abuelito:
    def __init__(self):
        self.estomago = []

    def come(self, comida):
        self.estomago.append(comida)

    def vomita(self):
        if not self.estomago:
            raise IndexError('Nada que vomitar!')
        return self.estomago.pop()

    def esta_digiriendo(self):
        if len (self.estomago) > 0:
            return 'Silencio'
        return 'Gruñe'


