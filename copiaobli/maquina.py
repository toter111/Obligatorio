from pieza import Pieza

class Maquina:
    def __init__(self, codigo, descripcion):
        self.__codigo = codigo
        self.__descripcion = descripcion
        self.__piezas_requeridas = []  # lista de objetos Pieza
        self.__cantidades = []  # cantidades necesarias por pieza

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, nuevo_codigo):
        self.__codigo = nuevo_codigo

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, nueva_descripcion):
        self.__descripcion = nueva_descripcion

    @property
    def piezas_requeridas(self):
        return self.__piezas_requeridas

    @property
    def cantidades(self):
        return self.__cantidades

    def agregar_requerimiento(self, pieza, cantidad):
        self.__piezas_requeridas.append(pieza)
        self.__cantidades.append(cantidad)

    def disponibilidad(self):
        for i, pieza in enumerate(self.__piezas_requeridas):
            if pieza.cantidadPieza < self.__cantidades[i]:
                return False
        return True

    def costo_produccion(self):
        total = 0
        for i, pieza in enumerate(self.__piezas_requeridas):
            total += pieza.costoPieza * self.__cantidades[i]
        return total

    def __str__(self):
        return f"Código: {self.codigo}, Desc: {self.descripcion}, Costo Producción: ${self.costo_produccion():.2f}"
