"""
Configuración de la base de datos
=================================

Configuraciones centralizadas para la conexión a la base de datos.
"""

import os

class DatabaseConfig:
    """Configuración de base de datos para diferentes motores."""

    @staticmethod
    def get_sqlite_config(db_name: str = "ejemplo_orm.db") -> str:
        """Configuración para SQLite (desarrollo)."""
        return f"sqlite:///./{db_name}"

    @staticmethod
    def get_postgresql_config(
        host: str = "localhost",
        port: int = 5432,
        database: str = "ejemplo_orm",
        username: str = "postgres",
        password: str = "password"
    ) -> str:
        """Configuración para PostgreSQL (producción)."""
        return f"postgresql://{username}:{password}@{host}:{port}/{database}"

    @staticmethod
    def get_mysql_config(
        host: str = "localhost",
        port: int = 3306,
        database: str = "ejemplo_orm",
        username: str = "root",
        password: str = "password"
    ) -> str:
        """Configuración para MySQL."""
        return f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"

    @staticmethod
    def get_sqlserver_config(
        host: str = "localhost",
        port: int = 1433,
        database: str = "LaUltimaApuesta"
    ) -> str:
        """Configuración para SQL Server usando variables de entorno para evitar que queden expuestos."""
        username = os.getenv("DB_USER", "gerenmake")
        password = os.getenv("LUA_PASSWORD", "2000719dhj")

        return (
            f"mssql+pyodbc://{username}:{password}@{host},{port}/{database}"
            "?driver=ODBC+Driver+17+for+SQL+Server"
        )


"""URL de la base de datos usando SQL Server, se establece para la conexion a la base de datos"""

DATABASE_URL: str = DatabaseConfig.get_sqlserver_config(
    host="localhost",
    port=1433,
    database="LaUltimaApuesta"
)

"""Flag de depuracion py imprime todas las las consultas que ejecuta sql"""
DB_ECHO: bool = os.getenv("DB_ECHO", "True").lower() == "true"