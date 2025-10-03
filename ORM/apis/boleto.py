"""
API de Boletos - Endpoints para gestión de boletos
"""

from typing import List
from uuid import UUID

from ORM.crud.Boleto_crud import BoletoCRUD
from ORM.database.config import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from ORM.schemas import BoletoCreate, BoletoResponse, BoletoUpdate, RespuestaAPI
from sqlalchemy.orm import Session

router = APIRouter(prefix="/boletos", tags=["boletos"])


@router.get("/", response_model=List[BoletoResponse])
async def obtener_boletos(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    try:
        return BoletoCRUD.obtener_boletos(db, skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al obtener boletos: {str(e)}"
        )


@router.get("/{boleto_id}", response_model=BoletoResponse)
async def obtener_boleto(boleto_id: UUID, db: Session = Depends(get_db)):
    try:
        boleto = BoletoCRUD.obtener_boleto(db, boleto_id)
        if not boleto:
            raise HTTPException(status_code=404, detail="Boleto no encontrado")
        return boleto
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al obtener boleto: {str(e)}"
        )


@router.post("/", response_model=BoletoResponse, status_code=201)
async def crear_boleto(boleto_data: BoletoCreate, db: Session = Depends(get_db)):
    try:
        return BoletoCRUD.crear_boleto(db, **boleto_data.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear boleto: {str(e)}")


@router.put("/{boleto_id}", response_model=BoletoResponse)
async def actualizar_boleto(
    boleto_id: UUID, boleto_data: BoletoUpdate, db: Session = Depends(get_db)
):
    try:
        boleto = BoletoCRUD.obtener_boleto(db, boleto_id)
        if not boleto:
            raise HTTPException(status_code=404, detail="Boleto no encontrado")

        campos = {k: v for k, v in boleto_data.dict().items() if v is not None}
        return BoletoCRUD.actualizar_boleto(db, boleto_id, **campos)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al actualizar boleto: {str(e)}"
        )


@router.delete("/{boleto_id}", response_model=RespuestaAPI)
async def eliminar_boleto(boleto_id: UUID, db: Session = Depends(get_db)):
    try:
        boleto = BoletoCRUD.obtener_boleto(db, boleto_id)
        if not boleto:
            raise HTTPException(status_code=404, detail="Boleto no encontrado")

        eliminado = BoletoCRUD.eliminar_boleto(db, boleto_id)
        if eliminado:
            return RespuestaAPI(mensaje="Boleto eliminado exitosamente", exito=True)
        raise HTTPException(status_code=500, detail="Error al eliminar boleto")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al eliminar boleto: {str(e)}"
        )
