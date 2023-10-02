# Importar las clases necesarias
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

# Crear una instancia de la clase base declarativa
Base = declarative_base()

# Definir la clase Cliente
class Cliente(Base):
    """
    Clase que representa un cliente en la base de datos.

    Attributes:
        clave (str): La clave única del cliente.
        nombre (str): El nombre del cliente.
        direccion (str): La dirección del cliente.
        correo_electronico (str): El correo electrónico del cliente.
        telefono (str): El número de teléfono del cliente.
    """
    __tablename__ = 'clientes'
    
    clave = Column(String, primary_key=True)
    nombre = Column(String)
    direccion = Column(String)
    correo_electronico = Column(String)
    telefono = Column(String)

    def __init__(self, clave, nombre, direccion, correo_electronico, telefono):
        """
        Constructor de la clase Cliente.

        :param clave: La clave única del cliente.
        :param nombre: El nombre del cliente.
        :param direccion: La dirección del cliente.
        :param correo_electronico: El correo electrónico del cliente.
        :param telefono: El número de teléfono del cliente.
        """
        self.clave = clave
        self.nombre = nombre
        self.direccion = direccion
        self.correo_electronico = correo_electronico
        self.telefono = telefono
