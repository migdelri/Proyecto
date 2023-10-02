from manejo_clientes import ManejoClientes
from manejo_productos import ManejoProductos
from manejo_pedidos import ManejoPedidos

# Instancias de las clases ManejoClientes, ManejoProductos y ManejoPedidos
manejo_clientes = ManejoClientes()
manejo_productos = ManejoProductos()
manejo_pedidos = ManejoPedidos()

while True:
    """
    Menú principal de manejo de clientes, productos y pedidos.
    """
    print("\nMenú de Manejo de Clientes, Productos y Pedidos:")
    print("1. Manejo de Clientes")
    print("2. Manejo de Productos")
    print("3. Manejo de Pedidos")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        while True:
            print("\nMenú de Manejo de Clientes:")
            print("1. Agregar Cliente")
            print("2. Eliminar Cliente")
            print("3. Actualizar Cliente")
            print("4. Listar Clientes")
            print("5. Volver al Menú Principal")
            
            opcion_cliente = input("Seleccione una opción para manejo de clientes: ")
            
            if opcion_cliente == '1':
                clave = input("Ingrese la clave del cliente: ")
                nombre = input("Ingrese el nombre del cliente: ")
                direccion = input("Ingrese la dirección del cliente: ")
                correo = input("Ingrese el correo electrónico del cliente: ")
                telefono = input("Ingrese el teléfono del cliente: ")
                manejo_clientes.agregar_cliente(clave, nombre, direccion, correo, telefono)
                print("Cliente agregado con éxito.")
            
            elif opcion_cliente == '2':
                clave = input("Ingrese la clave del cliente que desea eliminar: ")
                manejo_clientes.eliminar_cliente(clave)
                print("Cliente eliminado con éxito.")
            
            elif opcion_cliente == '3':
                clave = input("Ingrese la clave del cliente que desea actualizar: ")
                nombre = input("Ingrese el nuevo nombre (o presione Enter para dejar sin cambios): ")
                direccion = input("Ingrese la nueva dirección (o presione Enter para dejar sin cambios): ")
                correo = input("Ingrese el nuevo correo electrónico (o presione Enter para dejar sin cambios): ")
                telefono = input("Ingrese el nuevo teléfono (o presione Enter para dejar sin cambios): ")
                manejo_clientes.actualizar_cliente(clave, nombre, direccion, correo, telefono)
                print("Cliente actualizado con éxito.")
            
            elif opcion_cliente == '4':
                manejo_clientes.listar_clientes()
            
            elif opcion_cliente == '5':
                break
            
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
    
    elif opcion == '2':
        while True:
            print("\nMenú de Manejo de Productos:")
            print("1. Agregar Producto")
            print("2. Eliminar Producto")
            print("3. Actualizar Producto")
            print("4. Listar Productos")
            print("5. Volver al Menú Principal")
            
            opcion_producto = input("Seleccione una opción para manejo de productos: ")
            
            if opcion_producto == '1':
                clave = input("Ingrese la clave del producto: ")
                nombre = input("Ingrese el nombre del producto: ")
                precio = input("Ingrese el precio del producto: ")
                manejo_productos.agregar_producto(clave, nombre, precio)
                print("Producto agregado con éxito.")
            
            elif opcion_producto == '2':
                clave = input("Ingrese la clave del producto que desea eliminar: ")
                manejo_productos.eliminar_producto(clave)
                print("Producto eliminado con éxito.")
            
            elif opcion_producto == '3':
                clave = input("Ingrese la clave del producto que desea actualizar: ")
                nombre = input("Ingrese el nuevo nombre (o presione Enter para dejar sin cambios): ")
                precio = input("Ingrese el nuevo precio (o presione Enter para dejar sin cambios): ")
                manejo_productos.actualizar_producto(clave, nombre, precio)
                print("Producto actualizado con éxito.")
            
            elif opcion_producto == '4':
                manejo_productos.listar_productos()
            
            elif opcion_producto == '5':
                break
            
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

    elif opcion == '3':
        while True:
            print("\nMenú de Manejo de Pedidos:")
            print("1. Agregar Pedido")
            print("2. Eliminar Pedido")
            print("3. Actualizar Pedido")
            print("4. Listar Pedidos")
            print("5. Imprimir Pedido")
            print("6. Volver al Menú Principal")
            
            opcion_pedido = input("Seleccione una opción para manejo de pedidos: ")
            
            if opcion_pedido == '1':
               pedido = input("Ingrese el número de pedido: ")

            # Obtener la lista de clientes y productos disponibles
               manejo_clientes.listar_clientes()
               cliente_id = input("Seleccione el ID del cliente: ")
               cliente = manejo_clientes.obtener_cliente_por_id(cliente_id)

               manejo_productos.listar_productos()
               producto_id = input("Seleccione el ID del producto: ")
               # Llama a la función para obtener el producto y precio
               resultado = manejo_productos.obtener_producto_por_id(producto_id)

               # Verifica si se encontró un producto
               if resultado is not None:
                  producto_encontrado = resultado['producto']
                  precio_producto = resultado['precio']
                  
                  manejo_pedidos.agregar_pedido(pedido, cliente.nombre, producto_encontrado.nombre, precio_producto)
                  print("Pedido agregado con éxito.")
                  
               # Ahora puedes utilizar producto_encontrado y precio_producto en tu código
                  #print("Producto encontrado:", producto_encontrado.nombre)
                  #print("Precio del producto:", precio_producto)
               else:
                print("Producto no encontrado.")

            elif opcion_pedido == '2':
                pedido = input("Ingrese el número de pedido que desea eliminar: ")
                manejo_pedidos.eliminar_pedido(pedido)
                print("Pedido eliminado con éxito.")
            
            elif opcion_pedido == '3':
                pedido = input("Ingrese el número de pedido que desea actualizar: ")
                cliente = input("Ingrese el nuevo nombre del cliente (o presione Enter para dejar sin cambios): ")
                producto = input("Ingrese el nuevo nombre del producto (o presione Enter para dejar sin cambios): ")
                precio = input("Ingrese el nuevo precio (o presione Enter para dejar sin cambios): ")
                manejo_pedidos.actualizar_pedido(pedido, cliente, producto, precio)
                print("Pedido actualizado con éxito.")
            
            elif opcion_pedido == '4':
                manejo_pedidos.listar_pedidos()
           
            elif opcion_pedido == '5':
                manejo_pedidos.listar_pedidos()
                pedido = input("Ingrese el número de pedido que desea imprimir: ")
                manejo_pedidos.print_pedido(pedido)
            
            
            elif opcion_pedido == '6':
                break
            
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
    
    elif opcion == '4':
        print("Saliendo del programa. ¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
