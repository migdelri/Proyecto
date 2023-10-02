# Importar las clases necesarias
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Crear una conexión a la base de datos
engine = create_engine('sqlite:///datos.db')  # La base de datos se ubicará en el directorio raíz

# Función para obtener una sesión de SQLAlchemy
def get_session():
    """
    Crea y devuelve una sesión de SQLAlchemy vinculada al motor de la base de datos.

    Returns:
        Session: Una instancia de la clase Session de SQLAlchemy.
    """
    Session = sessionmaker(bind=engine)
    return Session()
