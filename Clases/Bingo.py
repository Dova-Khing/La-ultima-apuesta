import random
import time
from Clases.Usuario import Usuario

class Bingo:
    def __init__(self, usuario: Usuario, costo_boleto=10, premio=150, max_sorteos=30)->None:
        self.usuario = usuario
        self.costo_boleto = costo_boleto
        self.premio = premio
        self.max_sorteos = max_sorteos
        self.carton = self.generar_carton()
        self.numeros_sorteados = set()
        self.juego_terminado = False

    def generar_carton(self)->list:
        """Genera un cartón 5x5 con números únicos del 1 al 50"""
        numeros = random.sample(range(1, 51), 25)
        return [numeros[i:i+5] for i in range(0, 25, 5)]

    def mostrar_carton(self)->None:
        print("\n--- CARTÓN DE BINGO ---")
        for fila in self.carton:
            print(" | ".join(f"{n:2}" for n in fila))
        print("-----------------------\n")

    def jugar(self)->None:
        # Cobrar boleto
        resultado = self.usuario.comprar_boleto(self.costo_boleto)
        if "Fondos insuficientes" in resultado:
            print(resultado)
            return

        print(f"\n {self.usuario.nombre} ha comenzado el Bingo 🎲")
        self.mostrar_carton()

        sorteos = 0

        while not self.juego_terminado and sorteos < self.max_sorteos:
            numero = self.sortear_numero()
            sorteos += 1
            print(f" Número sorteado: {numero}")
            time.sleep(0.5)

            if self.verificar_ganador():
                self.juego_terminado = True
                self.usuario.aumentar_dinero(self.premio)
                print(f"\n ¡Bingo! {self.usuario.nombre} completó el cartón en {sorteos} sorteos y gana ${self.premio}")
                print(self.usuario.mostrar_saldo())
                return

        # Si se acaban los sorteos y no completó el cartón
        if not self.juego_terminado:
            print("\n Se acabaron los intentos y no lograste completar el cartón.")

    def sortear_numero(self)->int|None:
        """Saca un número único del 1 al 50"""
        if len(self.numeros_sorteados) >= 50:
            self.juego_terminado = True
            return None

        numero = random.randint(1, 50)
        while numero in self.numeros_sorteados:
            numero = random.randint(1, 50)

        self.numeros_sorteados.add(numero)
        return numero

    def verificar_ganador(self)->bool:
        """Verifica si todos los números del cartón salieron"""
        return all(num in self.numeros_sorteados for fila in self.carton for num in fila)