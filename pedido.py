from datetime import datetime
from cliente import Empresa, ClienteParticular
from maquina import Maquina

class Pedido:
    def __init__(self, cliente, maquina, fechaRecibido=None, fechaEntregado=None, estado="Pendiente"):
        self._cliente = cliente
        self._maquina = maquina
        self._fechaRecibido = fechaRecibido or datetime.now()
        self._fechaEntregado = fechaEntregado
        self._estado = estado

    @property
    def cliente(self):
        return self._cliente
    
    @cliente.setter
    def cliente(self, value):
        self._cliente = value
        
    @property
    def maquina(self):
        return self._maquina
    
    @maquina.setter
    def maquina(self, value):
        self._maquina = value
        
    @property
    def fechaRecibido(self):
        return self._fechaRecibido
    
    @fechaRecibido.setter
    def fechaRecibido(self, value):
        self._fechaRecibido = value
        
    @property
    def fechaEntregado(self):
        return self._fechaEntregado
    
    @fechaEntregado.setter
    def fechaEntregado(self, value):
        self._fechaEntregado = value
        
    @property
    def estado(self):
        return self._estado
    
    @estado.setter
    def estado(self, value):
        self._estado = value

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