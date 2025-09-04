import random
import time
from Clases.Usuario import Usuario

class Ruleta:
    def __init__(self, usuario: Usuario, costo_apuesta=10, premio=100):
        self.usuario = usuario
        self.costo_apuesta = costo_apuesta
        self.premio = premio

    def jugar(self):
        # Descuento de dinero por jugar
        resultado = self.usuario.comprar_boleto(self.costo_apuesta)
        if "Fondos insuficientes" in resultado:  # Validación de saldo
            print(resultado)
            return

        print("\n Opciones Ruleta:")
        print(" - Ingresa 'rojo' o 'negro'")
        print(" - Ingresa un número del 0 al 36")
        eleccion:str = input("Tu apuesta: ").lower()

            # Convertir a número si corresponde
        if eleccion.isdigit():
            eleccion = int(eleccion)

        # Validación de la apuesta
        if isinstance(eleccion, int):
            if eleccion < 0 or eleccion > 36:  # Número inválido
                print(" Apuesta inválida. Se tomará por defecto el número 1.")
                eleccion = 1
        elif isinstance(eleccion, str):
            if eleccion.lower() not in ["rojo", "negro"]:
                print(" Apuesta inválida. Se tomará por defecto el color negro.")
                eleccion = "negro"
        else:
            # Si no es número ni cadena
            print(" Apuesta inválida. Se tomará por defecto el número 1.")
            eleccion = 1

        print(f"\n {self.usuario.nombre} está jugando a la Ruleta.")
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
                print(f" ¡Acertaste el número! Ganaste ${self.premio * 3}")
                print(self.usuario.mostrar_saldo())
                return

        # Validar si ganó por color
        elif isinstance(eleccion, str) and eleccion in ["rojo", "negro"]:
            if color == eleccion:
                self.usuario.aumentar_dinero(self.premio)
                print(f" ¡Acertaste el color! Ganaste ${self.premio}")
                print(self.usuario.mostrar_saldo())
                return

        # Si no acierta nada → pierde
        print(" Perdiste la apuesta.")

