from pieza import Pieza

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
        dis=False
        for i, pieza in enumerate(self.piezas_requeridas):
            if pieza.cantidadPieza < self.cantidades[i]:
                dis=True
        return dis
    
    
    def faltantes(self):
        mensajes = []
        for i, pieza in enumerate(self.piezas_requeridas):
            cantidad_disponible = pieza.cantidadPieza
            cantidad_necesaria = self.cantidades[i]
            if cantidad_disponible < cantidad_necesaria:
                faltan = cantidad_necesaria - cantidad_disponible
                mensajes.append(f"Faltan {faltan} unidades de la pieza '{pieza.descPieza}' para la máquina '{self.descripcion}' (Código {self.codigo})")
        return mensajes

    
  
        
      



    def costo_produccion(self):
        total = 0
        for i, Pieza in enumerate(self.piezas_requeridas):
            total += Pieza.costoPieza * self.cantidades[i]
        return total

    def __str__(self):
        return f"Código: {self.codigo}, Desc: {self.descripcion}, Costo Producción: ${self.costo_produccion():.2f}"
