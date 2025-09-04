"""
Entidad Lotería

Modelo de Lotería con SQLAlchemy y esquemas de validación con Pydantic.
"""

from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional

from ..database.database import Base


class Loteria(Base):
    """
    Modelo de Lotería que representa la tabla 'loterias'
    
    Atributos:
        id: Identificador único del juego de lotería
        usuario_id: ID del usuario asociado
        costo_boleto: Costo del boleto
        premio: Premio obtenido (si aplica)
        fecha_registro: Fecha y hora de creación
    """
    
    __tablename__ = "loterias"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    costo_boleto = Column(Float, nullable=False)
    premio = Column(Float, default=0.0)
    fecha_registro = Column(DateTime, default=datetime.now, nullable=False)
    
    # Relación con Usuario
    usuario = relationship("Usuario", back_populates="loterias")
    
    def __repr__(self):
        return f"<Loteria(id={self.id}, usuario_id={self.usuario_id}, costo_boleto={self.costo_boleto}, premio={self.premio})>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "costo_boleto": self.costo_boleto,
            "premio": self.premio,
            "fecha_registro": self.fecha_registro.isoformat() if self.fecha_registro else None
        }


# Esquemas de Pydantic

class LoteriaBase(BaseModel):
    """Esquema base para Lotería"""
    usuario_id: int = Field(..., description="ID del usuario que juega la lotería")
    costo_boleto: float = Field(..., gt=0, description="Costo del boleto")
    premio: Optional[float] = Field(0.0, ge=0, description="Premio obtenido")
    
    @validator("costo_boleto", "premio")
    def validar_valores_positivos(cls, v):
        if v < 0:
            raise ValueError("El valor no puede ser negativo")
        return v


class LoteriaCreate(LoteriaBase):
    """Esquema para crear una nueva Lotería"""
    pass


class LoteriaUpdate(BaseModel):
    """Esquema para actualizar una Lotería existente"""
    costo_boleto: Optional[float] = Field(None, gt=0)
    premio: Optional[float] = Field(None, ge=0)


class LoteriaResponse(LoteriaBase):
    """Esquema de respuesta de Lotería"""
    id: int
    fecha_registro: datetime
    
    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
