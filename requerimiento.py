from pieza import Pieza

class Reposicion:
    def __init__(self, pieza, cantidad, fecha):
        self.__pieza = pieza
        self.__cantidad = cantidad
        self.__fecha = fecha

    @property
    def pieza(self):
        return self.__pieza
    
    @pieza.setter
    def pieza(self, value):
        if not isinstance(value, Pieza):
            raise ValueError("Debe proporcionar un objeto Pieza válido")
        self.__pieza = value
        
    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("La cantidad debe ser un entero positivo")
        self.__cantidad = value
        
    @property
    def fecha(self):
        return self.__fecha
    
    @fecha.setter
    def fecha(self, value):
        self.__fecha = value

    def costo(self):
        return self.__cantidad * self.__pieza.costo_unitario()

    def __str__(self):
        return f"Reposición: Pieza {self.__pieza.descPieza}, Cantidad: {self.__cantidad}, Fecha: {self.__fecha}, Costo: ${self.costo():.2f}"