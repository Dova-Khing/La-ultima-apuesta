import random
import time
from Clases.Usuario import Usuario

class Bingo:
    def __init__(self, usuario: Usuario, costo_boleto=10, premio=100, max_sorteos=30):
        self.usuario = usuario
        self.costo_boleto = costo_boleto   # Precio por jugar
        self.premio = premio               # Dinero que gana el jugador si completa el cartón
        self.max_sorteos = max_sorteos     # Máximo de intentos para sacar números
        self.carton = self.generar_carton()  # Cartón 5x5 generado al iniciar

    def generar_carton(self):
        """Genera un cartón de bingo 5x5 con números aleatorios de 1 a 50"""
        numeros = random.sample(range(1, 51), 25)  # 25 números distintos
        return [numeros[i:i+5] for i in range(0, 25, 5)]  # Divide en filas de 5

    def mostrar_carton(self):
        """Muestra el cartón en pantalla"""
        for fila in self.carton:
            print(" ".join(f"{n:2}" for n in fila))
        print() #Salto de linea

    def jugar(self):
        # Se descuenta el costo del boleto
        resultado = self.usuario.comprar_boleto(self.costo_boleto)
        if "Fondos insuficientes" in resultado:  # Validación de saldo
            print(resultado)
            return

        print(f"\n🎉 {self.usuario.nombre} comienza a jugar Bingo!")
        self.mostrar_carton()

        # Se sortearán números hasta el límite de intentos
        numeros_sorteados = set()
        aciertos = 0

        for intento in range(1, self.max_sorteos + 1):
            numero = random.randint(1, 50)  # Número sorteado
            while numero in numeros_sorteados:  # Evitar repetidos
                numero = random.randint(1, 50)

            numeros_sorteados.add(numero)
            print(f"Sorteo {intento}: salió el {numero}")
            time.sleep(0.2)  # Simulación del sorteo

            # Verificar si el número está en el cartón
            for fila in self.carton:
                if numero in fila:
                    aciertos += 1
                    fila[fila.index(numero)] = "X"  # Marcar número acertado

            # Si se llenan los 25 casilleros → Gana
            if aciertos == 25:
                self.usuario.aumentar_dinero(self.premio)
                print(f"\n🏆 ¡Bingo completado! Ganaste ${self.premio}")
                print(self.usuario.mostrar_saldo())
                return
        print("\n😢 No lograste completar el cartón en los intentos dados.")
        self.mostrar_carton()
        