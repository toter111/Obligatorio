class Pieza:
    __contador_codigo = 1  # atributo de clase para generar códigos únicos

    def __init__(self, descPieza, costoPieza, cantidadPieza):
        self.__codigo = Pieza.__contador_codigo
        Pieza.__contador_codigo += 1  # incrementa para la próxima pieza
        self.__descPieza = descPieza
        self.__costoPieza = costoPieza
        self.__cantidadPieza = cantidadPieza
    # Getters y setters

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def set_codigo(self, codigo):
        self.__codigo = codigo

    @property
    def descPieza(self):
        return self.__descPieza

    @descPieza.setter
    def descPieza(self, nueva_desc):
        self.__descPieza = nueva_desc

    @property
    def costoPieza(self):
        return self.__costoPieza

    @costoPieza.setter
    def costoPieza(self, nuevo_costo):
        self.__costoPieza = nuevo_costo

    @property
    def cantidadPieza(self):
        return self.__cantidadPieza

    @cantidadPieza.setter
    def cantidadPieza(self, nueva_cant):
        self.__cantidadPieza = nueva_cant

    # Métodos

    def costo_unitario(self):
        return self.__costoPieza * 1.5

    def actualizar_pieza(self):
        pass

    def actualizar(self):
        pass
