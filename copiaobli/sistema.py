from datetime import datetime
from maquina import Maquina
from reposicion import Reposicion
from pieza import Pieza
from cliente import Cliente
from pedido import Pedido


class Sistema:
    def __init__(self):
        self.__maquinas = []
        self.__piezas = []
        self.__clientes = []
        self.__pedidos = []
        self.__reposiciones = []

        self.__codigo_pieza = 1
        self.__codigo_maquina = 1
        self.__codigo_cliente = 1

    # Getters y Setters para listas

    @property
    def maquinas(self):
        return self.__maquinas

    @property
    def piezas(self):
        return self.__piezas

    @property
    def clientes(self):
        return self.__clientes

    @property
    def pedidos(self):
        return self.__pedidos

    @property
    def reposiciones(self):
        return self.__reposiciones

    # Getters y Setters para códigos

    def get_codigo_pieza(self):
        return self.__codigo_pieza

    def set_codigo_pieza(self, valor):
        self.__codigo_pieza = valor

    def get_codigo_maquina(self):
        return self.__codigo_maquina

    def set_codigo_maquina(self, valor):
        self.__codigo_maquina = valor

    def get_codigo_cliente(self):
        return self.__codigo_cliente

    def set_codigo_cliente(self, valor):
        self.__codigo_cliente = valor

    # Métodos de agregado

    def agregar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def agregar_pieza(self, pieza):
        self.__piezas.append(pieza)

    def agregar_maquina(self, maquina):
        self.__maquinas.append(maquina)

    def agregar_pedido(self, pedido):
        self.__pedidos.append(pedido)

    def agregar_reposicion(self, reposicion):
        self.__reposiciones.append(reposicion)
        reposicion.pieza.cantidadPieza += reposicion.cantidad

    # Búsqueda

    def buscar_pieza_por_codigo(self, codigo):
        for pieza in self.__piezas:
            if pieza.codigo == codigo:
                return pieza
        return None

    def buscar_maquina_por_codigo(self, codigo):
        for maquina in self.__maquinas:
            if maquina.codigo == codigo:
                return maquina
        return None

    def buscar_cliente_por_id(self, id):
        for cliente in self.__clientes:
            if cliente.id == id:
                return cliente
        return None

    def actualizar_stock_por_pedido(self, pedido):
        if pedido.estado == "Entregado":
            for i, pieza in enumerate(pedido.maquina.piezas_requeridas):
                cantidad = pedido.maquina.cantidades[i]
                pieza.cantidadPieza -= cantidad

    def procesar_pedidos_pendientes(self, pedido):
        for pedido in self.__pedidos:
            if pedido.estado == "Pendiente":
                if pedido.maquina.disponibilidad():
                    pedido.estado = "Entregado"
                    pedido.fechaEntregado = datetime.now()
                    self.actualizar_stock_por_pedido(pedido)
                    print(f"Pedido de cliente {pedido.cliente.id} entregado tras reposición.")

    def procesar_todos_los_pedidos(self):
        for pedido in self.__pedidos:
            self.procesar_pedidos_pendientes(pedido)

    def listar_faltantes_pedidos_pendientes(self):
        print("Verificando piezas faltantes para pedidos pendientes:")
        print("--------------")
        envio = False
        for pedido in self.__pedidos:
            if pedido.estado == "Pendiente":
                maquina = pedido.maquina

                if isinstance(maquina, (str, int)):
                    maquina = self.obtener_maquina_objeto(maquina)

                if maquina:
                    faltantes = []
                    for i, pieza in enumerate(maquina.piezas_requeridas):
                        cantidad_disponible = pieza.cantidadPieza
                        cantidad_necesaria = maquina.cantidades[i]
                        if cantidad_disponible < cantidad_necesaria:
                            faltan = cantidad_necesaria - cantidad_disponible
                            mensaje = (
                                f"Pedido del cliente ID {pedido.cliente.id}: "
                                f"Faltan {faltan} unidades de la pieza '{pieza.descPieza}' "
                                f"para la máquina '{maquina.descripcion}' (Código {maquina.codigo})"
                            )
                            faltantes.append(mensaje)

                    if faltantes:
                        for msg in faltantes:
                            print(msg)
                        envio = True
        if not envio:
            print("No faltan piezas para los pedidos pendientes.")

    def obtener_maquina_objeto(self, codigo_o_desc):
        for maquina in self.__maquinas:
            if str(maquina.codigo) == str(codigo_o_desc) or maquina.descripcion.lower() == str(codigo_o_desc).lower():
                return maquina
        return None
