"""
Prueba de conexión a la base de datos
=====================================

Este script verifica la conexión con SQL Server
y crea las tablas definidas en los modelos.
"""

from ORM.database.database import check_connection, create_tables

# Importa al menos un modelo para que se cree la tabla
from ORM.entities.usuario import Usuario  

if __name__ == "__main__":
    print("Verificando conexión con la base de datos...")
    ok = check_connection()
    print("¿Conexión establecida?:", ok)

    if ok:
        print(" Creando tablas...")
        create_tables()
        print("Tablas creadas en SQL POSTGRE neon.")