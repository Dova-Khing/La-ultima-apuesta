"""
Operaciones CRUD para Usuario
=============================

Este módulo contiene todas las operaciones de base de datos
para la entidad Usuario.
"""

from sqlalchemy.orm import Session
from typing import List, Optional

from entities.usuario import Usuario
from database.database import get_db


class UsuarioCRUD:
    """Clase para operaciones CRUD de Usuario"""

    @staticmethod
    def crear_usuario(db: Session, nombre: str, edad: str, saldo_inicial: int) -> Usuario:
        """
        Crea un nuevo usuario
        
        Args:
            db: Sesión de base de datos
            nombre: Nombre del usuario
            edad: Edad del usuario
            saldo_inicial: Saldo inicial del usuario

        Returns:
            Usuario: Usuario creado
        """
        usuario = Usuario(
            nombre=nombre,
            edad=edad,
            saldo_inicial=saldo_inicial
        )

        db.add(usuario)
        db.commit()
        db.refresh(usuario)
        return usuario

    @staticmethod
    def obtener_por_id(db: Session, usuario_id: int) -> Optional[Usuario]:
        """Obtiene un usuario por su ID"""
        return db.query(Usuario).filter(Usuario.id == usuario_id).first()

    @staticmethod
    def obtener_todos(db: Session, skip: int = 0, limit: int = 100) -> List[Usuario]:
        """Obtiene todos los usuarios con paginación"""
        return db.query(Usuario).offset(skip).limit(limit).all()

    @staticmethod
    def actualizar_usuario(db: Session, usuario_id: int, nombre: Optional[str] = None,
                           edad: Optional[str] = None, saldo_inicial: Optional[int] = None) -> Optional[Usuario]:
        """
        Actualiza un usuario existente
        
        Args:
            db: Sesión de base de datos
            usuario_id: ID del usuario
            nombre: Nuevo nombre (opcional)
            edad: Nueva edad (opcional)
            saldo_inicial: Nuevo saldo (opcional)

        Returns:
            Usuario actualizado o None si no existe
        """
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if not usuario:
            return None

        if nombre is not None:
            usuario.nombre = nombre
        if edad is not None:
            usuario.edad = edad
        if saldo_inicial is not None:
            usuario.saldo_inicial = saldo_inicial

        db.commit()
        db.refresh(usuario)
        return usuario

    @staticmethod
    def eliminar_usuario(db: Session, usuario_id: int) -> bool:
        """
        Elimina un usuario permanentemente
        
        Args:
            db: Sesión de base de datos
            usuario_id: ID del usuario a eliminar

        Returns:
            True si se eliminó correctamente, False si no existe
        """
        usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
        if not usuario:
            return False

        db.delete(usuario)
        db.commit()
        return True
