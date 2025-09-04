"""
Operaciones CRUD para Lotería
=============================

Este módulo contiene todas las operaciones de base de datos
para la entidad Lotería.
"""

from sqlalchemy.orm import Session
from typing import List, Optional

from entities.loteria import Loteria
from entities.usuario import Usuario


class LoteriaCRUD:
    """Clase para operaciones CRUD de Lotería"""

    @staticmethod
    def crear_loteria(db: Session, usuario: Usuario,
                      costo_boleto: int, premio: int) -> Loteria:
        """
        Crea un nuevo registro de Lotería

        Args:
            db: Sesión de base de datos
            usuario: Usuario que juega
            costo_boleto: Costo del boleto comprado
            premio: Premio obtenido

        Returns:
            Loteria creada
        """
        loteria = Loteria(
            usuario_id=usuario.id,
            costo_boleto=costo_boleto,
            premio=premio
        )

        db.add(loteria)
        db.commit()
        db.refresh(loteria)
        return loteria

    @staticmethod
    def obtener_por_id(db: Session, loteria_id: int) -> Optional[Loteria]:
        """Obtiene un registro de Lotería por su ID"""
        return db.query(Loteria).filter(Loteria.id == loteria_id).first()

    @staticmethod
    def obtener_todos(db: Session, skip: int = 0, limit: int = 100) -> List[Loteria]:
        """Obtiene todas las jugadas de Lotería con paginación"""
        return db.query(Loteria).offset(skip).limit(limit).all()

    @staticmethod
    def obtener_por_usuario(db: Session, usuario_id: int, skip: int = 0, limit: int = 100) -> List[Loteria]:
        """Obtiene todas las jugadas de Lotería realizadas por un usuario"""
        return db.query(Loteria).filter(Loteria.usuario_id == usuario_id).offset(skip).limit(limit).all()

    @staticmethod
    def actualizar_loteria(db: Session, loteria_id: int,
                           costo_boleto: Optional[int] = None,
                           premio: Optional[int] = None) -> Optional[Loteria]:
        """
        Actualiza un registro de Lotería

        Args:
            db: Sesión de base de datos
            loteria_id: ID del registro
            costo_boleto: Nuevo costo del boleto (opcional)
            premio: Nuevo premio (opcional)

        Returns:
            Lotería actualizada o None si no existe
        """
        loteria = db.query(Loteria).filter(Loteria.id == loteria_id).first()
        if not loteria:
            return None

        if costo_boleto is not None:
            loteria.costo_boleto = costo_boleto
        if premio is not None:
            loteria.premio = premio

        db.commit()
        db.refresh(loteria)
        return loteria

    @staticmethod
    def eliminar_loteria(db: Session, loteria_id: int) -> bool:
        """
        Elimina un registro de Lotería permanentemente

        Args:
            db: Sesión de base de datos
            loteria_id: ID del registro

        Returns:
            True si se eliminó, False si no existe
        """
        loteria = db.query(Loteria).filter(Loteria.id == loteria_id).first()
        if not loteria:
            return False

        db.delete(loteria)
        db.commit()
        return True
