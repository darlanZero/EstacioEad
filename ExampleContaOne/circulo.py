class circulo ():
    _total_circulos = 0
    def __init__(self, Px, Py, Raio):
        self.Px = Px
        self.Py = Py
        self.Raio = Raio
        self._total_circulos += 1

    @classmethod
    def get total_circulos(cls):
        return cls._total_circulos
