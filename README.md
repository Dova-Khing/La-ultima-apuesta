# Sistema de Gestión de Juegos y Apuestas - API REST

Este proyecto implementa un sistema de juegos de azar (Bingo, Ruleta y Lotería) utilizando **API REST** con conexión a **PostgreSQL** (Neon Database).  
Incluye operaciones CRUD y validaciones con Pydantic.


## Recursos Adicionales

### Documentación Oficial
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [Neon Documentation](https://neon.tech/docs)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

## Instalación

Para iniciar el proyecto debes:

1. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Configurar variables de entorno:**
   Crear un archivo `.env` en la raíz del proyecto:
   ```env
   DATABASE_URL=postgresql://usuario:contraseña@host:puerto/database
   ```

3. **Ejecutar el servidor:**
   ```bash
   python ORM/login.py
   ```

El servidor se ejecutará en `http://localhost:8000`

## Documentación de la API

Una vez que el servidor esté ejecutándose, puedes acceder a:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## Endpoints Principales

### Autenticación (`/auth`)
- `POST /auth/login` - Iniciar sesión
- `POST /auth/crear-admin` - Crear usuario administrador
- `GET /auth/verificar/{usuario_id}` - Verificar usuario
- `GET /auth/estado` - Estado del sistema

### Usuarios (`/usuarios`)
- `GET /usuarios/` - Listar usuarios
- `GET /usuarios/{usuario_id}` - Obtener usuario por ID
- `GET /usuarios/email/{email}` - Obtener usuario por email
- `GET /usuarios/username/{nombre_usuario}` - Obtener usuario por nombre de usuario
- `POST /usuarios/` - Crear usuario
- `PUT /usuarios/{usuario_id}` - Actualizar usuario
- `DELETE /usuarios/{usuario_id}` - Eliminar usuario
- `PATCH /usuarios/{usuario_id}/desactivar` - Desactivar usuario
- `POST /usuarios/{usuario_id}/cambiar-contraseña` - Cambiar contraseña
- `GET /usuarios/admin/lista` - Listar administradores
- `GET /usuarios/{usuario_id}/es-admin` - Verificar si es admin

### Juegos (`/juegos`)
- `GET /juegos/` - Listar juegos
- `GET /juegos/{juego_id}` - Obtener juego por ID
- `POST /juegos/` - Crear un nuevo juego
- `PUT /juegos/{juego_id}` - Actualizar un juego existente
- `DELETE /juegos/{juego_id}` - Eliminar un juego

### Premios (`/premios`)
- `GET /premios/` - Listar premios
- `GET /premios/{premio_id}` - Obtener premio por ID
- `POST /premios/` - Crear un premio
- `PUT /premios/{premio_id}` - Actualizar un premio
- `DELETE /premios/{premio_id}` - Eliminar un premio

### Partidas (`/partidas`)
- `GET /partidas/` - Listar partidas
- `GET /partidas/{partida_id}` - Obtener partida por ID
- `POST /partidas/` - Crear una partida
- `PUT /partidas/{partida_id}` - Actualizar una partida
- `DELETE /partidas/{partida_id}` - Eliminar una partida

### Historial de Saldo (`/historial-saldo`)
- `GET /historial-saldo/` - Listar historial de movimientos
- `GET /historial-saldo/{historial_id}` - Obtener registro por ID
- `POST /historial-saldo/` - Crear un registro de movimiento
- `PUT /historial-saldo/{historial_id}` - Actualizar un registro
- `DELETE /historial-saldo/{historial_id}` - Eliminar un registro

### Boletos (`/boletos`)
- `GET /boletos/` - Listar boletos
- `GET /boletos/{boleto_id}` - Obtener boleto por ID
- `POST /boletos/` - Crear un boleto
- `PUT /boletos/{boleto_id}` - Actualizar un boleto
- `DELETE /boletos/{boleto_id}` - Eliminar un boleto
