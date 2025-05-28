from datetime import datetime
from cliente import Empresa, ClienteParticular
from maquina import Maquina



class Pedido:
    def __init__(self, cliente, maquina, fechaRecibido=None, fechaEntregado=None, estado="Pendiente"):
        self.cliente = cliente
        self.maquina = maquina
        self.fechaRecibido = fechaRecibido or datetime.now()
        self.fechaEntregado = fechaEntregado
        self.estado = estado

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