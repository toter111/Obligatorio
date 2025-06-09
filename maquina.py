from pieza import Pieza

class Maquina:
    def __init__(self, codigo, descripcion):
        self._codigo = codigo
        self._descripcion = descripcion
        self._piezas_requeridas = []  # lista de objetos Pieza
        self._cantidades = []  # cantidades necesarias por pieza

    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, value):
        self._codigo = value
        
    @property
    def descripcion(self):
        return self._descripcion
    
    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value
        
    @property
    def piezas_requeridas(self):
        return self._piezas_requeridas
    
    @property
    def cantidades(self):
        return self._cantidades

    def agregar_requerimiento(self, pieza, cantidad):
        self._piezas_requeridas.append(pieza)
        self._cantidades.append(cantidad)

    def disponibilidad(self):
        for i, pieza in enumerate(self._piezas_requeridas):
            if pieza.cantidadPieza <= self._cantidades[i]:
                return False
        return True

    def costo_produccion(self):
        total = 0
        for i, pieza in enumerate(self._piezas_requeridas):
            total += pieza.costoPieza * self._cantidades[i]
        return total

    def __str__(self):
        return f"Código: {self.codigo}, Desc: {self.descripcion}, Costo Producción: ${self.costo_produccion():.2f}"