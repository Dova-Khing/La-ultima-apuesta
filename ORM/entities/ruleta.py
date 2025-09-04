"""
Entidad Ruleta

Modelo de Ruleta con SQLAlchemy y esquemas de validación con Pydantic.
"""

from sqlalchemy import Column, Integer, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional

from ..database.database import Base


class Ruleta(Base):
    """
    Modelo de Ruleta que representa la tabla 'ruletas'
    
    Atributos:
        id: Identificador único del juego de ruleta
        usuario_id: ID del usuario asociado
        costo_apuesta: Costo de la apuesta realizada
        premio: Premio obtenido (si aplica)
        fecha_registro: Fecha y hora de creación
    """
    
    __tablename__ = "ruletas"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    costo_apuesta = Column(Float, nullable=False)
    premio = Column(Float, default=0.0)
    fecha_registro = Column(DateTime, default=datetime.now, nullable=False)
    
    # Relación con Usuario
    usuario = relationship("Usuario", back_populates="ruletas")
    
    def __repr__(self):
        return f"<Ruleta(id={self.id}, usuario_id={self.usuario_id}, costo_apuesta={self.costo_apuesta}, premio={self.premio})>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "costo_apuesta": self.costo_apuesta,
            "premio": self.premio,
            "fecha_registro": self.fecha_registro.isoformat() if self.fecha_registro else None
        }


# Esquemas de Pydantic

class RuletaBase(BaseModel):
    """Esquema base para Ruleta"""
    usuario_id: int = Field(..., description="ID del usuario que juega la ruleta")
    costo_apuesta: float = Field(..., gt=0, description="Costo de la apuesta")
    premio: Optional[float] = Field(0.0, ge=0, description="Premio obtenido")
    
    @validator("costo_apuesta", "premio")
    def validar_valores_positivos(cls, v):
        if v < 0:
            raise ValueError("El valor no puede ser negativo")
        return v


class RuletaCreate(RuletaBase):
    """Esquema para crear una nueva Ruleta"""
    pass


class RuletaUpdate(BaseModel):
    """Esquema para actualizar una Ruleta existente"""
    costo_apuesta: Optional[float] = Field(None, gt=0)
    premio: Optional[float] = Field(None, ge=0)


class RuletaResponse(RuletaBase):
    """Esquema de respuesta de Ruleta"""
    id: int
    fecha_registro: datetime
    
    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
