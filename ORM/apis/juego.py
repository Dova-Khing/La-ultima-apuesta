"""
API de Juegos - Endpoints para gestión de juegos
"""

from typing import List
from uuid import UUID

from ORM.crud.juego_crud import JuegoCRUD
from ORM.database.config import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from ORM.schemas import JuegoCreate, JuegoResponse, JuegoUpdate, RespuestaAPI
from sqlalchemy.orm import Session

router = APIRouter(prefix="/juegos", tags=["juegos"])


@router.get("/", response_model=List[JuegoResponse])
async def obtener_juegos(
    skip: int = 0, limit: int = 100, db: Session = Depends(get_db)
):
    try:
        juego_crud = JuegoCRUD(db)
        return juego_crud.obtener_juegos(skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al obtener juegos: {str(e)}"
        )


@router.get("/{juego_id}", response_model=JuegoResponse)
async def obtener_juego(juego_id: UUID, db: Session = Depends(get_db)):
    try:
        juego_crud = JuegoCRUD(db)
        juego = juego_crud.obtener_juego(juego_id)
        if not juego:
            raise HTTPException(status_code=404, detail="Juego no encontrado")
        return juego
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener juego: {str(e)}")


@router.post("/", response_model=JuegoResponse, status_code=201)
async def crear_juego(juego_data: JuegoCreate, db: Session = Depends(get_db)):
    try:
        juego_crud = JuegoCRUD(db)
        return juego_crud.crear_juego(**juego_data.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear juego: {str(e)}")


@router.put("/{juego_id}", response_model=JuegoResponse)
async def actualizar_juego(
    juego_id: UUID, juego_data: JuegoUpdate, db: Session = Depends(get_db)
):
    try:
        juego_crud = JuegoCRUD(db)
        juego = juego_crud.obtener_juego(juego_id)
        if not juego:
            raise HTTPException(status_code=404, detail="Juego no encontrado")

        campos = {k: v for k, v in juego_data.dict().items() if v is not None}
        return juego_crud.actualizar_juego(juego_id, **campos)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al actualizar juego: {str(e)}"
        )


@router.delete("/{juego_id}", response_model=RespuestaAPI)
async def eliminar_juego(juego_id: UUID, db: Session = Depends(get_db)):
    try:
        juego_crud = JuegoCRUD(db)
        juego = juego_crud.obtener_juego(juego_id)
        if not juego:
            raise HTTPException(status_code=404, detail="Juego no encontrado")

        eliminado = juego_crud.eliminar_juego(juego_id)
        if eliminado:
            return RespuestaAPI(mensaje="Juego eliminado exitosamente", exito=True)
        raise HTTPException(status_code=500, detail="Error al eliminar juego")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al eliminar juego: {str(e)}"
        )
