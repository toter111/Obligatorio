from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self, id, telefono, correoE):
        self._id = id
        self._telefono = telefono
        self._correoE = correoE

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, value):
        self._id = value
        
    @property
    def telefono(self):
        return self._telefono
    
    @telefono.setter
    def telefono(self, value):
        self._telefono = value
        
    @property
    def correoE(self):
        return self._correoE
    
    @correoE.setter
    def correoE(self, value):
        self._correoE = value

    @abstractmethod
    def mostrar_datos(self):
        pass


class ClienteParticular(Cliente):
    def __init__(self, id, telefono, correoE, cedula, nombreCompleto):
        super().__init__(id, telefono, correoE)
        self._cedula = cedula
        self._nombreCompleto = nombreCompleto

    @property
    def cedula(self):
        return self._cedula
    
    @cedula.setter
    def cedula(self, value):
        self._cedula = value
        
    @property
    def nombreCompleto(self):
        return self._nombreCompleto
    
    @nombreCompleto.setter
    def nombreCompleto(self, value):
        self._nombreCompleto = value

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
        self._RUT = RUT
        self._nombre = nombre
        self._paginaWeb = paginaWeb

    @property
    def RUT(self):
        return self._RUT
    
    @RUT.setter
    def RUT(self, value):
        self._RUT = value
        
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, value):
        self._nombre = value
        
    @property
    def paginaWeb(self):
        return self._paginaWeb
    
    @paginaWeb.setter
    def paginaWeb(self, value):
        self._paginaWeb = value

    def mostrar_datos(self):
        print(f"Empresa - ID: {self.id}, Nombre: {self.nombre}, RUT: {self.RUT}, Tel: {self.telefono}, Email: {self.correoE}, Web: {self.paginaWeb}")

    def imprimir_datos(self):
        print(f"Empresa - ID: {self.id}, Nombre: {self.nombre}, RUT: {self.RUT}, Tel: {self.telefono}, Email: {self.correoE}, Web: {self.paginaWeb}")
        
    @property
    def es_empresa(self):
        return True
