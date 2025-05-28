from datetime import datetime
from maquina import Maquina
from reposicion import Reposicion
from pieza import Pieza
from cliente import Cliente
from pedido import Pedido


class Sistema:
    def __init__(self):
        self.maquinas = []
        self.piezas = []
        self.clientes = []
        self.pedidos = []
        self.reposiciones = []

        self.codigo_pieza = 1
        self.codigo_maquina = 1
        self.codigo_cliente = 1

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_pieza(self, pieza):
        self.piezas.append(pieza)

    def agregar_maquina(self, maquina):
        self.maquinas.append(maquina)

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)

    def agregar_reposicion(self, reposicion):
        self.reposiciones.append(reposicion)
        # actualizar stock
        reposicion.pieza.cantidadPieza += reposicion.cantidad 
        

    def buscar_pieza_por_codigo(self, codigo):
        for pieza in self.piezas:
            if pieza.codigo == codigo:
                return pieza
        return None

    def buscar_maquina_por_codigo(self, codigo):
        for maquina in self.maquinas:
            if maquina.codigo == codigo:
                return maquina
        return None

    def buscar_cliente_por_id(self, id):
        for cliente in self.clientes:
            if cliente.id == id:
                return cliente
        return None

    def actualizar_stock_por_pedido(self, pedido):
        if pedido.estado == "Entregado":
            for i, pieza in enumerate(pedido.maquina.piezas_requeridas):
                cantidad = pedido.maquina.cantidades[i]
                pieza.cantidadPieza -= cantidad

    def procesar_pedidos_pendientes(self,pedido):
        for pedido in self.pedidos:
            if pedido.estado == "Pendiente":
                if pedido.maquina.disponibilidad():
                    pedido.estado = "Entregado"
                    pedido.fechaEntregado = datetime.now()
                    self.actualizar_stock_por_pedido(pedido)
                    print(f"Pedido de cliente {pedido.cliente.id} entregado tras reposición.")
    
    def procesar_todos_los_pedidos(self):
        for x in range(0,len(self.pedidos)):
            self.procesar_pedidos_pendientes(self.pedidos[x])
    
    def listar_faltantes_pedidos_pendientes(self):
        print("Verificando piezas faltantes para pedidos pendientes:")
        print("--------------")
        for pedido in self.pedidos:
            if pedido.estado == "Pendiente":
                # Si pedido.maquina es un objeto:
                maquina = pedido.maquina

                # Si no es un objeto, buscarlo por código o descripción:
                if isinstance(maquina, str) or isinstance(maquina, int):
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
                    else:
                        print(f"Pedido del cliente ID {pedido.cliente.id}: No faltan piezas para la máquina '{maquina.descripcion}'")
                else:
                    print(f"No se encontró la máquina para el pedido del cliente ID {pedido.cliente.id}")
    
    def obtener_maquina_objeto(self, codigo_o_desc):
        for maquina in self.maquinas:
            if str(maquina.codigo) == str(codigo_o_desc) or maquina.descripcion.lower() == str(codigo_o_desc).lower():
                return maquina
        return None
