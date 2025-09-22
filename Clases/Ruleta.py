import random
import time
from Clases.Usuario import Usuario


class Ruleta:
    """
    Clase que simula un juego de ruleta.

    Permite a un usuario realizar apuestas por número (0-36)
    o por color ('rojo' o 'negro'). El jugador paga un costo
    por jugar y recibe un premio si acierta.
    """

    def __init__(self, usuario: Usuario, costo_apuesta=10, premio=100) -> None:
        """
        Inicializa una instancia de Ruleta.

        Args:
            usuario (Usuario): El jugador que participa.
            costo_apuesta (int, opcional): Costo de cada apuesta. Por defecto 10.
            premio (int, opcional): Premio base para apuestas ganadas. Por defecto 100.
        """
        self.usuario = usuario
        self.costo_apuesta = costo_apuesta
        self.premio = premio

    def jugar(self) -> None:
        """
        Ejecuta una ronda de ruleta.

        Flujo del juego:
        1. Cobra el costo de la apuesta al usuario.
        2. Pide al jugador elegir un número (0–36) o un color ('rojo' o 'negro').
        3. Genera un número aleatorio ganador y su color.
        4. Valida la apuesta:
            - Si acierta el número exacto, gana premio * 3.
            - Si acierta el color, gana premio base.
            - Si no acierta, pierde el costo de la apuesta.
        5. Actualiza y muestra el saldo del usuario.
        """
        resultado = self.usuario.comprar_boleto(self.costo_apuesta)
        if "Fondos insuficientes" in resultado:
            print(resultado)
            return

        print("\n Opciones Ruleta:")
        print(" - Ingresa 'rojo' o 'negro'")
        print(" - Ingresa un número del 0 al 36")
        eleccion: str = input("Tu apuesta: ").lower()

        if eleccion.isdigit():
            eleccion = int(eleccion)

        if isinstance(eleccion, int):
            if eleccion < 0 or eleccion > 36:
                print(" Apuesta inválida. Se tomará por defecto el número 1.")
                eleccion = 1
        elif isinstance(eleccion, str):
            if eleccion.lower() not in ["rojo", "negro"]:
                print(" Apuesta inválida. Se tomará por defecto el color negro.")
                eleccion = "negro"
        else:
            print(" Apuesta inválida. Se tomará por defecto el número 1.")
            eleccion = 1

        print(f"\n {self.usuario.nombre} está jugando a la Ruleta.")
        print(f"Apuesta: {eleccion} (costo ${self.costo_apuesta})")

        time.sleep(1)
        numero = random.randint(0, 36)
        color = random.choice(["rojo", "negro"])
        print(f"La bola cayó en: {numero} {color}")

        if isinstance(eleccion, int) and 0 <= eleccion <= 36:
            if numero == eleccion:
                self.usuario.aumentar_dinero(self.premio * 3)
                print(f" ¡Acertaste el número! Ganaste ${self.premio * 3}")
                print(self.usuario.mostrar_saldo())
                return

        elif isinstance(eleccion, str) and eleccion in ["rojo", "negro"]:
            if color == eleccion:
                self.usuario.aumentar_dinero(self.premio)
                print(f" ¡Acertaste el color! Ganaste ${self.premio}")
                print(self.usuario.mostrar_saldo())
                return

        print(" Perdiste la apuesta.")
