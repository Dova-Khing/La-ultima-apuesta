"""
Configuración y conexión a la base de datos
===========================================

Este módulo maneja la conexión a la base de datos usando SQLAlchemy.
"""

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
from contextlib import contextmanager
from typing import Generator
import logging
from .config import DATABASE_URL, DB_ECHO, DB_MAX_OVERFLOW
from sqlalchemy.engine import Engine

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Crear la clase base para los modelos
Base = declarative_base()

""" Configurar el motor de base de datos
 NOTA: pool_size puede dar problemas en Neon, por eso se comenta.
 """
engine = create_engine(
    DATABASE_URL,
    echo=DB_ECHO,
    max_overflow=DB_MAX_OVERFLOW,
    pool_pre_ping=True,
    # Configuraciones específicas para SQLite
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {},
)

# Crear la fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_engine() -> Engine:
    """Retorna el motor de base de datos"""
    return engine


def get_session() -> Session:
    """
    Crea y retorna una nueva sesión de base de datos

    Returns:
        Session: Sesión de SQLAlchemy
    """
    return SessionLocal()


@contextmanager
def get_session_context() -> Generator[Session, None, None]:
    """
    Context manager para manejar sesiones de base de datos

    Yields:
        Session: Sesión de SQLAlchemy
    """
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()


def create_tables() -> None:
    """
    Crea todas las tablas definidas en los modelos

    Esta función debe ser llamada después de importar todos los modelos
    para que SQLAlchemy pueda detectarlos.
    """
    logger.info("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    logger.info("Tablas creadas exitosamente")


def drop_tables() -> None:
    """
    Elimina todas las tablas de la base de datos

    CUIDADO: Esta función elimina TODOS los datos
    """
    logger.warning("Eliminando todas las tablas...")
    Base.metadata.drop_all(bind=engine)
    logger.info("Tablas eliminadas exitosamente")


def check_connection() -> bool:
    """
    Verifica la conexión a la base de datos.

    Returns:
        bool: True si la conexión es exitosa, False en caso contrario.
    """
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    logger.info("Conexión a la base de datos exitosa.")
    return True
