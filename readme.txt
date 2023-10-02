# mi proyecto phyton back end eleavorado por Miguel Del Rio Ramirez 01-10-23

## Descripción Primera Parte
Este sistema de gestión de pedidos es una aplicación de línea de comandos (CLI) que te permite administrar clientes, productos y pedidos en una base de datos. La aplicación utiliza SQLAlchemy para interactuar con la base de datos y proporciona funciones para agregar, eliminar, actualizar y listar clientes, productos y pedidos.

## Estructura de Directorios
- `main.py`: Contiene la configuración principal de la aplicación.
  
  - `routes.py`: Definición de las rutas y vistas de la aplicación.
- `db/`: Contiene la configuración de la base de datos SQLAlchemy.
  - `cliente.py, pedido.py, producto.py`: Define las clases de modelo para clientes, productos y pedidos.
- `manejo_clientes.py`: Clase para gestionar clientes en la base de datos.
- `manejo_productos.py`: Clase para gestionar productos en la base de datos.
- `manejo_pedidos.py`: Clase para gestionar pedidos en la base de datos.
- `run.py`: Archivo principal para ejecutar la aplicación CLI.
- `static/`: Contiene archivos estáticos como estilos CSS.
- `templates/`: Directorio que contiene plantillas HTML (no utilizadas en la CLI).

## Uso
1. Asegúrate de tener Python instalado en tu sistema.
2. Instala las dependencias ejecutando `pip install sqlalchemy tabulate`.
3. Configura una base de datos SQLAlchemy según tus necesidades en `db/models.py`.
4. Ejecuta la aplicación CLI con el comando `python run.py`.
5. Utiliza el menú principal para gestionar clientes, productos y pedidos.

## Funcionalidades Principales
- Manejo de Clientes:
  - Agregar Cliente.
  - Eliminar Cliente.
  - Actualizar Cliente.
  - Listar Clientes.

- Manejo de Productos:
  - Agregar Producto.
  - Eliminar Producto.
  - Actualizar Producto.
  - Listar Productos.

- Manejo de Pedidos:
  - Agregar Pedido.
  - Eliminar Pedido.
  - Actualizar Pedido.
  - Listar Pedidos.
  - Imprimir Pedido como archivo de ticket.

## Autor
- Autor: Tu Nombre
- Fecha: Fecha de Creación

Este sistema de gestión de pedidos te ayuda a administrar tus datos de manera eficiente. ¡Disfruta de su uso!
Asegúrate de reemplazar "Tu Nombre" y "Fecha de Creación" con tu nombre y la fecha real de creación del sistema. Además, asegúrate de personalizar la sección "Uso" con las instrucciones específicas para tu aplicación, como la configuración de la base de datos y las dependencias.



## Descripción segunda parte
Este proyecto Flask se utiliza para gestionar pedidos y mostrar detalles de los mismos.

## Estructura de directorios
- `app/`: Directorio principal de la aplicación Flask.
  - `__init__.py`: Inicialización de la aplicación Flask.
  - `routes.py`: Definición de las rutas y vistas de la aplicación.
- `templates/`: Directorio que contiene las plantillas HTML.
  - `index.html`: Plantilla para mostrar el listado de pedidos.
  - `pedido.html`: Plantilla para mostrar los detalles de un pedido.
- `datos.db`: Base de datos SQLite que almacena los pedidos.
- `run.py`: Archivo principal para ejecutar la aplicación Flask.

## Archivos y clases
- `db.py`: Contiene la configuración de la base de datos y la función para obtener una sesión de SQLAlchemy.
- `pedido.py`: Define la clase `Pedido` para representar un pedido en la base de datos.
- `manejo_pedidos.py`: Contiene la clase `ManejoPedidos` con métodos para gestionar pedidos en la base de datos.
- `ticket.py`: Define la clase `Tickets` para generar archivos de tickets.
- `static/styles.css`: Archivo CSS con estilos personalizados.

## Instrucciones de configuración
1. Crea un directorio para tu proyecto de Flask.
2. Configura un entorno virtual en el directorio de tu proyecto.
3. Activa el entorno virtual.
4. Instala Flask: `pip install Flask`.
5. Organiza tu proyecto con la estructura de directorios mencionada anteriormente.
6. Asegúrate de que los archivos y clases estén en sus ubicaciones correspondientes.
7. Puedes personalizar los estilos en el archivo `static/styles.css`.
8. Ejecuta la aplicación Flask utilizando `python run.py`.

## Uso
- Ejecuta la aplicación Flask utilizando `python run.py`.
- Abre un navegador web y accede a `http://localhost:5000` para ver el listado de pedidos.

## Personalización
- Puedes personalizar los estilos y la apariencia de las plantillas HTML según tus necesidades.
- Agrega más funcionalidad a la aplicación según los requisitos de tu proyecto.

¡Disfruta trabajando en tu proyecto de Flask!
