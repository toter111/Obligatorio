from pieza import Pieza

class Reposicion:
    def __init__(self, pieza, cantidad, fecha):
        self.pieza = pieza
        self.cantidad = cantidad
        self.fecha = fecha

    def costo(self):
        return self.cantidad * Pieza.costo_unitario

    def __str__(self):
        return f"Reposición: Pieza {self.pieza.descripcion}, Lotes: {self.cantidad}, Fecha: {self.fecha}, Costo: ${self.costo():.2f}"
