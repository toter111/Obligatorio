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

    # Getters y setters

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, nuevo_cliente):
        self.__cliente = nuevo_cliente

    @property
    def maquina(self):
        return self.__maquina

    @maquina.setter
    def maquina(self, nueva_maquina):
        self.__maquina = nueva_maquina

    @property
    def fechaRecibido(self):
        return self.__fechaRecibido

    @fechaRecibido.setter
    def fechaRecibido(self, nueva_fecha):
        self.__fechaRecibido = nueva_fecha

    @property
    def fechaEntregado(self):
        return self.__fechaEntregado

    @fechaEntregado.setter
    def fechaEntregado(self, nueva_fecha):
        self.__fechaEntregado = nueva_fecha

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    # Métodos

    def precio(self):
        precio_base = self.__maquina.costo_produccion() * 1.5
        if self.__cliente.es_empresa:
            precio_base *= 0.8
        return precio_base

    def mostrar_pedido(self):
        fecha_entrega_str = self.__fechaEntregado.strftime("%Y-%m-%d %H:%M:%S") if self.__fechaEntregado else "Pendiente"
        print(f"Cliente: {self.__cliente.id}, Máquina: {self.__maquina.descripcion}, Estado: {self.__estado}, Precio: ${self.precio():.2f}, Fecha recibido: {self.__fechaRecibido.strftime('%Y-%m-%d %H:%M:%S')}, Fecha entrega: {fecha_entrega_str}")

    @property
    def faltantes(self):
        pass
