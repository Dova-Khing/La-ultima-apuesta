"""
Operaciones CRUD para HistorialSaldo
====================================

Este módulo contiene todas las operaciones de base de datos
para la entidad HistorialSaldo.
"""

from sqlalchemy.orm import Session
from typing import List, Optional
from entities.historial_saldo import HistorialSaldo


class HistorialSaldoCRUD:
    """Clase para operaciones CRUD de HistorialSaldo"""

    @staticmethod
    def crear_movimiento(
        db: Session, usuario_id: int, tipo: str, monto: float
    ) -> HistorialSaldo:
        movimiento = HistorialSaldo(usuario_id=usuario_id, tipo=tipo, monto=monto)
        db.add(movimiento)
        db.commit()
        db.refresh(movimiento)
        return movimiento

    @staticmethod
    def obtener_por_id(db: Session, movimiento_id: int) -> Optional[HistorialSaldo]:
        return (
            db.query(HistorialSaldo).filter(HistorialSaldo.id == movimiento_id).first()
        )

    @staticmethod
    def obtener_todos(
        db: Session, skip: int = 0, limit: int = 100
    ) -> List[HistorialSaldo]:
        return db.query(HistorialSaldo).offset(skip).limit(limit).all()

    @staticmethod
    def eliminar_movimiento(db: Session, movimiento_id: int) -> bool:
        movimiento = (
            db.query(HistorialSaldo).filter(HistorialSaldo.id == movimiento_id).first()
        )
        if not movimiento:
            return False
        db.delete(movimiento)
        db.commit()
        return True
