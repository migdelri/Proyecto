import os
from datetime import datetime

class Tickets:
    def __init__(self):
        pass

    def generar_ticket(self, pedido, cliente_nombre, producto_nombre, precio_producto):
        """
        Crea un archivo de ticket para un pedido.

        :param pedido: El número de pedido.
        :param cliente_nombre: El nombre del cliente.
        :param producto_nombre: El nombre del producto.
        :param precio_producto: El precio del producto.
        """
        # Crear el archivo de ticket
        ticket_filename = f"ticket_pedido_{pedido}.txt"
        with open(ticket_filename, "w") as ticket_file:
            # Escribir la información del ticket
            ticket_file.write(f"Ticket impreso en: - {datetime.now()}\n")
            ticket_file.write(f"Número de Pedido: {pedido}\n")
            ticket_file.write(f"Cliente: {cliente_nombre}\n")
            ticket_file.write(f"Producto: {producto_nombre}\n")
            ticket_file.write(f"Precio: ${precio_producto:.2f}\n")
            ticket_file.write(f"Total: ${precio_producto:.2f}\n")

        print("Ticket generado con éxito.")
        print(f"Se ha creado el archivo de ticket: {ticket_filename}")


        
    