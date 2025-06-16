from datetime import datetime
from cliente import Empresa, ClienteParticular
from maquina import Maquina

class Pedido:
    def __init__(self, cliente, maquina, fechaRecibido=None, fechaEntregado=None, estado="Pendiente"):
        self.__cliente = cliente
        self.__maquina = maquina
        self.__fechaRecibido = fechaRecibido or datetime.now()
        self.__fechaEntregado = fechaEntregado
        self.__estado = estado

    @property
    def cliente(self):
        return self.__cliente
    
    @cliente.setter
    def cliente(self, value):
        self.__cliente = value
        
    @property
    def maquina(self):
        return self.__maquina
    
    @maquina.setter
    def maquina(self, value):
        self.__maquina = value
        
    @property
    def fechaRecibido(self):
        return self.__fechaRecibido
    
    @fechaRecibido.setter
    def fechaRecibido(self, value):
        self.__fechaRecibido = value
        
    @property
    def fechaEntregado(self):
        return self.__fechaEntregado
    
    @fechaEntregado.setter
    def fechaEntregado(self, value):
        self.__fechaEntregado = value
        
    @property
    def estado(self):
        return self.__estado
    
    @estado.setter
    def estado(self, value):
        self.__estado = value

    def precio(self):
        precio_base = self.maquina.costo_produccion() * 1.5
        if self.cliente.es_empresa:
            precio_base *= 0.8
        return precio_base

    @property
    def mostrarPedidos(self):
        fecha_entrega_str = self.fechaEntregado.strftime("%Y-%m-%d %H:%M:%S") if self.fechaEntregado else "Pendiente"
        return print(f"Cliente: {self.cliente.id}, Máquina: {self.maquina.descripcion}, Estado: {self.estado}, Precio: ${self.precio():.2f}, Fecha recibido: {self.fechaRecibido.strftime('%Y-%m-%d %H:%M:%S')}, Fecha entrega: {fecha_entrega_str}")

    @property
    def faltantes(self):
        pass

    def es_empresaP(self):
        if self.cliente.es_empresa:
            return True
        else:
            return False