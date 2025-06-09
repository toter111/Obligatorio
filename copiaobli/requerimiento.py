class Requerimiento:
    def __init__(self, maquina, pieza, cantidad):
        self.__maquina = maquina
        self.__pieza = pieza
        self.__cantidad = cantidad

    # Getters y setters

    @property
    def maquina(self):
        return self.__maquina

    @maquina.setter
    def maquina(self, nueva_maquina):
        self.__maquina = nueva_maquina

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
    def cantidad(self, nueva_cantidad):
        self.__cantidad = nueva_cantidad
