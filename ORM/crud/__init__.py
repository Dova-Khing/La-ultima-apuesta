"""
Módulo de operaciones CRUD
==========================

Este módulo contiene todas las operaciones CRUD (Create, Read, Update, Delete)
para las entidades del sistema de lotería/apuestas.
"""

from .usuario_crud import UsuarioCRUD
from .bingo_crud import BingoCRUD
from .ruleta_crud import RuletaCRUD
from .loteria_crud import LoteriaCRUD

__all__ = ['UsuarioCRUD', 'BingoCRUD', 'RuletaCRUD', 'LoteriaCRUD']