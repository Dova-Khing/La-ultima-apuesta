import random
import time
from Clases.Usuario import Usuario

class Ruleta:
    def __init__(self, usuario: Usuario, costo_apuesta=10, premio=100):
        self.usuario = usuario
        self.costo_apuesta = costo_apuesta
        self.premio = premio

    def jugar(self, eleccion=None):
        """
        El usuario puede elegir:
        - 'rojo' o 'negro'
        - un número del 0 al 36
        Si no elige nada, será 'rojo' por defecto.
        """
        # Cobrar apuesta
        resultado = self.usuario.comprar_boleto(self.costo_apuesta)
        if "Fondos insuficientes" in resultado:
            print(resultado)
            return

        if eleccion is None:
            eleccion = "rojo"

        print(f"\n🎰 {self.usuario.nombre} está jugando a la Ruleta.")
        print(f"Apuesta: {eleccion} (costo ${self.costo_apuesta})")

        time.sleep(1)
        numero = random.randint(0, 36)
        color = random.choice(["rojo", "negro"])
        print(f"La bola cayó en: {numero} {color}")

        # Validar ganancia
        if isinstance(eleccion, int) and 0 <= eleccion <= 36:
            if numero == eleccion:
                self.usuario.aumentar_dinero(self.premio * 3)
                print(f"🏆 ¡Acertaste el número! Ganaste ${self.premio * 3}")
                print(self.usuario.mostrar_saldo())
                return
        elif eleccion in ["rojo", "negro"]:
            if color == eleccion:
                self.usuario.aumentar_dinero(self.premio)
                print(f"🏆 ¡Acertaste el color! Ganaste ${self.premio}")
                print(self.usuario.mostrar_saldo())
                return

        print("😢 Perdiste la apuesta.")