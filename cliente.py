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
    def id(self, value):
        self.__id = value
        
    @property
    def telefono(self):
        return self.__telefono
    
    @telefono.setter
    def telefono(self, value):
        self.__telefono = value
        
    @property
    def correoE(self):
        return self.__correoE
    
    @correoE.setter
    def correoE(self, value):
        self.__correoE = value

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
    def cedula(self, value):
        self._cedula = value
        
    @property
    def nombreCompleto(self):
        return self.__nombreCompleto
    
    @nombreCompleto.setter
    def nombreCompleto(self, value):
        self.__nombreCompleto = value

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
        self.__RUT = RUT
        self.__nombre = nombre
        self.__paginaWeb = paginaWeb

    @property
    def RUT(self):
        return self.__RUT
    
    @RUT.setter
    def RUT(self, value):
        self.__RUT = value
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value):
        self.__nombre = value
        
    @property
    def paginaWeb(self):
        return self.__paginaWeb
    
    @paginaWeb.setter
    def paginaWeb(self, value):
        self.__paginaWeb = value

    def mostrar_datos(self):
        print(f"Empresa - ID: {self.id}, Nombre: {self.nombre}, RUT: {self.RUT}, Tel: {self.telefono}, Email: {self.correoE}, Web: {self.paginaWeb}")

    def imprimir_datos(self):
        print(f"Empresa - ID: {self.id}, Nombre: {self.nombre}, RUT: {self.RUT}, Tel: {self.telefono}, Email: {self.correoE}, Web: {self.paginaWeb}")
        
    @property
    def es_empresa(self):
        return True
