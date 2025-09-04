"""
Operaciones CRUD para Bingo
===========================

Este módulo contiene todas las operaciones de base de datos
para la entidad Bingo.
"""

from sqlalchemy.orm import Session
from typing import List, Optional

from entities.bingo import Bingo
from entities.usuario import Usuario


class BingoCRUD:
    """Clase para operaciones CRUD de Bingo"""

    @staticmethod
    def crear_bingo(db: Session, usuario: Usuario,
                    costo_boleto: int, premio: int, max_sorteos: int) -> Bingo:
        """
        Crea un nuevo registro de Bingo

        Args:
            db: Sesión de base de datos
            usuario: Usuario que juega
            costo_boleto: Costo del boleto comprado
            premio: Premio obtenido
            max_sorteos: Número máximo de sorteos realizados

        Returns:
            Bingo creado
        """
        bingo = Bingo(
            usuario_id=usuario.id,
            costo_boleto=costo_boleto,
            premio=premio,
            max_sorteos=max_sorteos
        )

        db.add(bingo)
        db.commit()
        db.refresh(bingo)
        return bingo

    @staticmethod
    def obtener_por_id(db: Session, bingo_id: int) -> Optional[Bingo]:
        """Obtiene un registro de Bingo por su ID"""
        return db.query(Bingo).filter(Bingo.id == bingo_id).first()

    @staticmethod
    def obtener_todos(db: Session, skip: int = 0, limit: int = 100) -> List[Bingo]:
        """Obtiene todas las jugadas de Bingo con paginación"""
        return db.query(Bingo).offset(skip).limit(limit).all()

    @staticmethod
    def obtener_por_usuario(db: Session, usuario_id: int, skip: int = 0, limit: int = 100) -> List[Bingo]:
        """Obtiene todas las jugadas de Bingo realizadas por un usuario"""
        return db.query(Bingo).filter(Bingo.usuario_id == usuario_id).offset(skip).limit(limit).all()

    @staticmethod
    def actualizar_bingo(db: Session, bingo_id: int,
                         costo_boleto: Optional[int] = None,
                         premio: Optional[int] = None,
                         max_sorteos: Optional[int] = None) -> Optional[Bingo]:
        """
        Actualiza un registro de Bingo

        Args:
            db: Sesión de base de datos
            bingo_id: ID del registro
            costo_boleto: Nuevo costo del boleto (opcional)
            premio: Nuevo premio (opcional)
            max_sorteos: Nuevo número máximo de sorteos (opcional)

        Returns:
            Bingo actualizado o None si no existe
        """
        bingo = db.query(Bingo).filter(Bingo.id == bingo_id).first()
        if not bingo:
            return None

        if costo_boleto is not None:
            bingo.costo_boleto = costo_boleto
        if premio is not None:
            bingo.premio = premio
        if max_sorteos is not None:
            bingo.max_sorteos = max_sorteos

        db.commit()
        db.refresh(bingo)
        return bingo

    @staticmethod
    def eliminar_bingo(db: Session, bingo_id: int) -> bool:
        """
        Elimina un registro de Bingo permanentemente

        Args:
            db: Sesión de base de datos
            bingo_id: ID del registro

        Returns:
            True si se eliminó, False si no existe
        """
        bingo = db.query(Bingo).filter(Bingo.id == bingo_id).first()
        if not bingo:
            return False

        db.delete(bingo)
        db.commit()
        return True
