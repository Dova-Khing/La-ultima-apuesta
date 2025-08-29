import random
import time
from Clases.Usuario import Usuario


class Ruleta:
    def __init__(self, usuario: Usuario, costo_apuesta=10, premio=100):
        self.usuario = usuario
        self.costo_apuesta = costo_apuesta  # Costo de jugar una ronda
        self.premio = premio                # Premio base (se multiplica en algunos casos)

    def jugar(self, eleccion=None):
        """
        - Elección del jugador: 'rojo', 'negro' o número del 0 al 36
        - Si no elige nada → 'rojo' por defecto
        """
        # Descuento de dinero por jugar
        resultado = self.usuario.comprar_boleto(self.costo_apuesta)
        if "Fondos insuficientes" in resultado:  # Validación de saldo
            print(resultado)
            return

        if eleccion is None:
            eleccion = "rojo"  # Opción por defecto

        print(f"\n🎰 {self.usuario.nombre} está jugando a la Ruleta.")
        print(f"Apuesta: {eleccion} (costo ${self.costo_apuesta})")

        # Simulación de la ruleta
        time.sleep(1)
        numero = random.randint(0, 36)          # Número ganador
        color = random.choice(["rojo", "negro"])  # Color ganador
        print(f"La bola cayó en: {numero} {color}")

        # Validar si ganó por número exacto
        if isinstance(eleccion, int) and 0 <= eleccion <= 36:
            if numero == eleccion:
                self.usuario.aumentar_dinero(self.premio * 3)  # Premio multiplicado
                print(f"🏆 ¡Acertaste el número! Ganaste ${self.premio * 3}")
                print(self.usuario.mostrar_saldo())
                return

        # Validar si ganó por color
        elif eleccion in ["rojo", "negro"]:
            if color == eleccion:
                self.usuario.aumentar_dinero(self.premio)
                print(f"🏆 ¡Acertaste el color! Ganaste ${self.premio}")
                print(self.usuario.mostrar_saldo())
                return

        # Si no acierta nada → pierde
        print("😢 Perdiste la apuesta.")