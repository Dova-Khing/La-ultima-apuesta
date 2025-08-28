import random
import time
from Clases.Usuario import Usuario

class Loteria:
    def __init__(self, usuario: Usuario, costo_boleto=5, premio=200):
        self.usuario = usuario
        self.costo_boleto = costo_boleto  # Precio del boleto
        self.premio = premio              # Premio fijo al acertar

    def jugar(self):
        # Cobrar boleto
        resultado = self.usuario.comprar_boleto(self.costo_boleto)
        if "Fondos insuficientes" in resultado:  # Validación de saldo
            print(resultado)
            return

        print(f"\n🎟️ {self.usuario.nombre} está jugando la Lotería.")
        boleto_usuario = random.randint(1000, 9999)   # Número asignado al jugador
        boleto_ganador = random.randint(1000, 9999)  # Número ganador del sorteo

        time.sleep(1)
        print(f"Tu número: {boleto_usuario}")
        print(f"Número ganador: {boleto_ganador}")

        # Validar si ganó
        if boleto_usuario == boleto_ganador:
            self.usuario.aumentar_dinero(self.premio)
            print(f"🏆 ¡Felicidades! Ganaste la lotería y recibes ${self.premio}")
            print(self.usuario.mostrar_saldo())
        else:
            print("😢 No ganaste esta vez, sigue intentando.")