# Importar las clases necesarias
from db import get_session
from cliente import Cliente
from tabulate import tabulate

class ManejoClientes:
    """
    Clase que proporciona métodos para gestionar clientes en la base de datos.

    Attributes:
        None
    """

    def agregar_cliente(self, clave, nombre, direccion, correo_electronico, telefono):
        """
        Agrega un nuevo cliente a la base de datos.

        :param clave: La clave única del cliente.
        :param nombre: El nombre del cliente.
        :param direccion: La dirección del cliente.
        :param correo_electronico: El correo electrónico del cliente.
        :param telefono: El número de teléfono del cliente.
        """
        # Crear una nueva instancia de Cliente
        nuevo_cliente = Cliente(clave, nombre, direccion, correo_electronico, telefono)
        
        # Iniciar una sesión de SQLAlchemy
        session = get_session()
        
        # Agregar el nuevo cliente a la base de datos
        session.add(nuevo_cliente)
        session.commit()
        
        # Cerrar la sesión
        session.close()

    def eliminar_cliente(self, clave):
        """
        Elimina un cliente de la base de datos.

        :param clave: La clave única del cliente a eliminar.
        """
        # Iniciar una sesión de SQLAlchemy
        session = get_session()
        
        # Buscar el cliente por clave y eliminarlo
        cliente = session.query(Cliente).filter_by(clave=clave).first()
        if cliente:
            session.delete(cliente)
            session.commit()
        
        # Cerrar la sesión
        session.close()

    def actualizar_cliente(self, clave, nombre=None, direccion=None, correo_electronico=None, telefono=None):
        """
        Actualiza los detalles de un cliente en la base de datos.

        :param clave: La clave única del cliente a actualizar.
        :param nombre: El nuevo nombre del cliente (opcional).
        :param direccion: La nueva dirección del cliente (opcional).
        :param correo_electronico: El nuevo correo electrónico del cliente (opcional).
        :param telefono: El nuevo número de teléfono del cliente (opcional).
        """
        # Iniciar una sesión de SQLAlchemy
        session = get_session()
        
        # Buscar el cliente por clave
        cliente = session.query(Cliente).filter_by(clave=clave).first()
        
        if cliente:
            # Actualizar los campos proporcionados
            if nombre is not None:
                cliente.nombre = nombre if nombre != '' else cliente.nombre
            if direccion is not None:
                cliente.direccion = direccion if direccion != '' else cliente.direccion
            if correo_electronico is not None:
                cliente.correo_electronico = correo_electronico if correo_electronico != '' else cliente.correo_electronico
            if telefono is not None:
                cliente.telefono = telefono if telefono != '' else cliente.telefono
            
            session.commit()
        
        # Cerrar la sesión
        session.close()
       
    def listar_clientes(self):
        """
        Lista todos los clientes en la base de datos en forma de tabla.
        """
        # Iniciar una sesión de SQLAlchemy
        session = get_session()
        
        # Obtener todos los clientes de la base de datos
        clientes = session.query(Cliente).all()

        if clientes:
            cliente_data = []
            for cliente in clientes:
                cliente_data.append([
                    cliente.clave,
                    cliente.nombre,
                    cliente.direccion,
                    cliente.correo_electronico,
                    cliente.telefono
                ])

            headers = ["Clave", "Nombre", "Dirección", "Correo Electrónico", "Teléfono"]
            print(tabulate(cliente_data, headers, tablefmt="fancy_grid"))
        else:
            print("No hay clientes registrados en la base de datos.")

        # Cerrar la sesión
        session.close()
    def obtener_cliente_por_id(self, cliente_id):
        """
        Obtiene un cliente por su ID.

        :param cliente_id: El ID del cliente a buscar.
        :return: El cliente encontrado o None si no se encuentra.
        """
        # Iniciar una sesión de SQLAlchemy
        session = get_session()

        # Buscar el cliente por su ID
        cliente = session.query(Cliente).filter_by(clave=cliente_id).first()

        # Cerrar la sesión
        session.close()

        return cliente    

# Autor: Miguel Del Rio
# Fecha: 25-sep-23
