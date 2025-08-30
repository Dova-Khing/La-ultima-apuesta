# Importo clases
from Clases.Usuario import Usuario  # Importa clase Usuario
from Clases.Loteria import Loteria  # Importa clase Loteria
from Clases.Ruleta import Ruleta    # Importa clase Ruleta
from Clases.Bingo import Bingo      # Importa clase Bingo
from Clases.Validaciones import Validaciones # Importa clase Validaciones

#  menu del juego con las opciones a seleccionar
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

    nombre: str = Validaciones.validar_nombre() # Llama la validacion del nombre 
    edad: int = Validaciones.validar_edad()     # llama la validacion de la edad
    saldo_inicial: float = Validaciones.validar_saldo() # llama la validacion de el saldo inicial
    # Se construye instancia de Usuario
    jugador: Usuario = Usuario(nombre,edad,saldo_inicial)  # instancia de jugador donde se tiene las variables que lo conforman
    return jugador


# Menu de bienvenida
def main() -> None: # no retorna nada 
    # Bienvenida
    print("""
=============================================
   ♠️🎰 BIENVENIDO A LA ÚLTIMA APUESTA 🎰♠️
=============================================
    """)

    # Se registra al jugador antes de jugar
    jugador: Usuario = registrar_usuario() # Se llama a registrar el usuario 

    print("\n=== Usuario registrado con éxito ===")
    print(jugador)

    # -- Flujo del Menú Principal --
    while True:
        mostrar_menu() # lLAMA AL MOSTRAR MENU 
        opcion: str = input("Ingrese una Opción: ")

        if opcion == "1":
            bingo = Bingo(jugador, costo_boleto=10, premio=150, max_sorteos=30)
            bingo.jugar() # Llama al metodo de jugar para iniciar el bingo

        elif opcion == "2":
            # Llamo a ruleta jugar
            ruleta = Ruleta(jugador, costo_apuesta=10, premio=50)
            ruleta.jugar() # Llama el metodo de jugar para iniciar el bingo


        elif opcion == "3":
            loteria = Loteria(jugador, costo_boleto=5, premio=200)
            loteria.jugar() # Llama el metodo de jugar para iniciar la loteria

        elif opcion == "4":
            print("\n== DATOS DEL USUARIO ==")
            print(jugador) # Muestra el print de la representacion del objeto

        elif opcion == "5":
            print(f" ! Hasta Pronto !, Gracias por jugar {jugador.nombre} ") # Mensaje de despedida con el nombre del jugador 
            break

        else:
            print("✖️ OPCIÓN INVÁLIDA, INTENTE NUEVAMENTE ✖️")


# Punto de entrada
 
# Punto de entrada / controla como se ejecuta el archivo
# Si el archivo se ejecuta directamente llama a main y impide que si se importa en otro no se ejecute automaticamente 
if __name__ == "__main__":
    main()