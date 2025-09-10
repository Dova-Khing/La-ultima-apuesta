"""
Entidad Usuario
===============

Modelo de Usuario con SQLAlchemy y esquemas de validación con Pydantic.
"""

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field, validator
from datetime import datetime
from typing import Optional, List

from ..database.database import Base


class Usuario(Base):
    """
    Modelo de Usuario que representa la tabla 'usuarios'

    Atributos:
        id: Identificador único del usuario
        nombre: Nombre del usuario
        edad: Edad del usuario
        saldo_inicial: Saldo actual del usuario
        fecha_registro: Fecha de creación
        fecha_actualizacion: Última actualización
    """

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    edad = Column(String(3), nullable=False)
    saldo_inicial = Column(Integer, nullable=False, default=0)
    fecha_registro = Column(DateTime, default=datetime.now, nullable=False)
    fecha_actualizacion = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    # Relaciones (si un usuario participa en juegos)
    bingos = relationship("Bingo", back_populates="usuario", cascade="all, delete-orphan")
    loterias = relationship("Loteria", back_populates="usuario", cascade="all, delete-orphan")
    ruletas = relationship("Ruleta", back_populates="usuario", cascade="all, delete-orphan")

    def __repr__(self)->str:
        return f"<Usuario(id={self.id}, nombre='{self.nombre}', saldo={self.saldo_inicial})>"

    def to_dict(self)->dict [str,any]:
        """Convierte el objeto a un diccionario"""
        return {
            "id": self.id,
            "nombre": self.nombre,
            "edad": self.edad,
            "saldo_inicial": self.saldo_inicial,
            "fecha_registro": self.fecha_registro.isoformat() if self.fecha_registro else None,
            "fecha_actualizacion": self.fecha_actualizacion.isoformat() if self.fecha_actualizacion else None,
        }
"""
ESQUEMAS DE PYDANTIC
"""

class UsuarioBase(BaseModel):
    """Esquema base para Usuario"""
    nombre: str = Field(..., min_length=2, max_length=100, description="Nombre del usuario")
    edad: str = Field(..., min_length=1, max_length=3, description="Edad del usuario")
    saldo_inicial: int = Field(..., ge=0, description="Saldo inicial del usuario")

    @validator("nombre")
    def validar_nombre(cls, v)->str:
        if not v.strip():
            raise ValueError("El nombre no puede estar vacío")
        return v.strip().title()

    @validator("edad")
    def validar_edad(cls, v)->str:
        if not v.isdigit():
            raise ValueError("La edad debe ser numérica")
        return v

    @validator("saldo_inicial")
    def validar_saldo(cls, v)->int:
        if v < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        return v


class UsuarioCreate(UsuarioBase):
    """Esquema para crear un nuevo usuario"""
    pass


class UsuarioUpdate(BaseModel):
    """Esquema para actualizar un usuario"""
    nombre: Optional[str] = Field(None, min_length=2, max_length=100)
    edad: Optional[str] = Field(None, min_length=1, max_length=3)
    saldo_inicial: Optional[int] = Field(None, ge=0)

    @validator("nombre")
    def validar_nombre(cls, v)->str:
        if v is not None and not v.strip():
            raise ValueError("El nombre no puede estar vacío")
        return v.strip().title() if v else v

    @validator("edad")
    def validar_edad(cls, v)->str:
        if v is not None and not v.isdigit():
            raise ValueError("La edad debe ser numérica")
        return v

    @validator("saldo_inicial")
    def validar_saldo(cls, v)->int:
        if v is not None and v < 0:
            raise ValueError("El saldo inicial no puede ser negativo")
        return v


class UsuarioResponse(UsuarioBase):
    """Esquema para respuesta de usuario"""
    id: int
    fecha_registro: datetime
    fecha_actualizacion: Optional[datetime] = None

    class Config:
        from_attributes = True
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }


class UsuarioListResponse(BaseModel):
    """Esquema para lista de usuarios"""
    usuarios: List[UsuarioResponse]
    total: int
    pagina: int
    por_pagina: int

    class Config:
        from_attributes = True
