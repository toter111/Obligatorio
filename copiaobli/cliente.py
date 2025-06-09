from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, id, telefono, correoE):
        self.__id = id
        self.__telefono = telefono
        self.__correoE = correoE

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, nuevo_id):
        self.__id = nuevo_id

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, nuevo_telefono):
        self.__telefono = nuevo_telefono

    @property
    def correoE(self):
        return self.__correoE

    @correoE.setter
    def correoE(self, nuevo_correo):
        self.__correoE = nuevo_correo

    @abstractmethod
    def mostrar_datos(self):
        pass

class ClienteParticular(Cliente):
    def __init__(self, id, telefono, correoE, cedula, nombreCompleto):
        super().__init__(id, telefono, correoE)
        self.__cedula = cedula
        self.__nombreCompleto = nombreCompleto

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self, nueva_cedula):
        self.__cedula = nueva_cedula

    @property
    def nombreCompleto(self):
        return self.__nombreCompleto

    @nombreCompleto.setter
    def nombreCompleto(self, nuevo_nombre):
        self.__nombreCompleto = nuevo_nombre

    @property
    def es_empresa(self):
        return False

    def mostrar_datos(self):
        print(f"Cliente Particular - ID: {self.id}, Nombre: {self.nombreCompleto}, "
              f"Cédula: {self.cedula}, Tel: {self.telefono}, Email: {self.correoE}")

    def imprimir_datos(self):
        self.mostrar_datos()

class Empresa(Cliente):
    def __init__(self, id, telefono, correoE, RUT, nombre, paginaWeb):
        super().__init__(id, telefono, correoE)
        self.__RUT = RUT
        self.__nombre = nombre
        self.__paginaWeb = paginaWeb

    @property
    def RUT(self):
        return self.__RUT

    @RUT.setter
    def RUT(self, nuevo_rut):
        self.__RUT = nuevo_rut

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def paginaWeb(self):
        return self.__paginaWeb

    @paginaWeb.setter
    def paginaWeb(self, nueva_web):
        self.__paginaWeb = nueva_web

    @property
    def es_empresa(self):
        return True

    def mostrar_datos(self):
        print(f"Empresa - ID: {self.id}, Nombre: {self.nombre}, RUT: {self.RUT}, "
              f"Tel: {self.telefono}, Email: {self.correoE}, Web: {self.paginaWeb}")

    def imprimir_datos(self):
        self.mostrar_datos()
