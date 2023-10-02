# Importar las clases necesarias de SQLAlchemy
from sqlalchemy import Column, String, Float
from sqlalchemy.ext.declarative import declarative_base

# Crear una instancia de la clase base declarativa
Base = declarative_base()

# Definir la clase Producto
class Producto(Base):
    """
    Clase que representa un producto en la base de datos.
    """
    __tablename__ = 'productos'
    
    clave = Column(String, primary_key=True)
    nombre = Column(String)
    precio = Column(Float)

    def __init__(self, clave, nombre, precio):
        """
        Constructor de la clase Producto.

        :param clave: La clave única del producto.
        :param nombre: El nombre del producto.
        :param precio: El precio del producto.
        """
        self.clave = clave
        self.nombre = nombre
        self.precio = precio
