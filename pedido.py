from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pedido(Base):
    """
    Clase que representa un pedido en la base de datos.
    """
    __tablename__ = 'pedidos'
    
    pedido = Column(Integer, primary_key=True)
    cliente = Column(String)
    producto = Column(String)
    precio = Column(Float)

    def __init__(self, pedido, cliente, producto, precio):
        """
        Constructor de la clase Pedido.

        :param pedido: El número de pedido.
        :param cliente: El nombre del cliente.
        :param producto: El nombre del producto en el pedido.
        :param precio: El precio del producto en el pedido.
        """
        self.pedido = pedido
        self.cliente = cliente
        self.producto = producto
        self.precio = precio
