"""
Operaciones CRUD para Juego
===========================

Este módulo contiene todas las operaciones de base de datos
para la entidad Juego.
"""

from sqlalchemy.orm import Session
from typing import List, Optional
from entities.juego import Juego


class JuegoCRUD:
    """Clase para operaciones CRUD de Juego"""

    @staticmethod
    def crear_juego(
        db: Session,
        nombre: str,
        descripcion: Optional[str],
        costo_base: float,
        creado_por: Optional[str] = None
    ) -> Juego:
        juego = Juego(
            nombre=nombre,
            descripcion=descripcion,
            costo_base=costo_base,
            creado_por=creado_por
        )
        db.add(juego)
        db.commit()
        db.refresh(juego)
        return juego

    @staticmethod
    def obtener_por_id(db: Session, juego_id: int) -> Optional[Juego]:
        return db.query(Juego).filter(Juego.id == juego_id).first()

    @staticmethod
    def obtener_todos(db: Session, skip: int = 0, limit: int = 100) -> List[Juego]:
        return db.query(Juego).offset(skip).limit(limit).all()

    @staticmethod
    def actualizar_juego(
        db: Session,
        juego_id: int,
        nombre: Optional[str] = None,
        descripcion: Optional[str] = None,
        costo_base: Optional[float] = None,
        actualizado_por: Optional[str] = None
    ) -> Optional[Juego]:
        juego = db.query(Juego).filter(Juego.id == juego_id).first()
        if not juego:
            return None

        if nombre is not None:
            juego.nombre = nombre
        if descripcion is not None:
            juego.descripcion = descripcion
        if costo_base is not None:
            juego.costo_base = costo_base
        if actualizado_por is not None:
            juego.actualizado_por = actualizado_por

        db.commit()
        db.refresh(juego)
        return juego

    @staticmethod
    def eliminar_juego(db: Session, juego_id: int) -> bool:
        juego = db.query(Juego).filter(Juego.id == juego_id).first()
        if not juego:
            return False
        db.delete(juego)
        db.commit()
        return True
