# Proyecto ORM - Juegos (Bingo, Ruleta y Lotería)

Este proyecto implementa un sistema de juegos de azar (Bingo, Ruleta y Lotería) utilizando **SQLAlchemy** con conexión a **PostgreSQL** (Neon Database).  
Incluye operaciones CRUD, validaciones con Pydantic y soporte para migraciones con Alembic.


## Recursos Adicionales

### Documentación Oficial
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Alembic Documentation](https://alembic.sqlalchemy.org/)
- [Neon Documentation](https://neon.tech/docs)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

## Inicio Rápido

Si quieres empezar inmediatamente:

1. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configura Neon:**
   - Crea una cuenta en [neon.tech](https://neon.tech)
   - Crea un nuevo proyecto
   - Copia la cadena de conexión

3. **Configura las variables de entorno:**
   ```bash
   cp env.example .env
   # Edita .env con tu cadena de conexión de Neon
   ```

4. **Crea las tablas automáticamente:**
   ```bash
   alembic revision --autogenerate -m "migracion_inicial"
   alembic upgrade heads
   ```

5. **¡Ejecuta el proyecto!**
   ```bash
   python ORM/login.py
   ```

¿Necesitas más detalles? Continúa leyendo la guía completa abajo.

## Instalación y Configuración

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Configurar Neon Database

#### Paso 1: Crear cuenta en Neon
1. Ve a [neon.tech](https://neon.tech) y crea una cuenta gratuita
2. Inicia sesión en tu dashboard de Neon

#### Paso 2: Crear una nueva base de datos
1. En el dashboard, haz clic en "Create Project"
2. Elige un nombre para tu proyecto (ej: `mi-proyecto-orm`)
3. Selecciona la región más cercana a tu ubicación
4. Haz clic en "Create Project"

#### Paso 3: Obtener la cadena de conexión
1. Una vez creado el proyecto, ve a la sección "Connection Details"
2. Copia la cadena de conexión que aparece (algo como: `postgresql://usuario:password@host/database?sslmode=require`)
3. También anota los datos individuales:
   - **Host**: El host de tu base de datos
   - **Database**: El nombre de la base de datos
   - **Username**: Tu nombre de usuario
   - **Password**: Tu contraseña
   - **Port**: 5432 (por defecto)

### 3. Configurar variables de entorno

1. Copia el archivo de ejemplo:
```bash
cp env.example .env
```

2. Edita el archivo `.env` con tus credenciales reales de Neon:

**Opción A: Usar la cadena de conexión completa (Recomendado)**
```env
DATABASE_URL=postgresql://usuario:password@host/database?sslmode=require
```

**Opción B: Usar variables individuales**
```env
DB_HOST=tu-host.neon.tech
DB_PORT=5432
DB_NAME=tu-base-de-datos
DB_USERNAME=tu-usuario
DB_PASSWORD=tu-password
```

### 4. Verificar la conexión

Ejecuta el script de prueba para verificar que la conexión funciona:

```bash
python test_connection.py
```

### 5. Crear las tablas automáticamente (Método Recomendado)

#### Opción A: Usar test_connection.py (Más fácil)
```bash
python test_connection.py
```

Este script:
- Verifica la conexión a Neon
- Crea automáticamente todas las tablas definidas en las entidades
- Muestra información de la base de datos
- Confirma que todo está funcionando

#### Opción B: Usar migraciones con Alembic (Para proyectos avanzados)

Si prefieres usar migraciones (recomendado para proyectos en producción):

##### Paso 1: Inicializar Alembic (solo la primera vez)
```bash
alembic init migrations
```

##### Paso 2: Configurar alembic.ini
El archivo `alembic.ini` ya está configurado, pero si necesitas modificarlo, asegúrate de que la línea `sqlalchemy.url` esté comentada o vacía, ya que usaremos las variables de entorno.

##### Paso 3: Crear la primera migración
```bash
alembic revision --autogenerate -m "Initial migration"
```

##### Paso 4: Aplicar las migraciones
```bash
alembic upgrade head
```

### 6. Verificar que todo funciona

Ejecuta el script principal para verificar que todo está funcionando:

```bash
python main.py
```
