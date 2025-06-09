

from pieza import Pieza

class Reposicion:
    def __init__(self, pieza, cantidad, fecha):
        self.__pieza = pieza
        self.__cantidad = cantidad
        self.__fecha = fecha

    # Getters y setters

    @property
    def pieza(self):
        return self.__pieza

    @pieza.setter
    def pieza(self, nueva_pieza):
        self.__pieza = nueva_pieza

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, nueva_cant):
        self.__cantidad = nueva_cant

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, nueva_fecha):
        self.__fecha = nueva_fecha

    # Método

    def costo(self):
        return self.__cantidad * self.__pieza.costo_unitario()

    def __str__(self):
        return f"Reposición: Pieza {self.__pieza.descPieza}, Lotes: {self.__cantidad}, Fecha: {self.__fecha}, Costo: ${self.costo():.2f}"
