class Pieza:
    def __init__(self,descPieza,costoPieza,cantidadPieza): #agregar el lote
        self.codigo=0
        self.descPieza=descPieza
        self.costoPieza=costoPieza
        self.cantidadPieza=cantidadPieza
        
    def actualizar(self):
        pass

    def costo_unitario(self):
        return self.costoPieza*1.5
    
    def actualizar_pieza(self):
        pass

    def cantidad(self):
        return self.cantidadPieza