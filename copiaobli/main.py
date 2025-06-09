from datetime import datetime

from cliente import ClienteParticular, Empresa
from pieza import Pieza
from maquina import Maquina
from pedido import Pedido
from reposicion import Reposicion
from sistema import Sistema

def main():
    sistema_fabrica = Sistema()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Registrar")
        print("2. Listar")
        print("3. Salir del Sistema")
        opcion = input("Ingrese opción: ")

        if opcion == "1":
            while True:
                print("\n-- Registrar --")
                print("1. Pieza")
                print("2. Máquina")
                print("3. Cliente")
                print("4. Pedido")
                print("5. Reposición")
                print("6. Salir")
                opc_reg = input("Ingrese opción: ")

                if opc_reg == "1":  # Pieza
                    desc = input("Descripción de la pieza: ")
                    costo = float(input("Costo de fabricación de la pieza: "))
                    cantidad = int(input("Cantidad en stock: "))

                    p = Pieza(desc, costo, cantidad)
                    p.set_codigo(sistema_fabrica.codigo_pieza)
                    sistema_fabrica.codigo_pieza += 1

                    sistema_fabrica.set_codigo_pieza(sistema_fabrica.get_codigo_pieza() + 1)
                    sistema_fabrica.agregar_pieza(p)
                    print(f"Pieza '{desc}' agregada con código {p.get_codigo()}.")

                elif opc_reg == "2":  # Máquina
                    codigo = sistema_fabrica.get_codigo_maquina()
                    descripcion = input("Descripción de la máquina: ")
                    m = Maquina(codigo, descripcion)
                    sistema_fabrica.set_codigo_maquina(codigo + 1)

                    while True:
                        agregar_req = input("¿Agregar pieza requerida? (s/n): ").lower()
                        if agregar_req != "s":
                            break
                        print("Piezas disponibles:")
                        for p in sistema_fabrica.piezas:
                            print(f"{p.get_codigo()} - {p.get_desc_pieza()} (Stock: {p.get_cantidad_pieza()})")
                        cod_pieza = int(input("Ingrese código de la pieza: "))
                        pieza_req = sistema_fabrica.buscar_pieza_por_codigo(cod_pieza)
                        if pieza_req is None:
                            print("Pieza no encontrada.")
                            continue
                        cantidad_req = int(input("Cantidad necesaria de esta pieza para fabricar la máquina: "))
                        m.agregar_requerimiento(pieza_req, cantidad_req)
                    sistema_fabrica.agregar_maquina(m)
                    print(f"Máquina '{descripcion}' agregada con código {codigo}.")

                elif opc_reg == "3":  # Cliente
                    tipo = int(input("¿Cliente Particular (1) o Empresa (2)? "))
                    if tipo == 1:
                        cedula = input("Cédula: ")
                        nombre = input("Nombre completo: ")
                        telefono = input("Teléfono: ")
                        correo = input("Correo electrónico: ")
                        c = ClienteParticular(sistema_fabrica.get_codigo_cliente(), telefono, correo, cedula, nombre)
                        sistema_fabrica.set_codigo_cliente(sistema_fabrica.get_codigo_cliente() + 1)
                        sistema_fabrica.agregar_cliente(c)
                        print(f"Cliente particular '{nombre}' agregado con ID {c.get_id()}.")
                    elif tipo == 2:
                        rut = input("RUT: ")
                        nombre = input("Nombre empresa: ")
                        web = input("Página web: ")
                        telefono = input("Teléfono: ")
                        correo = input("Correo electrónico: ")
                        c = Empresa(sistema_fabrica.get_codigo_cliente(), telefono, correo, rut, nombre, web)
                        sistema_fabrica.set_codigo_cliente(sistema_fabrica.get_codigo_cliente() + 1)
                        sistema_fabrica.agregar_cliente(c)
                        print(f"Empresa '{nombre}' agregada con ID {c.get_id()}.")
                    else:
                        print("Tipo inválido.")

                elif opc_reg == "4":  # Pedido
                    print("Clientes disponibles:")
                    for c in sistema_fabrica.clientes:
                        print(f"{c.get_id()} - ", end="")
                        c.mostrar_datos()
                    id_cliente = int(input("Ingrese ID del cliente: "))
                    cliente = sistema_fabrica.buscar_cliente_por_id(id_cliente)
                    if cliente is None:
                        print("Cliente no encontrado.")
                        continue

                    print("Máquinas disponibles:")
                    for m in sistema_fabrica.maquinas:
                        print(f"{m.get_codigo()} - {m.get_descripcion()}")
                    cod_maquina = int(input("Ingrese código de la máquina: "))
                    maquina_sel = sistema_fabrica.buscar_maquina_por_codigo(cod_maquina)
                    if maquina_sel is None:
                        print("Máquina no encontrada.")
                        continue
                    fecha_recibido = datetime.now()
                    pedido = Pedido(cliente, maquina_sel, fecha_recibido, None)
                    sistema_fabrica.agregar_pedido(pedido)
                    sistema_fabrica.procesar_pedidos_pendientes(pedido)
                    print("Pedido registrado.")

                elif opc_reg == "5":  # Reposición
                    print("Piezas disponibles:")
                    for p in sistema_fabrica.piezas:
                        print(f"{p.get_codigo()} - {p.get_desc_pieza()} (Stock: {p.get_cantidad_pieza()})")
                    cod_pieza = int(input("Ingrese código de la pieza para reposición: "))
                    pieza = sistema_fabrica.buscar_pieza_por_codigo(cod_pieza)
                    if pieza is None:
                        print("Pieza no encontrada.")
                        continue
                    cant = int(input("Cantidad a reponer: "))
                    repos = Reposicion(pieza, cant, datetime.now())
                    sistema_fabrica.agregar_reposicion(repos)
                    sistema_fabrica.procesar_todos_los_pedidos()
                    print("Reposición registrada y stock actualizado.")

                elif opc_reg == "6":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "2":
            while True:
                print("\n-- Listar --")
                print("1. Clientes")
                print("2. Pedidos")
                print("3. Máquinas")
                print("4. Piezas")
                print("5. Contabilidad")
                print("6. Salir")
                opc_list = input("Ingrese opción: ")

                if opc_list == "1":
                    print("Clientes registrados:")
                    for c in sistema_fabrica.clientes:
                        print("--------------")
                        c.imprimir_datos()
                        print("--------------")

                elif opc_list == "2":
                    print("Pedidos pendientes(1), Pedidos Entregados(2), Todos los pedidos(3)")
                    opc_list_ped = input("Ingrese opción: ")
                    if opc_list_ped == "1":
                        print("Pedidos pendientes:")
                        for ped in sistema_fabrica.pedidos:
                            if ped.get_estado() == "Pendiente":
                                print("--------------")
                                ped.mostrarPedidos()
                    elif opc_list_ped == "2":
                        print("Pedidos entregados:")
                        for ped in sistema_fabrica.pedidos:
                            if ped.get_estado() == "Entregado":
                                print("--------------")
                                ped.mostrarPedidos()
                    elif opc_list_ped == "3":
                        print("Todos los pedidos:")
                        for ped in sistema_fabrica.pedidos:
                            print("--------------")
                            ped.mostrarPedidos()
                    else:
                        print("Opción inválida.")

                elif opc_list == "3":
                    print("Máquinas registradas:")
                    for m in sistema_fabrica.maquinas:
                        disp = "Disponible" if m.disponibilidad() else "No disponible"
                        precio = m.costo_produccion() * 1.5
                        print("--------------")
                        print(f"Código: {m.get_codigo()}, Desc: {m.get_descripcion()}, Costo Producción: ${m.costo_produccion():.2f}, Precio: ${precio:.2f}, Disponibilidad: {disp}")
                    print("--------------")

                elif opc_list == "4":
                    print("Piezas registradas:")
                    for p in sistema_fabrica.piezas:
                        print(f"Código: {p.get_codigo()} - Descripción: {p.get_desc_pieza()} - Costo: {p.get_costo_pieza()} - Stock: {p.get_cantidad_pieza()}")
                        print("--------------")
                    sistema_fabrica.listar_faltantes_pedidos_pendientes()

                elif opc_list == "5":
                    precio_total = sum([ped.precio() for ped in sistema_fabrica.pedidos])
                    costo_total = precio_total / 1.5
                    ganancia = precio_total - costo_total
                    impuesto = ganancia * 0.25
                    ganancia_final = ganancia - impuesto
                    print("--------------")
                    print("Contabilidad:")
                    print("--------------")
                    print(f"Ingreso total: ${precio_total:.2f}")
                    print(f"Costo total: ${costo_total:.2f}")
                    print(f"Ganancia bruta: ${ganancia:.2f}")
                    print(f"Impuesto (25%): ${impuesto:.2f}")
                    print(f"Ganancia final: ${ganancia_final:.2f}")
                    print("--------------")

                elif opc_list == "6":
                    break
                else:
                    print("Opción inválida.")

        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()