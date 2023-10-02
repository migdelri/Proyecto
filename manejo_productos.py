# Importar las clases necesarias
from db import get_session
from producto import Producto
from tabulate import tabulate

class ManejoProductos:
    """
    Clase que proporciona métodos para gestionar productos en la base de datos.

    Attributes:
        None
    """

    def agregar_producto(self, clave, nombre, precio):
        """
        Agrega un nuevo producto a la base de datos.

        :param clave: La clave única del producto.
        :param nombre: El nombre del producto.
        :param precio: El precio del producto.
        """
        # Crear una nueva instancia de Producto
        nuevo_producto = Producto(clave, nombre, precio)
        
        # Iniciar una sesión de SQLAlchemy
        session = get_session()
        
        # Agregar el nuevo producto a la base de datos
        session.add(nuevo_producto)
        session.commit()
        
        # Cerrar la sesión
        session.close()

    def eliminar_producto(self, clave):
        """
        Elimina un producto de la base de datos.

        :param clave: La clave única del producto a eliminar.
        """
        # Iniciar una sesión de SQLAlchemy
        session = get_session()
        
        # Buscar el producto por clave y eliminarlo
        producto = session.query(Producto).filter_by(clave=clave).first()
        if producto:
            session.delete(producto)
            session.commit()
        
        # Cerrar la sesión
        session.close()

    def actualizar_producto(self, clave, nombre=None, precio=None):
        """
        Actualiza los detalles de un producto en la base de datos.

        :param clave: La clave única del producto a actualizar.
        :param nombre: El nuevo nombre del producto (opcional).
        :param precio: El nuevo precio del producto (opcional).
        """
        # Iniciar una sesión de SQLAlchemy
        session = get_session()
        
        # Buscar el producto por clave
        producto = session.query(Producto).filter_by(clave=clave).first()
        
        if producto:
            # Actualizar los campos proporcionados
            if nombre is not None:
                producto.nombre = nombre if nombre != '' else producto.nombre
            if precio is not None:
                producto.precio = precio if precio != '' else producto.precio
        
            session.commit()
        
        # Cerrar la sesión
        session.close()
       
    def listar_productos(self):
        """
        Lista todos los productos en la base de datos en forma de tabla.
        """
        # Iniciar una sesión de SQLAlchemy
        session = get_session()
        
        productos = session.query(Producto).all()
       
        for producto in productos:
            print(producto.clave, producto.nombre, producto.precio)

        
        # Obtener todos los productos de la base de datos
        #productos = session.query(Producto).all()

        if productos:
            producto_data = []
            for producto in productos:
                producto_data.append([
                    producto.clave,
                    producto.nombre,
                    producto.precio
                ])

            headers = ["Clave", "Nombre", "Precio"]
            print(tabulate(producto_data, headers, tablefmt="fancy_grid"))
        else:
            print("No hay productos registrados en la base de datos.")

        # Cerrar la sesión
        session.close()
        
    def obtener_producto_por_id(self, producto_id):
        """
        Obtiene un producto y su precio por su ID.

        :param producto_id: El ID del producto a buscar.
        :return: Un diccionario con el producto y su precio encontrado o None si no se encuentra.
        """
        # Iniciar una sesión de SQLAlchemy
        session = get_session()

        # Buscar el producto por su ID
        producto = session.query(Producto).filter_by(clave=producto_id).first()

        # Cerrar la sesión
        session.close()

        if producto:
            # Si se encuentra el producto, devuelve un diccionario con el producto y su precio
            return {
                'producto': producto,
                'precio': producto.precio
            }
        else:
            return None    

# Autor: Miguel Del Rio
# Fecha: 25-sep-23
