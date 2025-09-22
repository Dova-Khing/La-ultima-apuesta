# Importo clases
from Clases.Usuario import Usuario
from Clases.Loteria import Loteria
from Clases.Ruleta import Ruleta
from Clases.Bingo import Bingo
from Clases.Validaciones import Validaciones


def mostrar_menu() -> None:
    print(
        """
===========================================
    MENÚ DE LA ÚLTIMA APUESTA 
===========================================
1. Jugar Bingo
2. Jugar Ruleta
3. Jugar Lotería
4. Ver datos del usuario
5. Salir
"""
    )


def registrar_usuario() -> Usuario:
    print(
        """
    ====================================
    [ INGRESE SUS DATOS POR FAVOR ]      
    ====================================            
    """
    )

    nombre: str = Validaciones.validar_nombre()
    edad: int = Validaciones.validar_edad()
    saldo_inicial: float = Validaciones.validar_saldo()

    jugador: Usuario = Usuario(nombre, edad, saldo_inicial)
    return jugador


def main() -> None:

    print(
        """
=============================================
   BIENVENIDO A LA ÚLTIMA APUESTA 
=============================================
    """
    )

    jugador: Usuario = registrar_usuario()
    print("\n=== Usuario registrado con éxito ===")
    print(jugador)

    while True:
        mostrar_menu()
        opcion: str = input("Ingrese una Opción: ")

        if opcion == "1":
            bingo = Bingo(jugador, costo_boleto=10, premio=150, max_sorteos=30)
            bingo.jugar()
        elif opcion == "2":

            ruleta = Ruleta(jugador, costo_apuesta=10, premio=50)
            ruleta.jugar()

        elif opcion == "3":
            loteria = Loteria(jugador, costo_boleto=5, premio=200)
            loteria.jugar()

        elif opcion == "4":
            print("\n== DATOS DEL USUARIO ==")
            print(jugador)

        elif opcion == "5":
            print(f" ! Hasta Pronto !, Gracias por jugar {jugador.nombre} ")
            break

        else:
            print(" OPCIÓN INVÁLIDA, INTENTE NUEVAMENTE ")


if __name__ == "__main__":
    main()
