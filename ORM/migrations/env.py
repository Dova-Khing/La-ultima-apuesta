from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context
import os
import sys
from dotenv import load_dotenv
from ORM.entities.usuario import Usuario
from ORM.entities.juego import Juego
from ORM.entities.partida import Partida
from ORM.entities.premio import Premio
from ORM.entities.Boleto import Boleto
from ORM.entities.historial_saldo import HistorialSaldo

sys.path.append(os.path.dirname(os.path.abspath(_file_)) + "/../..")
load_dotenv()

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

from ORM.database.database import Base

target_metadata = Base.metadata


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    database_url = os.getenv("DATABASE_URL")
    connectable = engine_from_config(
        {"sqlalchemy.url": database_url},
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
