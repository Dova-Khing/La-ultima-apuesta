"""
Entidad Bingo

Modelo de Bingo con SQLAlchemy y esquemas de validación con Pydantic.
"""

from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional

from ..database.database import Base


class Bingo(Base):
    """
    Modelo de Bingo que representa la tabla 'bingos'
    
    Atributos:
        id: Identificador único del juego de bingo
        usuario_id: ID del usuario asociado
        costo_boleto: Costo del boleto del bingo
        premio: Premio obtenido (si aplica)
        max_sorteos: Número máximo de sorteos permitidos
        fecha_registro: Fecha y hora de creación
    """
    
    __tablename__ = 'bingos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    costo_boleto = Column(Float, nullable=False)
    premio = Column(Float, default=0.0)
    max_sorteos = Column(Integer, nullable=False)
    fecha_registro = Column(DateTime, default=datetime.now, nullable=False)
    
    # Relación con Usuario
    usuario = relationship("Usuario", back_populates="bingos")
    
    def __repr__(self):
        return f"<Bingo(id={self.id}, usuario_id={self.usuario_id}, costo_boleto={self.costo_boleto}, premio={self.premio})>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "costo_boleto": self.costo_boleto,
            "premio": self.premio,
            "max_sorteos": self.max_sorteos,
            "fecha_registro": self.fecha_registro.isoformat() if self.fecha_registro else None
        }


# Esquemas de Pydantic

class BingoBase(BaseModel):
    """Esquema base para Bingo"""
    usuario_id: int = Field(..., description="ID del usuario que juega bingo")
    costo_boleto: float = Field(..., gt=0, description="Costo del boleto")
    premio: Optional[float] = Field(0.0, ge=0, description="Premio obtenido")
    max_sorteos: int = Field(..., gt=0, description="Número máximo de sorteos")
    
    @validator("costo_boleto", "premio")
    def validar_valores_positivos(cls, v):
        if v < 0:
            raise ValueError("El valor no puede ser negativo")
        return v


class BingoCreate(BingoBase):
    """Esquema para crear un nuevo Bingo"""
    pass


class BingoUpdate(BaseModel):
    """Esquema para actualizar un Bingo existente"""
    costo_boleto: Optional[float] = Field(None, gt=0)
    premio: Optional[float] = Field(None, ge=0)
    max_sorteos: Optional[int] = Field(None, gt=0)


class BingoResponse(BingoBase):
    """Esquema de respuesta de Bingo"""
    id: int
    fecha_registro: datetime
    
    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
