"""
Operaciones CRUD para Partida
=============================

Este módulo contiene todas las operaciones de base de datos
para la entidad Partida.
"""

from sqlalchemy.orm import Session
from typing import List, Optional
from entities.partida import Partida


class PartidaCRUD:
    """Clase para operaciones CRUD de Partida"""

    @staticmethod
    def crear_partida(
        db: Session,
        usuario_id: int,
        juego_id: int,
        costo_apuesta: float,
        estado: str,
        premio_id: Optional[int] = None
    ) -> Partida:
        partida = Partida(
            usuario_id=usuario_id,
            juego_id=juego_id,
            costo_apuesta=costo_apuesta,
            estado=estado,
            premio_id=premio_id
        )
        db.add(partida)
        db.commit()
        db.refresh(partida)
        return partida

    @staticmethod
    def obtener_por_id(db: Session, partida_id: int) -> Optional[Partida]:
        return db.query(Partida).filter(Partida.id == partida_id).first()

    @staticmethod
    def obtener_todas(db: Session, skip: int = 0, limit: int = 100) -> List[Partida]:
        return db.query(Partida).offset(skip).limit(limit).all()

    @staticmethod
    def actualizar_partida(
        db: Session,
        partida_id: int,
        estado: Optional[str] = None,
        premio_id: Optional[int] = None
    ) -> Optional[Partida]:
        partida = db.query(Partida).filter(Partida.id == partida_id).first()
        if not partida:
            return None

        if estado is not None:
            partida.estado = estado
        if premio_id is not None:
            partida.premio_id = premio_id

        db.commit()
        db.refresh(partida)
        return partida

    @staticmethod
    def eliminar_partida(db: Session, partida_id: int) -> bool:
        partida = db.query(Partida).filter(Partida.id == partida_id).first()
        if not partida:
            return False
        db.delete(partida)
        db.commit()
        return True
