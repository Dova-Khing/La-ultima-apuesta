"""
Operaciones CRUD para Ruleta
============================

Este módulo contiene todas las operaciones de base de datos
para la entidad Ruleta.
"""

from sqlalchemy.orm import Session
from typing import List, Optional

from entities.ruleta import Ruleta
from entities.usuario import Usuario


class RuletaCRUD:
    """Clase para operaciones CRUD de Ruleta"""

    @staticmethod
    def crear_ruleta(db: Session, usuario: Usuario, costo_apuesta: int, premio: int) -> Ruleta:
        """
        Crea un nuevo registro de Ruleta

        Args:
            db: Sesión de base de datos
            usuario: Usuario que juega
            costo_apuesta: Costo de la apuesta
            premio: Premio obtenido

        Returns:
            Ruleta creada
        """
        ruleta = Ruleta(
            usuario_id=usuario.id,
            costo_apuesta=costo_apuesta,
            premio=premio
        )

        db.add(ruleta)
        db.commit()
        db.refresh(ruleta)
        return ruleta

    @staticmethod
    def obtener_por_id(db: Session, ruleta_id: int) -> Optional[Ruleta]:
        """Obtiene un registro de Ruleta por su ID"""
        return db.query(Ruleta).filter(Ruleta.id == ruleta_id).first()

    @staticmethod
    def obtener_todos(db: Session, skip: int = 0, limit: int = 100) -> List[Ruleta]:
        """Obtiene todas las jugadas de Ruleta con paginación"""
        return db.query(Ruleta).offset(skip).limit(limit).all()

    @staticmethod
    def obtener_por_usuario(db: Session, usuario_id: int, skip: int = 0, limit: int = 100) -> List[Ruleta]:
        """Obtiene todas las jugadas de un usuario"""
        return db.query(Ruleta).filter(Ruleta.usuario_id == usuario_id).offset(skip).limit(limit).all()

    @staticmethod
    def actualizar_ruleta(db: Session, ruleta_id: int,
                          costo_apuesta: Optional[int] = None,
                          premio: Optional[int] = None) -> Optional[Ruleta]:
        """
        Actualiza un registro de Ruleta

        Args:
            db: Sesión de base de datos
            ruleta_id: ID de la jugada
            costo_apuesta: Nuevo costo de apuesta (opcional)
            premio: Nuevo premio (opcional)

        Returns:
            Ruleta actualizada o None si no existe
        """
        ruleta = db.query(Ruleta).filter(Ruleta.id == ruleta_id).first()
        if not ruleta:
            return None

        if costo_apuesta is not None:
            ruleta.costo_apuesta = costo_apuesta
        if premio is not None:
            ruleta.premio = premio

        db.commit()
        db.refresh(ruleta)
        return ruleta

    @staticmethod
    def eliminar_ruleta(db: Session, ruleta_id: int) -> bool:
        """
        Elimina un registro de Ruleta permanentemente

        Args:
            db: Sesión de base de datos
            ruleta_id: ID de la jugada

        Returns:
            True si se eliminó, False si no existe
        """
        ruleta = db.query(Ruleta).filter(Ruleta.id == ruleta_id).first()
        if not ruleta:
            return False

        db.delete(ruleta)
        db.commit()
        return True