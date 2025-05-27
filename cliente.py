from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, id, telefono, correoE):
        self.id = id
        self.telefono = telefono
        self.correoE = correoE

    @abstractmethod
    def mostrar_datos(self):
        pass


class ClienteParticular(Cliente):
    def __init__(self, id, telefono, correoE, cedula, nombreCompleto):
        super().__init__(id, telefono, correoE)
        self.cedula = cedula
        self.nombreCompleto = nombreCompleto

    def mostrar_datos(self):
        print(f"Cliente Particular - ID: {self.id}, Nombre: {self.nombreCompleto}, Cédula: {self.cedula}, Tel: {self.telefono}, Email: {self.correoE}")

    def imprimir_datos(self):
        print(f"Cliente Particular - ID: {self.id}, Nombre: {self.nombreCompleto}, Cédula: {self.cedula}, Tel: {self.telefono}, Email: {self.correoE}")

    @property
    def es_empresa(self):
        return False

class Empresa(Cliente):
    def __init__(self, id, telefono, correoE, RUT, nombre, paginaWeb):
        super().__init__(id, telefono, correoE)
        self.RUT = RUT
        self.nombre = nombre
        self.paginaWeb = paginaWeb

    def mostrar_datos(self):
        print(f"Empresa - ID: {self.id}, Nombre: {self.nombre}, RUT: {self.RUT}, Tel: {self.telefono}, Email: {self.correoE}, Web: {self.paginaWeb}")

    def imprimir_datos(self):
        print(f"Empresa - ID: {self.id}, Nombre: {self.nombre}, RUT: {self.RUT}, Tel: {self.telefono}, Email: {self.correoE}, Web: {self.paginaWeb}")
    @property
    def es_empresa(self):
        return True

        
