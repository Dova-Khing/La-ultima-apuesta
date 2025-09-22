"""
Sistema de gestion de partidas con ORM SQLAlchemy y Neon PostgreSQL
Incluye sistema de autenticacion con login
"""

import getpass
from typing import Optional

from ORM.auth.security import PasswordManager
from ORM.crud.Boleto_crud import BoletoCRUD
from ORM.crud.partida_crud import PartidaCRUD
from ORM.crud.usuario_crud import UsuarioCRUD
from ORM.database.config import SessionLocal
from ORM.entities.Boleto import Boleto
from ORM.entities.partida import Partida
from ORM.entities.usuario import Usuario
from ORM.entities.juego import Juego


class SistemaGestion:
    """Sistema principal de gestion con interfaz de consola y autenticacion"""

    def __init__(self):
        """Inicializar el sistema"""
        self.db = SessionLocal()
        self.usuario_crud = UsuarioCRUD(self.db)
        self.Boleto_crud = BoletoCRUD(self.db)
        self.partida_crud = PartidaCRUD(self.db)
        self.usuario_actual: Optional[Usuario] = None

    def __enter__(self):
        """Context manager entry"""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.db.close()

    def mostrar_pantalla_login(self) -> bool:
        """Mostrar pantalla de login y autenticar usuario"""
        print("\n" + "=" * 50)
        print("        SISTEMA DE GESTION DE PARTIDAS")
        print("=" * 50)
        print("INICIAR SESION")
        print("=" * 50)

        intentos = 0
        max_intentos = 3

        while intentos < max_intentos:
            try:
                print(f"\nIntento {intentos + 1} de {max_intentos}")
                nombre_usuario = input("Nombre de usuario o email: ").strip()

                if not nombre_usuario:
                    print("ERROR: El nombre de usuario es obligatorio")
                    intentos += 1
                    continue

                contrasena = getpass.getpass("Contrasena: ")

                if not contrasena:
                    print("ERROR: La contrasena es obligatoria")
                    intentos += 1
                    continue

                usuario = self.usuario_crud.autenticar_usuario(
                    nombre_usuario, contrasena
                )

                if usuario:
                    self.usuario_actual = usuario
                    print(f"\nEXITO: ¡Bienvenido, {usuario.nombre}!")
                    if usuario.es_admin:
                        print("INFO: Tienes privilegios de administrador")
                    return True
                else:
                    print("ERROR: Credenciales incorrectas o usuario inactivo")
                    intentos += 1

            except KeyboardInterrupt:
                print("\n\nINFO: Operacion cancelada por el usuario")
                return False
            except Exception as e:
                print(f"ERROR: Error durante el login: {e}")
                intentos += 1

        print(
            f"\nERROR: Maximo de intentos ({max_intentos}) excedido. Acceso denegado."
        )
        return False

    def mostrar_menu_principal_autenticado(self) -> None:
        """Mostrar el menu principal para usuario autenticado"""
        print("\n" + "=" * 50)
        print("    SISTEMA DE GESTION DE partidaS")
        print("=" * 50)
        print(f"Usuario: {self.usuario_actual.nombre}")
        print(f"Email: {self.usuario_actual.email}")
        if self.usuario_actual.es_admin:
            print("Administrador")
        print("=" * 50)
        print("1. Gestion de Usuarios")
        print("2. Gestion de Boletos")
        print("3. Gestion de partidas")
        print("4. Consultas y Reportes")
        print("5. Configuracion del Sistema")
        print("6. Mi Perfil")
        print("0. Cerrar Sesion")
        print("=" * 50)

    def mostrar_menu_perfil(self) -> None:
        """Mostrar menu de perfil del usuario"""
        while True:
            print("\n" + "-" * 30)
            print("   MI PERFIL")
            print("-" * 30)
            print("1. Ver Informacion Personal")
            print("2. Actualizar Informacion")
            print("3. Cambiar Contrasena")
            print("0. Volver al menu principal")

            opcion = input("\nSeleccione una opcion: ").strip()

            if opcion == "1":
                self.ver_informacion_personal()
            elif opcion == "2":
                self.actualizar_informacion_personal()
            elif opcion == "3":
                self.cambiar_contrasena()
            elif opcion == "0":
                break
            else:
                print("ERROR: Opcion invalida. Intente nuevamente.")

    def ver_informacion_personal(self) -> None:
        """Ver informacion personal del usuario"""
        try:
            print(f"\n--- INFORMACION PERSONAL ---")
            print(f"Nombre: {self.usuario_actual.nombre}")
            print(f"Nombre de usuario: {self.usuario_actual.nombre_usuario}")
            print(f"Email: {self.usuario_actual.email}")
            print(f"Telefono: {self.usuario_actual.telefono or 'No especificado'}")
            print(f"Estado: {'Activo' if self.usuario_actual.activo else 'Inactivo'}")
            print(
                f"Rol: {'Administrador' if self.usuario_actual.es_admin else 'Usuario'}"
            )
            print(f"Fecha de creacion: {self.usuario_actual.fecha_creacion}")

        except Exception as e:
            print(f"ERROR: Error: {e}")

    def actualizar_informacion_personal(self) -> None:
        """Actualizar informacion personal del usuario"""
        try:
            print(f"\n--- ACTUALIZAR INFORMACION PERSONAL ---")
            print("Deje en blanco para mantener el valor actual")

            nuevo_nombre = input(
                f"Nombre actual ({self.usuario_actual.nombre}): "
            ).strip()
            nuevo_nombre_usuario = input(
                f"Nombre de usuario actual ({self.usuario_actual.nombre_usuario}): "
            ).strip()
            nuevo_email = input(f"Email actual ({self.usuario_actual.email}): ").strip()
            nuevo_telefono = input(
                f"Telefono actual ({self.usuario_actual.telefono or 'No especificado'}): "
            ).strip()

            cambios = {}
            if nuevo_nombre:
                cambios["nombre"] = nuevo_nombre
            if nuevo_nombre_usuario:
                cambios["nombre_usuario"] = nuevo_nombre_usuario
            if nuevo_email:
                cambios["email"] = nuevo_email
            if nuevo_telefono:
                cambios["telefono"] = nuevo_telefono

            if cambios:
                usuario_actualizado = self.usuario_crud.actualizar_usuario(
                    self.usuario_actual.id, **cambios
                )
                if usuario_actualizado:
                    self.usuario_actual = usuario_actualizado
                    print(f"EXITO: Informacion actualizada exitosamente")
                else:
                    print("ERROR: Error al actualizar la informacion")
            else:
                print("INFO: No se realizaron cambios.")

        except ValueError as e:
            print(f"ERROR: Error: {e}")
        except Exception as e:
            print(f"ERROR: Error inesperado: {e}")

    def cambiar_contrasena(self) -> None:
        """Cambiar contrasena del usuario"""
        try:
            print(f"\n--- CAMBIAR CONTRASENA ---")

            contrasena_actual = getpass.getpass("Contrasena actual: ")
            if not contrasena_actual:
                print("ERROR: La contrasena actual es obligatoria")
                return

            nueva_contrasena = getpass.getpass("Nueva contrasena: ")
            if not nueva_contrasena:
                print("ERROR: La nueva contrasena es obligatoria")
                return

            confirmar_contrasena = getpass.getpass("Confirmar nueva contrasena: ")
            if nueva_contrasena != confirmar_contrasena:
                print("ERROR: Las contrasenas no coinciden")
                return

            if self.usuario_crud.cambiar_contrasena(
                self.usuario_actual.id, contrasena_actual, nueva_contrasena
            ):
                print("EXITO: Contrasena cambiada exitosamente")
            else:
                print("ERROR: Error al cambiar la contrasena")

        except ValueError as e:
            print(f"ERROR: Error: {e}")
        except Exception as e:
            print(f"ERROR: Error inesperado: {e}")

    def mostrar_menu_usuarios(self) -> None:
        """Mostrar menu de gestion de usuarios"""
        while True:
            print("\n" + "-" * 30)
            print("   GESTION DE USUARIOS")
            print("-" * 30)
            print("1. Crear Usuario")
            print("2. Listar Usuarios")
            print("3. Buscar Usuario por Email")
            print("4. Buscar Usuario por Nombre de Usuario")
            print("5. Actualizar Usuario")
            print("6. Eliminar Usuario")
            print("7. Crear Usuario Administrador")
            print("0. Volver al menu principal")

            opcion = input("\nSeleccione una opcion: ").strip()

            if opcion == "1":
                self.crear_usuario()
            elif opcion == "2":
                self.listar_usuarios()
            elif opcion == "3":
                self.buscar_usuario_por_email()
            elif opcion == "4":
                self.buscar_usuario_por_nombre_usuario()
            elif opcion == "5":
                self.actualizar_usuario()
            elif opcion == "6":
                self.eliminar_usuario()
            elif opcion == "7":
                self.crear_usuario_admin()
            elif opcion == "0":
                break
            else:
                print("ERROR: Opcion invalida. Intente nuevamente.")

    def crear_usuario(self) -> None:
        """Crear un nuevo usuario"""
        try:
            print("\n--- CREAR USUARIO ---")
            nombre = input("Nombre completo: ").strip()
            nombre_usuario = input("Nombre de usuario: ").strip()
            email = input("Email: ").strip()
            telefono = input("Telefono (opcional): ").strip() or None
            contrasena = getpass.getpass("Contrasena: ")
            edad = input("Edad: ").strip()
            saldo_inicial = input("Saldo inicial: ").strip()
            es_admin = input("¿Es administrador? (s/n): ").strip().lower() == "s"

            usuario = self.usuario_crud.crear_usuario(
                nombre=nombre,
                nombre_usuario=nombre_usuario,
                email=email,
                telefono=telefono,
                contrasena=contrasena,
                edad=edad,
                saldo_inicial=saldo_inicial,
                es_admin=es_admin,
            )

            print(f"EXITO: Usuario creado exitosamente: {usuario}")

        except ValueError as e:
            print(f"ERROR: Error: {e}")
        except Exception as e:
            print(f"ERROR: Error inesperado: {e}")

    def listar_usuarios(self) -> None:
        """Listar todos los usuarios"""
        try:
            usuarios = self.usuario_crud.obtener_usuarios()
            if not usuarios:
                print("INFO: No hay usuarios registrados.")
                return

            print(f"\n--- USUARIOS ({len(usuarios)}) ---")
            for i, usuario in enumerate(usuarios, 1):
                admin_text = " (ADMIN)" if usuario.es_admin else ""
                activo_text = "Activo" if usuario.activo else "Inactivo"
                print(
                    f"{i}. {usuario.nombre} ({usuario.nombre_usuario}) - {usuario.email} - {activo_text}{admin_text}"
                )

        except Exception as e:
            print(f"ERROR: Error: {e}")

    def buscar_usuario_por_email(self) -> None:
        """Buscar usuario por email"""
        try:
            email = input("\nIngrese el email a buscar: ").strip()
            usuario = self.usuario_crud.obtener_usuario_por_email(email)

            if usuario:
                admin_text = " (ADMIN)" if usuario.es_admin else ""
                activo_text = "Activo" if usuario.activo else "Inactivo"
                print(f"EXITO: Usuario encontrado:")
                print(f"   Nombre: {usuario.nombre}")
                print(f"   Nombre de usuario: {usuario.nombre_usuario}")
                print(f"   Email: {usuario.email}")
                print(f"   Telefono: {usuario.telefono or 'No especificado'}")
                print(f"   Edad: {usuario.edad}")
                print(f"   Saldo: {usuario.saldo_inicial}")
                print(f"   Estado: {activo_text}{admin_text}")
            else:
                print("ERROR: Usuario no encontrado.")

        except Exception as e:
            print(f"ERROR: Error: {e}")

    def buscar_usuario_por_nombre_usuario(self) -> None:
        """Buscar usuario por nombre de usuario"""
        try:
            nombre_usuario = input("\nIngrese el nombre de usuario a buscar: ").strip()
            usuario = self.usuario_crud.obtener_usuario_por_nombre_usuario(
                nombre_usuario
            )

            if usuario:
                admin_text = " (ADMIN)" if usuario.es_admin else ""
                activo_text = "Activo" if usuario.activo else "Inactivo"
                print(f"EXITO: Usuario encontrado:")
                print(f"   Nombre: {usuario.nombre}")
                print(f"   Nombre de usuario: {usuario.nombre_usuario}")
                print(f"   Email: {usuario.email}")
                print(f"   Telefono: {usuario.telefono or 'No especificado'}")
                print(f"   Edad: {usuario.edad}")
                print(f"   Saldo: {usuario.saldo_inicial}")
                print(f"   Estado: {activo_text}{admin_text}")
            else:
                print("ERROR: Usuario no encontrado.")

        except Exception as e:
            print(f"ERROR: Error: {e}")

    def actualizar_usuario(self) -> None:
        """Actualizar un usuario"""
        try:
            email = input("\nIngrese el email del usuario a actualizar: ").strip()
            usuario = self.usuario_crud.obtener_usuario_por_email(email)

            if not usuario:
                print("ERROR: Usuario no encontrado.")
                return

            print(f"\nActualizando usuario: {usuario.nombre}")
            print("Deje en blanco para mantener el valor actual")

            nuevo_nombre = input(f"Nombre actual ({usuario.nombre}): ").strip()
            nuevo_nombre_usuario = input(
                f"Nombre de usuario actual ({usuario.nombre_usuario}): "
            ).strip()
            nuevo_email = input(f"Email actual ({usuario.email}): ").strip()
            nuevo_telefono = input(
                f"Telefono actual ({usuario.telefono or 'No especificado'}): "
            ).strip()
            nuevo_edad = input(f"Edad actual ({usuario.edad}): ").strip()
            nuevo_saldo_inicial = input(
                f"Saldo inicial actual ({usuario.saldo_inicial}): "
            ).strip()
            cambios = {}
            if nuevo_nombre:
                cambios["nombre"] = nuevo_nombre
            if nuevo_nombre_usuario:
                cambios["nombre_usuario"] = nuevo_nombre_usuario
            if nuevo_email:
                cambios["email"] = nuevo_email
            if nuevo_telefono:
                cambios["telefono"] = nuevo_telefono
            if nuevo_edad:
                cambios["edad"] = nuevo_edad
            if nuevo_saldo_inicial:
                cambios["saldo_inicial"] = nuevo_saldo_inicial
            if cambios:
                usuario_actualizado = self.usuario_crud.actualizar_usuario(
                    usuario.id, **cambios
                )
                print(f"EXITO: Usuario actualizado: {usuario_actualizado}")
            else:
                print("INFO: No se realizaron cambios.")

        except ValueError as e:
            print(f"ERROR: Error: {e}")
        except Exception as e:
            print(f"ERROR: Error inesperado: {e}")

    def eliminar_usuario(self) -> None:
        """Eliminar un usuario"""
        try:
            email = input("\nIngrese el email del usuario a eliminar: ").strip()
            usuario = self.usuario_crud.obtener_usuario_por_email(email)

            if not usuario:
                print("ERROR: Usuario no encontrado.")
                return

            confirmacion = (
                input(f"¿Esta seguro de eliminar a {usuario.nombre}? (s/n): ")
                .strip()
                .lower()
            )
            if confirmacion == "s":
                if self.usuario_crud.eliminar_usuario(usuario.id):
                    print("EXITO: Usuario eliminado exitosamente.")
                else:
                    print("ERROR: Error al eliminar el usuario.")
            else:
                print("INFO: Operacion cancelada.")

        except Exception as e:
            print(f"ERROR: Error: {e}")

    def crear_usuario_admin(self) -> None:
        """Crear usuario administrador por defecto"""
        try:
            admin = self.usuario_crud.obtener_admin_por_defecto()
            if admin:
                print("INFO: Ya existe un usuario administrador por defecto.")
                return

            contrasena_admin = PasswordManager.generate_secure_password(12)
            admin = self.usuario_crud.crear_usuario(
                nombre="Administrador del Sistema",
                nombre_usuario="admin",
                email="admin@system.com",
                contrasena=contrasena_admin,
                es_admin=True,
            )
            print(f"EXITO: Usuario administrador creado: {admin}")
            print(f"INFO: Contrasena temporal: {contrasena_admin}")
            print(
                "ADVERTENCIA:  IMPORTANTE: Cambie esta contrasena en su primer inicio de sesion"
            )

        except Exception as e:
            print(f"ERROR: Error: {e}")

    def ejecutar(self) -> None:
        """Ejecutar el sistema principal con autenticacion"""
        try:
            print("Iniciando Sistema de Gestion de partidas...")
            print("Configurando base de datos...")
            print("Sistema listo para usar.")

            if not self.mostrar_pantalla_login():
                print("Acceso denegado. Hasta luego!")
                return

            while True:
                self.mostrar_menu_principal_autenticado()
                opcion = input("\nSeleccione una opcion: ").strip()

                if opcion == "1":
                    self.mostrar_menu_usuarios()
                elif opcion == "2":
                    self.mostrar_menu_Boletos()
                elif opcion == "3":
                    self.mostrar_menu_partidas()
                elif opcion == "4":
                    self.mostrar_menu_consultas()
                elif opcion == "5":
                    self.configurar_sistema()
                elif opcion == "6":
                    self.mostrar_menu_perfil()
                elif opcion == "0":
                    print("\n¡Hasta luego!")
                    break
                else:
                    print("ERROR: Opcion invalida. Intente nuevamente.")

        except KeyboardInterrupt:
            print("\n\nSistema interrumpido por el usuario.")
        except Exception as e:
            print(f"\nError critico: {e}")
        finally:
            self.db.close()

    def mostrar_menu_Boletos(self) -> None:
        while True:
            print("\n" + "-" * 30)
            print("   GESTIÓN DE BOLETOS")
            print("-" * 30)
            print("1. Crear Boleto")
            print("2. Listar Boletos")
            print("3. Buscar Boleto por ID")
            print("4. Actualizar Boleto")
            print("5. Eliminar Boleto")
            print("0. Volver al menú principal")

            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "1":
                self.crear_boleto()
            elif opcion == "2":
                self.listar_boletos()
            elif opcion == "3":
                self.buscar_boleto_por_id()
            elif opcion == "4":
                self.actualizar_boleto()
            elif opcion == "5":
                self.eliminar_boleto()
            elif opcion == "0":
                break
            else:
                print("ERROR: Opción inválida. Intente nuevamente.")

    def crear_boleto(self) -> None:
        """Crear un nuevo boleto"""
        with SessionLocal() as db:
            try:
                usuario_id = input("Ingrese el ID del usuario: ").strip()
                juego_id = input("Ingrese el ID del juego: ").strip()
                numeros = input("Ingrese los números separados por comas: ").strip()
                costo = float(input("Ingrese el costo del boleto: ").strip())
                creado_por = input("Ingrese su nombre: ").strip()

                boleto = self.Boleto_crud.crear_boleto(
                    db=db,
                    usuario_id=usuario_id,
                    juego_id=juego_id,
                    numeros=numeros,
                    costo=costo,
                    creado_por=creado_por,
                )
                print(f"Boleto creado correctamente con ID: {boleto.id}")
            except Exception as e:
                print(f"ERROR al crear boleto: {e}")

    def listar_boletos(self) -> None:
        """Listar todos los boletos"""
        with SessionLocal() as db:
            boletos = self.Boleto_crud.obtener_todos(db)
            if not boletos:
                print("No hay boletos registrados.")
                return
            for boleto in boletos:
                print(
                    f"ID: {boleto.id} | Usuario: {boleto.usuario_id} | "
                    f"Juego: {boleto.juego_id} | Numeros: {boleto.numeros} | "
                    f"Costo: {boleto.costo} | Creado por: {boleto.creado_por}"
                )

    def buscar_boleto_por_id(self) -> None:
        """Buscar un boleto por su ID"""
        with SessionLocal() as db:
            boleto_id = input("Ingrese el ID del boleto: ").strip()
            boleto = self.Boleto_crud.obtener_por_id(db, boleto_id)
            if boleto:
                print(
                    f"\nID: {boleto.id}\nUsuario: {boleto.usuario_id}\n"
                    f"Juego: {boleto.juego_id}\nNúmeros: {boleto.numeros}\n"
                    f"Costo: {boleto.costo}\nCreado por: {boleto.creado_por}"
                )
            else:
                print("No se encontró un boleto con ese ID.")

    def actualizar_boleto(self) -> None:
        """Actualizar un boleto existente"""
        with SessionLocal() as db:
            boleto_id = input("Ingrese el ID del boleto a actualizar: ").strip()
            nuevos_numeros = input(
                "Ingrese los nuevos números (dejar vacío para no cambiar): "
            ).strip()
            actualizado_por = input("Ingrese su nombre: ").strip()

            boleto = self.Boleto_crud.actualizar_boleto(
                db=db,
                boleto_id=boleto_id,
                numeros=nuevos_numeros if nuevos_numeros else None,
                actualizado_por=actualizado_por if actualizado_por else None,
            )
            if boleto:
                print("Boleto actualizado correctamente.")
            else:
                print("No se encontró un boleto con ese ID.")

    def eliminar_boleto(self) -> None:
        """Eliminar un boleto por su ID"""
        with SessionLocal() as db:
            boleto_id = input("Ingrese el ID del boleto a eliminar: ").strip()
            exito = self.Boleto_crud.eliminar_boleto(db, boleto_id)
            if exito:
                print("Boleto eliminado correctamente.")
            else:
                print("No se encontró un boleto con ese ID.")

    def mostrar_menu_partidas(self) -> None:
        while True:
            print("\n" + "-" * 30)
            print("   GESTIÓN DE PARTIDAS")
            print("-" * 30)
            print("1. Crear Partida")
            print("2. Listar Partidas")
            print("3. Buscar Partida por ID")
            print("4. Actualizar Partida")
            print("5. Eliminar Partida")
            print("0. Volver al menú principal")

            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "1":
                self.crear_partida()
            elif opcion == "2":
                self.listar_partidas()
            elif opcion == "3":
                self.buscar_partida_por_id()
            elif opcion == "4":
                self.actualizar_partida()
            elif opcion == "5":
                self.eliminar_partida()
            elif opcion == "0":
                break
            else:
                print("ERROR: Opción inválida. Intente nuevamente.")

    def crear_partida(self) -> None:
        """Crear una nueva partida"""
        with self.SessionLocal() as db:
            try:
                usuario_id = input("Ingrese el ID del usuario: ").strip()
                juego_id = input("Ingrese el ID del juego: ").strip()
                costo_apuesta = float(input("Ingrese el costo de la apuesta: ").strip())
                estado = input("Ingrese el estado de la partida: ").strip()
                premio_id = (
                    input("Ingrese el ID del premio (opcional): ").strip() or None
                )

                partida = self.partida_crud.crear_partida(
                    db=db,
                    usuario_id=usuario_id,
                    juego_id=juego_id,
                    costo_apuesta=costo_apuesta,
                    estado=estado,
                    premio_id=premio_id,
                )
                print(f"Partida creada con éxito: {partida}")
            except Exception as e:
                print(f"ERROR al crear la partida: {e}")

    def listar_partidas(self) -> None:
        """Listar todas las partidas"""
        with self.SessionLocal() as db:
            partidas = self.partida_crud.obtener_todas(db)
            if not partidas:
                print("No hay partidas registradas.")
                return
            for partida in partidas:
                print(
                    f"ID: {partida.id}, Usuario: {partida.usuario_id}, Juego: {partida.juego_id}, "
                    f"Apuesta: {partida.costo_apuesta}, Estado: {partida.estado}, Premio: {partida.premio_id}"
                )

    def buscar_partida_por_id(self) -> None:
        """Buscar una partida por su ID"""
        with self.SessionLocal() as db:
            partida_id = input("Ingrese el ID de la partida: ").strip()
            partida = self.partida_crud.obtener_por_id(db, partida_id)
            if partida:
                print(
                    f"ID: {partida.id}, Usuario: {partida.usuario_id}, Juego: {partida.juego_id}, "
                    f"Apuesta: {partida.costo_apuesta}, Estado: {partida.estado}, Premio: {partida.premio_id}"
                )
            else:
                print("Partida no encontrada.")

    def actualizar_partida(self) -> None:
        """Actualizar una partida"""
        with self.SessionLocal() as db:
            partida_id = input("Ingrese el ID de la partida: ").strip()
            estado = (
                input("Ingrese el nuevo estado (dejar vacío para no cambiar): ").strip()
                or None
            )
            premio_id = (
                input(
                    "Ingrese el nuevo ID de premio (dejar vacío para no cambiar): "
                ).strip()
                or None
            )

            partida = self.partida_crud.actualizar_partida(
                db=db, partida_id=partida_id, estado=estado, premio_id=premio_id
            )
            if partida:
                print(f"Partida actualizada con éxito: {partida}")
            else:
                print("No se encontró la partida.")

    def eliminar_partida(self) -> None:
        """Eliminar una partida"""
        with self.SessionLocal() as db:
            partida_id = input("Ingrese el ID de la partida: ").strip()
            eliminado = self.partida_crud.eliminar_partida(db, partida_id)
            if eliminado:
                print("Partida eliminada con éxito.")
            else:
                print("No se encontró la partida.")

    def mostrar_menu_consultas(self) -> None:
        """Mostrar menú de Consultas y Reportes"""
        while True:
            print("\n" + "-" * 30)
            print("   CONSULTAS Y REPORTES")
            print("-" * 30)
            print("1. Consultar Boletos de un Usuario")
            print("2. Consultar Partidas de un Usuario")
            print("3. Consultar Ganancias de un Juego")
            print("4. Consultar Premios Entregados")
            print("5. Consultar Resumen de un Usuario")
            print("0. Volver al menú principal")

            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "1":
                self.consultar_boletos_usuario()
            elif opcion == "2":
                self.consultar_partidas_usuario()
            elif opcion == "3":
                self.consultar_ganancias_juego()
            elif opcion == "4":
                self.consultar_premios_entregados()
            elif opcion == "5":
                self.consultar_resumen_usuario()
            elif opcion == "0":
                break
            else:
                print("ERROR: Opción inválida. Intente nuevamente.")

    def consultar_boletos_usuario(self) -> None:
        """Consultar todos los boletos de un usuario"""
        with self.SessionLocal() as db:
            usuario_id = input("Ingrese el ID del usuario: ").strip()
            boletos = db.query(Boleto).filter(Boleto.usuario_id == usuario_id).all()
            if not boletos:
                print("El usuario no tiene boletos registrados.")
                return
            for boleto in boletos:
                print(
                    f"ID: {boleto.id}, Juego: {boleto.juego_id}, Números: {boleto.numeros}, "
                    f"Costo: {boleto.costo}, Fecha: {boleto.fecha_creacion}"
                )

    def consultar_partidas_usuario(self) -> None:
        """Consultar todas las partidas de un usuario"""
        with self.SessionLocal() as db:
            usuario_id = input("Ingrese el ID del usuario: ").strip()
            partidas = db.query(Partida).filter(Partida.usuario_id == usuario_id).all()
            if not partidas:
                print("El usuario no tiene partidas registradas.")
                return
            for partida in partidas:
                print(
                    f"ID: {partida.id}, Juego: {partida.juego_id}, Apuesta: {partida.costo_apuesta}, "
                    f"Estado: {partida.estado}, Premio: {partida.premio_id}, Fecha: {partida.fecha}"
                )

    def consultar_ganancias_juego(self) -> None:
        """Consultar ganancias totales de un juego"""
        with self.SessionLocal() as db:
            juego_id = input("Ingrese el ID del juego: ").strip()
            partidas = db.query(Partida).filter(Partida.juego_id == juego_id).all()
            if not partidas:
                print("No hay partidas registradas para este juego.")
                return

            total_apuestas = sum(p.costo_apuesta for p in partidas)
            print(f"El juego {juego_id} ha recaudado en apuestas: {total_apuestas}")

    def consultar_premios_entregados(self) -> None:
        """Consultar todos los premios entregados"""
        with self.SessionLocal() as db:
            partidas_con_premio = (
                db.query(Partida).filter(Partida.premio_id.isnot(None)).all()
            )
            if not partidas_con_premio:
                print("No se han entregado premios.")
                return
            for partida in partidas_con_premio:
                print(
                    f"Partida ID: {partida.id}, Usuario: {partida.usuario_id}, Juego: {partida.juego_id}, "
                    f"Premio ID: {partida.premio_id}, Fecha: {partida.fecha}"
                )

    def consultar_resumen_usuario(self) -> None:
        """Consultar resumen general de un usuario (boletos, partidas, premios)"""
        with self.SessionLocal() as db:
            usuario_id = input("Ingrese el ID del usuario: ").strip()

            boletos = db.query(Boleto).filter(Boleto.usuario_id == usuario_id).count()
            partidas = (
                db.query(Partida).filter(Partida.usuario_id == usuario_id).count()
            )
            premios = (
                db.query(Partida)
                .filter(Partida.usuario_id == usuario_id, Partida.premio_id.isnot(None))
                .count()
            )

            print(
                f"Resumen del Usuario {usuario_id}:\n"
                f"- Boletos comprados: {boletos}\n"
                f"- Partidas jugadas: {partidas}\n"
                f"- Premios ganados: {premios}"
            )

    def configurar_sistema(self) -> None:
        while True:
            print("\n" + "-" * 30)
            print(" CONFIGURACIÓN DEL SISTEMA")
            print("-" * 30)
            print("1. Activar Usuario")
            print("2. Desactivar Usuario")
            print("3. Cambiar Rol de Usuario (Admin/Normal)")
            print("4. Actualizar Costo Base de un Juego")
            print("5. Actualizar Nombre/Descripción de un Juego")
            print("0. Volver al menú principal")

            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "1":
                self.activar_usuario()
            elif opcion == "2":
                self.desactivar_usuario()
            elif opcion == "3":
                self.cambiar_rol_usuario()
            elif opcion == "4":
                self.actualizar_costo_juego()
            elif opcion == "5":
                self.actualizar_nombre_juego()
            elif opcion == "0":
                break
            else:
                print("ERROR: Opción inválida. Intente nuevamente.")

    def activar_usuario(self) -> None:
        """Activar un usuario"""
        with self.SessionLocal() as db:
            usuario_id = input("Ingrese el ID del usuario a activar: ").strip()
            usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
            if not usuario:
                print("Usuario no encontrado.")
                return
            usuario.activo = True
            db.commit()
            print(f"Usuario {usuario.nombre} activado correctamente.")

    def desactivar_usuario(self) -> None:
        """Desactivar un usuario"""
        with self.SessionLocal() as db:
            usuario_id = input("Ingrese el ID del usuario a desactivar: ").strip()
            usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
            if not usuario:
                print("Usuario no encontrado.")
                return
            usuario.activo = False
            db.commit()
            print(f"Usuario {usuario.nombre} desactivado correctamente.")

    def cambiar_rol_usuario(self) -> None:
        """Convertir un usuario en administrador o normal"""
        with self.SessionLocal() as db:
            usuario_id = input("Ingrese el ID del usuario: ").strip()
            usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
            if not usuario:
                print("Usuario no encontrado.")
                return
            usuario.es_admin = not usuario.es_admin
            db.commit()
            print(
                f"Usuario {usuario.nombre} ahora es {'Administrador' if usuario.es_admin else 'Usuario normal'}."
            )

    def actualizar_costo_juego(self) -> None:
        """Actualizar el costo base de un juego"""
        with self.SessionLocal() as db:
            juego_id = input("Ingrese el ID del juego: ").strip()
            nuevo_costo = float(input("Ingrese el nuevo costo base: ").strip())
            juego = db.query(Juego).filter(Juego.id == juego_id).first()
            if not juego:
                print("Juego no encontrado.")
                return
            juego.costo_base = nuevo_costo
            db.commit()
            print(f"Costo base del juego {juego.nombre} actualizado a {nuevo_costo}.")

    def actualizar_nombre_juego(self) -> None:
        """Actualizar nombre o descripción de un juego"""
        with self.SessionLocal() as db:
            juego_id = input("Ingrese el ID del juego: ").strip()
            nuevo_nombre = input(
                "Ingrese el nuevo nombre del juego (dejar vacío si no desea cambiar): "
            ).strip()
            nueva_desc = input(
                "Ingrese la nueva descripción (dejar vacío si no desea cambiar): "
            ).strip()

            juego = db.query(Juego).filter(Juego.id == juego_id).first()
            if not juego:
                print("Juego no encontrado.")
                return
            if nuevo_nombre:
                juego.nombre = nuevo_nombre
            if nueva_desc:
                juego.descripcion = nueva_desc

            db.commit()
            print(
                f"Juego actualizado: {juego.nombre} - {juego.descripcion or 'Sin descripción'}"
            )


def main():
    """Funcion principal"""
    with SistemaGestion() as sistema:
        sistema.ejecutar()


if __name__ == "__main__":
    main()
