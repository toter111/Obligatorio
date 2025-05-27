from entities.pieza import Pieza
from sistema import Sistema

class Maquina:
    def __init__(self, codigo, descripcion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.piezas_requeridas = []  # lista de objetos Pieza
        self.cantidades = []  # cantidades necesarias por pieza

    def agregar_requerimiento(self, pieza, cantidad):
        self.piezas_requeridas.append(pieza)
        self.cantidades.append(cantidad)

    def disponibilidad(self):
        for i, pieza in enumerate(self.piezas_requeridas):
            if pieza.cantidadPieza < self.cantidades[i]:
                return False
        return True

    def costo_produccion(self):
        total = 0
        for i, Pieza in enumerate(self.piezas_requeridas):
            total += Pieza.costoPieza * self.cantidades[i]
        return total
    def disponibilidad(self):
        cantidad_posible = []
        for i, pieza in enumerate(self.piezas_requeridas):
            if pieza.cantidadPieza < self.cantidades[i]:
                return 0
            else :
                cantidad_posible.append(pieza.cantidadPieza // self.cantidades[i])
            for i in range(len(cantidad_posible)):
                if cantidad_posible[i]>cantidad_posible[i+1]:
                    disponiblidad = cantidad_posible[i+1]
        return disponiblidad

    def __str__(self):
        return f"Código: {self.codigo}, Desc: {self.descripcion}, Costo Producción: ${self.costo_produccion():.2f}"
    
    def mostrar_maquinas(self):
        for maquina in Sistema.maquinas:
            return f"Código: {self.codigo}, Desc: {self.descripcion}, Costo Producción: ${self.costo_produccion():.2f}, Precio: {(self.costo_produccion)*1.5}"
        
