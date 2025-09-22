import random
import time
from Clases.Usuario import Usuario


class Loteria:
    """
    Clase que simula un juego de lotería.

    El jugador compra un boleto con un número aleatorio
    y compite contra un número ganador generado por el sistema.
    Si ambos coinciden, gana el premio definido.
    """

    def __init__(self, usuario: Usuario, costo_boleto=5, premio=200) -> None:
        """
        Inicializa una instancia de Loteria.

        Args:
            usuario (Usuario): Jugador que participa en la lotería.
            costo_boleto (int, opcional): Valor del boleto. Por defecto 5.
            premio (int, opcional): Premio por ganar. Por defecto 200.
        """
        self.usuario = usuario
        self.costo_boleto = costo_boleto
        self.premio = premio

    def jugar(self) -> None:
        """
        Ejecuta una ronda de lotería.

        Flujo del juego:
            1. El usuario compra un boleto (si tiene saldo suficiente).
            2. Se genera un número aleatorio para el usuario.
            3. Se genera un número aleatorio ganador.
            4. Si los números coinciden, el usuario recibe el premio.
            5. Si no, se notifica que perdió.
        """
        resultado = self.usuario.comprar_boleto(self.costo_boleto)
        if "Fondos insuficientes" in resultado:
            print(resultado)
            return

        print(f"\n {self.usuario.nombre} está jugando la Lotería.")
        boleto_usuario = random.randint(1000, 9999)
        boleto_ganador = random.randint(1000, 9999)

        time.sleep(1)
        print(f"Tu número: {boleto_usuario}")
        print(f"Número ganador: {boleto_ganador}")

        if boleto_usuario == boleto_ganador:
            self.usuario.aumentar_dinero(self.premio)
            print(f" ¡Felicidades! Ganaste la lotería y recibes ${self.premio}")
            print(self.usuario.mostrar_saldo())
        else:
            print("No ganaste esta vez, sigue intentando.")
