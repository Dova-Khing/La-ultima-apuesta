"""
Operaciones CRUD para Boleto
============================

Este módulo contiene todas las operaciones de base de datos
para la entidad Boleto.
"""

from sqlalchemy.orm import Session
from typing import List, Optional
from entities.Boleto import Boleto


class BoletoCRUD:
    """Clase para operaciones CRUD de Boleto"""

    @staticmethod
    def crear_boleto(
        db: Session,
        usuario_id: int,
        juego_id: int,
        numeros: Optional[str],
        costo: float,
        creado_por: Optional[str] = None,
    ) -> Boleto:
        boleto = Boleto(
            usuario_id=usuario_id,
            juego_id=juego_id,
            numeros=numeros,
            costo=costo,
            creado_por=creado_por,
        )
        db.add(boleto)
        db.commit()
        db.refresh(boleto)
        return boleto

    @staticmethod
    def obtener_por_id(db: Session, boleto_id: int) -> Optional[Boleto]:
        return db.query(Boleto).filter(Boleto.id == boleto_id).first()

    @staticmethod
    def obtener_todos(db: Session, skip: int = 0, limit: int = 100) -> List[Boleto]:
        return db.query(Boleto).offset(skip).limit(limit).all()

    @staticmethod
    def actualizar_boleto(
        db: Session,
        boleto_id: int,
        numeros: Optional[str] = None,
        actualizado_por: Optional[str] = None,
    ) -> Optional[Boleto]:
        boleto = db.query(Boleto).filter(Boleto.id == boleto_id).first()
        if not boleto:
            return None

        if numeros is not None:
            boleto.numeros = numeros
        if actualizado_por is not None:
            boleto.actualizado_por = actualizado_por

        db.commit()
        db.refresh(boleto)
        return boleto

    @staticmethod
    def eliminar_boleto(db: Session, boleto_id: int) -> bool:
        boleto = db.query(Boleto).filter(Boleto.id == boleto_id).first()
        if not boleto:
            return False
        db.delete(boleto)
        db.commit()
        return True
