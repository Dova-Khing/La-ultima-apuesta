"""
API de Historial de Saldo - Endpoints para gestión del historial de movimientos
"""

from typing import List
from uuid import UUID

from ORM.crud.historial_saldo_crud import HistorialSaldoCRUD
from ORM.database.config import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from ORM.schemas import (
    HistorialSaldoCreate,
    HistorialSaldoResponse,
    HistorialSaldoUpdate,
    RespuestaAPI,
)
from sqlalchemy.orm import Session

router = APIRouter(prefix="/historial-saldo", tags=["historial_saldo"])


@router.get("/", response_model=List[HistorialSaldoResponse])
async def obtener_historial(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    try:
        return HistorialSaldoCRUD.obtener_historial(db, skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al obtener historial: {str(e)}"
        )


@router.get("/{historial_id}", response_model=HistorialSaldoResponse)
async def obtener_historial_por_id(historial_id: UUID, db: Session = Depends(get_db)):
    try:
        registro = HistorialSaldoCRUD.obtener_por_id(db, historial_id)
        if not registro:
            raise HTTPException(status_code=404, detail="Registro no encontrado")
        return registro
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al obtener registro: {str(e)}"
        )


@router.post("/", response_model=HistorialSaldoResponse, status_code=201)
async def crear_historial(
    historial_data: HistorialSaldoCreate, db: Session = Depends(get_db)
):
    try:
        return HistorialSaldoCRUD.crear_historial(db, **historial_data.dict())
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al crear registro: {str(e)}"
        )


@router.put("/{historial_id}", response_model=HistorialSaldoResponse)
async def actualizar_historial(
    historial_id: UUID,
    historial_data: HistorialSaldoUpdate,
    db: Session = Depends(get_db),
):
    try:
        registro = HistorialSaldoCRUD.obtener_por_id(db, historial_id)
        if not registro:
            raise HTTPException(status_code=404, detail="Registro no encontrado")

        campos = {k: v for k, v in historial_data.dict().items() if v is not None}
        return HistorialSaldoCRUD.actualizar_historial(db, historial_id, **campos)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al actualizar registro: {str(e)}"
        )


@router.delete("/{historial_id}", response_model=RespuestaAPI)
async def eliminar_historial(historial_id: UUID, db: Session = Depends(get_db)):
    try:
        registro = HistorialSaldoCRUD.obtener_por_id(db, historial_id)
        if not registro:
            raise HTTPException(status_code=404, detail="Registro no encontrado")

        eliminado = HistorialSaldoCRUD.eliminar_historial(db, historial_id)
        if eliminado:
            return RespuestaAPI(mensaje="Registro eliminado exitosamente", exito=True)
        raise HTTPException(status_code=500, detail="Error al eliminar registro")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al eliminar registro: {str(e)}"
        )
