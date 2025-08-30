import random
import time
from Clases.Usuario import Usuario

class Loteria:

    # Se crean los constructores
    def __init__(self, usuario: Usuario, costo_boleto=5, premio=200):
        self.usuario = usuario
        self.costo_boleto = costo_boleto
        self.premio = premio

    def jugar(self):
        # Cobrar boleto
        resultado = self.usuario.comprar_boleto(self.costo_boleto)
        if "Fondos insuficientes" in resultado:
            print(resultado) # Imprime el resultado
            return

        print(f"\n🎟️ {self.usuario.nombre} está jugando la Lotería.") # Imprime de manera especifica el nombre del usuario
        boleto_usuario = random.randint(1000, 9999)
        boleto_ganador = random.randint(1000, 9999)

        time.sleep(1)
        print(f"Tu número: {boleto_usuario}")
        print(f"Número ganador: {boleto_ganador}")

        if boleto_usuario == boleto_ganador:
            self.usuario.aumentar_dinero(self.premio)
            print(f"🏆 ¡Felicidades! Ganaste la lotería y recibes ${self.premio}")
            print(self.usuario.mostrar_saldo())
        else:
            print("😢 No ganaste esta vez, sigue intentando.")