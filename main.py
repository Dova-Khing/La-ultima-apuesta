# Importo datetime para manejar las fechas de nacimiento
from datetime import datetime, date
# Importo clases
from Clases.Usuario import Usuario  # Importa clase Usuario
from Clases.Loteria import Loteria  # Importa clase Loteria
from Clases.Ruleta import Ruleta    # Importa clase Ruleta
from Clases.Bingo import Bingo      # Importa clase Bingo
from Clases.Validaciones import Validaciones # Importa clase Validaciones


def mostrar_menu() -> None:
    print("""
===========================================
   ♠️🎰  MENÚ DE LA ÚLTIMA APUESTA 🎰♠️
===========================================
1. Jugar Bingo
2. Jugar Ruleta
3. Jugar Lotería
4. Ver datos del usuario
5. Salir
""")


# Solicita los datos al jugador y devuelve una instancia de Usuario
def registrar_usuario() -> Usuario:  # retorna un objeto Usuario
    print("""
    ====================================
    [ INGRESE SUS DATOS POR FAVOR 🐉 ]      
    ====================================            
    """)


    nombre: str = input("Ingrese su Nombre: ").strip()  # Elimina espacios
    edad: int = int(input("Ingrese su Edad: ").strip())
    saldo_inicial: float = float(input("Ingrese su saldo inicial 💰: ").strip())
    nombre: str = Validaciones.validar_nombre()
    edad: int = Validaciones.validar_edad()
    fecha_nacimiento_str: str = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ").strip()
    # Convertimos el dato a tipo de dato datetime
    fecha_nacimiento: date = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()
    saldo_inicial: float = Validaciones.validar_saldo()


    # Se construye instancia de Usuario
    jugador: Usuario = Usuario(nombre, edad,saldo_inicial)
    return jugador


def main() -> None:
    # Bienvenida
    print("""
=============================================
   ♠️🎰 BIENVENIDO A LA ÚLTIMA APUESTA 🎰♠️
=============================================
    """)

    # Se registra al jugador antes de jugar
    jugador: Usuario = registrar_usuario()

    print("\n=== Usuario registrado con éxito ===")
    print(jugador)

    # -- Flujo del Menú Principal --
    while True:
        mostrar_menu()
        opcion: str = input("Ingrese una Opción: ")

        if opcion == "1":
            bingo = Bingo(jugador, costo_boleto=10, premio=150, max_sorteos=30)
            bingo.jugar()

        elif opcion == "2":
            print("\n👉 Opciones Ruleta:")
            print(" - Ingresa 'rojo' o 'negro'")
            print(" - Ingresa un número del 0 al 36")
            eleccion:str = input("Tu apuesta: ")

            # Convertir a número si corresponde
            if eleccion.isdigit():
                eleccion = int(eleccion)

            # Llamo a ruleta jugar
            ruleta = Ruleta(jugador, costo_apuesta=10, premio=50)
            ruleta.jugar(eleccion)

        elif opcion == "3":
            loteria = Loteria(jugador, costo_boleto=5, premio=200)
            loteria.jugar()

        elif opcion == "4":
            print("\n== DATOS DEL USUARIO ==")
            print(jugador) # Muestra el print de la representacion del objeto

        elif opcion == "5":
            print(f" ! Hasta Pronto !, Gracias por jugar {jugador.nombre} ")
            break

        else:
            print("✖️ OPCIÓN INVÁLIDA, INTENTE NUEVAMENTE ✖️")


# Punto de entrada
 
# Punto de entrada / controla como se ejecuta el archivo
# Si el archivo se ejecuta directamente llama a main y impide que si se importa en otro no se ejecute automaticamente 
if __name__ == "__main__":
    main()