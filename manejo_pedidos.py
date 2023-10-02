from db import get_session
from pedido import Pedido
from tabulate import tabulate
from ticket import Tickets

class ManejoPedidos:
    """
    Clase que proporciona métodos para gestionar pedidos en la base de datos.

    Attributes:
        None
    """

    def agregar_pedido(self, pedido, cliente, producto, precio):
        """
        Agrega un nuevo pedido a la base de datos.

        :param pedido: El número de pedido.
        :param cliente: El nombre del cliente.
        :param producto: El nombre del producto en el pedido.
        :param precio: El precio del producto en el pedido.
        """
        # Crear una nueva instancia de Pedido
        nuevo_pedido = Pedido(pedido, cliente, producto, precio)
        
        # Iniciar una sesión de SQLAlchemy
        session = get_session()
        
        # Agregar el nuevo pedido a la base de datos
        session.add(nuevo_pedido)
        session.commit()
        
        # Cerrar la sesión
        session.close()

    def eliminar_pedido(self, pedido):
        """
        Elimina un pedido de la base de datos.

        :param pedido: El número de pedido a eliminar.
        """
        # Iniciar una sesión de SQLAlchemy
        session = get_session()
        
        # Buscar el pedido por número de pedido y eliminarlo
        pedido_db = session.query(Pedido).filter_by(pedido=pedido).first()
        if pedido_db:
            session.delete(pedido_db)
            session.commit()
        
        # Cerrar la sesión
        session.close()

    def actualizar_pedido(self, pedido, cliente=None, producto=None, precio=None):
        """
        Actualiza los detalles de un pedido en la base de datos.

        :param pedido: El número de pedido a actualizar.
        :param cliente: El nuevo nombre del cliente (opcional).
        :param producto: El nuevo nombre del producto en el pedido (opcional).
        :param precio: El nuevo precio del producto en el pedido (opcional).
        """
        # Iniciar una sesión de SQLAlchemy
        session = get_session()
        
        # Buscar el pedido por número de pedido
        pedido_db = session.query(Pedido).filter_by(pedido=pedido).first()
        
        if pedido_db:
            # Actualizar los campos proporcionados
            if cliente is not None:
                pedido_db.cliente = cliente if cliente != '' else pedido_db.cliente
            if producto is not None:
                pedido_db.producto = producto if producto != '' else pedido_db.producto
            if precio is not None:
                pedido_db.precio = precio if precio != '' else pedido_db.precio
        
            session.commit()
        
        # Cerrar la sesión
        session.close()
       
    def listar_pedidos(self):
        """
        Lista todos los pedidos en la base de datos en forma de tabla.
        """
        # Iniciar una sesión de SQLAlchemy
        session = get_session()
        
        pedidos = session.query(Pedido).all()

        if pedidos:
            pedido_data = []
            for pedido in pedidos:
                pedido_data.append([
                    pedido.pedido,
                    pedido.cliente,
                    pedido.producto,
                    pedido.precio
                ])

            headers = ["Pedido", "Cliente", "Producto", "Precio"]
            print(tabulate(pedido_data, headers, tablefmt="fancy_grid"))
        else:
            print("No hay pedidos registrados en la base de datos.")

        # Cerrar la sesión
        session.close()
    
    def print_pedido(self,pedido):
        """
        Imprime un pedido de la tabla pedidos
        
        :param pedido: El número de pedido a imprimir en un txt.
        
        """
        # Iniciar una sesión de SQLAlchemy
        session = get_session()
        
        # Buscar el pedido por número de pedido y eliminarlo
        pedido_pr = session.query(Pedido).filter_by(pedido=pedido).first()
        
        if pedido_pr:
          manejo_tickets = Tickets()
          # Agrgar los campo de pedido a imprimri
          pedido = pedido_pr.pedido
          cliente_nombre = pedido_pr.cliente
          producto_nombre = pedido_pr.producto
          precio_producto = pedido_pr.precio
          #funcion de generar un archivo txt con funcion generar_ tickets del clase tickes 
          manejo_tickets.generar_ticket(pedido, cliente_nombre, producto_nombre, precio_producto)
        else:
           print("No se encontro pedido registrado en la base de datos / Registro no valido") 
    
    def dic_pedidos(self):
        """
        Lista todos los pedidos en la base de datos en forma de tabla.
        """
        # Iniciar una sesión de SQLAlchemy
        session = get_session()
        
        pedidos = session.query(Pedido).all()
        return pedidos

    def ver_pedido(self,pedido):
        """
        Ver un pedido de la tabla pedidos
        
        :param pedido: El número de pedido para rende flack.
        
        """
        # Iniciar una sesión de SQLAlchemy
        session = get_session()
        
        # Buscar el pedido por número de pedido y eliminarlo
        pedido_pr = session.query(Pedido).filter_by(pedido=pedido).first()
        
        return pedido_pr 
