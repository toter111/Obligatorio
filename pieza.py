class Pieza:
    def __init__(self, descPieza, costoPieza, cantidadPieza):
        self.__codigo = 0
        self.__descPieza = descPieza
        self.__costoPieza = costoPieza
        self.__cantidadPieza = cantidadPieza
        
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, value):
        self.__codigo = value
        
    @property
    def descPieza(self):
        return self.__descPieza
    
    @descPieza.setter
    def descPieza(self, value):
        self.__descPieza = value
        
    @property
    def costoPieza(self):
        return self.__costoPieza
    
    @costoPieza.setter
    def costoPieza(self, value):
        self.__costoPieza = value
        
    @property
    def cantidadPieza(self):
        return self.__cantidadPieza
    
    @cantidadPieza.setter
    def cantidadPieza(self, value):
        self.__cantidadPieza = value
    
    
    def costo_unitario(self):
        return self.costoPieza * 1.5

    def cantidad(self):
        return self.cantidadPieza