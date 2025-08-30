import random
import time
from Clases.Usuario import Usuario

class Bingo:

    # Creacion de constructores 
    def _init_(self, usuario: Usuario, costo_boleto=10, premio=150, max_sorteos=30):
        self.usuario = usuario
        self.costo_boleto = costo_boleto
        self.premio = premio
        self.max_sorteos = max_sorteos
        self.carton = self.generar_carton()
        self.numeros_sorteados = set()
        self.juego_terminado = False

    def generar_carton(self):
        """Genera un cartón 5x5 con números únicos del 1 al 50"""
        numeros = random.sample(range(1, 51), 25) # Elige varios numeros random en una secuencia
        return [numeros[i:i+5] for i in range(0, 25, 5)] # Generacion de carton/matriz

    def mostrar_carton(self):
        """Muestra el cartón, marcando con X los números ya sorteados"""
        print("\n--- CARTÓN DE BINGO ---") # Muestra carton 
        for fila in self.carton:
            fila_marcada = [(" X" if n in self.numeros_sorteados else f"{n:2}") for n in fila]
            print(" | ".join(fila_marcada)) # Concatena elementos de una lista con el .join
        print("-----------------------\n")

    def jugar(self):
        # Cobrar boleto
        resultado = self.usuario.comprar_boleto(self.costo_boleto)
        if "Fondos insuficientes" in resultado:
            print(resultado)
            return

        print(f"\n🎲 {self.usuario.nombre} ha comenzado el Bingo 🎲") # Imprime 
        self.mostrar_carton()

        sorteos = 0

        while not self.juego_terminado and sorteos < self.max_sorteos: # Hasta que la secuencia no sea cumplida
            numero = self.sortear_numero()
            sorteos += 1
            print(f"➡ Número sorteado: {numero}")
            time.sleep(1)

            # Mostrar el cartón actualizado
            self.mostrar_carton() # self para especificar la variable de instancia / pertenece a un obj especifico

            if self.verificar_ganador():
                self.juego_terminado = True # se cumplio la condicion
                self.usuario.aumentar_dinero(self.premio)
                print(f"\n🏆 ¡Bingo! {self.usuario.nombre} completó el cartón en {sorteos} sorteos y gana ${self.premio}")
                print(self.usuario.mostrar_saldo())
                return

        # Si se acaban los sorteos y no completó el cartón
        if not self.juego_terminado:
            print("\n😢 Se acabaron los intentos y no lograste completar el cartón.")
            print("Así quedó tu cartón final:")
            self.mostrar_carton()

    def sortear_numero(self):
        """Saca un número único del 1 al 50"""
        if len(self.numeros_sorteados) >= 50:
            self.juego_terminado = True
            return None

        numero = random.randint(1, 50) # randomziar
        while numero in self.numeros_sorteados:
            numero = random.randint(1, 50) # raondomizar 

        self.numeros_sorteados.add(numero) # añadelo
        return numero

    def verificar_ganador(self):
        """Verifica si todos los números del cartón salieron"""
        return all(num in self.numeros_sorteados for fila in self.carton for num in fila)