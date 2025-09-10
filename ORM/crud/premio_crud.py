"""
Operaciones CRUD para Premio
============================

Este módulo contiene todas las operaciones de base de datos
para la entidad Premio.
"""

from sqlalchemy.orm import Session
from typing import List, Optional
from entities.premio import Premio


class PremioCRUD:
    """Clase para operaciones CRUD de Premio"""

    @staticmethod
    def crear_premio(
        db: Session,
        juego_id: int,
        descripcion: str,
        valor: float,
        creado_por: Optional[str] = None
    ) -> Premio:
        premio = Premio(
            juego_id=juego_id,
            descripcion=descripcion,
            valor=valor,
            creado_por=creado_por
        )
        db.add(premio)
        db.commit()
        db.refresh(premio)
        return premio

    @staticmethod
    def obtener_por_id(db: Session, premio_id: int) -> Optional[Premio]:
        return db.query(Premio).filter(Premio.id == premio_id).first()

    @staticmethod
    def obtener_todos(db: Session, skip: int = 0, limit: int = 100) -> List[Premio]:
        return db.query(Premio).offset(skip).limit(limit).all()

    @staticmethod
    def actualizar_premio(
        db: Session,
        premio_id: int,
        descripcion: Optional[str] = None,
        valor: Optional[float] = None,
        actualizado_por: Optional[str] = None
    ) -> Optional[Premio]:
        premio = db.query(Premio).filter(Premio.id == premio_id).first()
        if not premio:
            return None

        if descripcion is not None:
            premio.descripcion = descripcion
        if valor is not None:
            premio.valor = valor
        if actualizado_por is not None:
            premio.actualizado_por = actualizado_por

        db.commit()
        db.refresh(premio)
        return premio

    @staticmethod
    def eliminar_premio(db: Session, premio_id: int) -> bool:
        premio = db.query(Premio).filter(Premio.id == premio_id).first()
        if not premio:
            return False
        db.delete(premio)
        db.commit()
        return True
