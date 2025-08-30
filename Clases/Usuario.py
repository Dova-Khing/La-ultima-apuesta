class Usuario:
    def __init__(self, nombre: str, edad:str, saldo_inicial: int = 0):
        self.nombre = nombre           # Nombre del usuario en concreto
        self.edad = edad               # Edad
        self.__saldo = saldo_inicial   # 💰 dinero disponible
        self.__boletos = 0             # 🎟️ boletos (se inicializa en 0)
     
     #Representacion del objeto
    def __str__(self):
           return (f"👤 Usuario: {self.nombre}\n" # Muestra el nombre del jugador
                f"🎂 Edad: {self.edad} años\n"    # Muestra la edad del jugador
                f"💰 Saldo: ${self.__saldo}\n"    # muestra el saldo del jugador
                f"🎟️ Boletos: {self.__boletos}")  # muestra los boletos del jugador

    # --- Método que aumenta el dinero si se gana el premio ---
    def aumentar_dinero(self, cantidad: int):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Se han añadido ${cantidad}. Saldo actual: ${self.__saldo}" # Se añade la cantidad de saldo correspondiente
        else:
            return "La cantidad debe ser positiva." # Indica que la cantidad debe ser positiva
        
    # --- Método que muestra la cantidad de dinero obtenido ---
    def mostrar_saldo(self): 
        return f"Saldo actual de {self.nombre}: ${self.__saldo} | Boletos: {self.__boletos}" # Retorna mensaje concadenado del saldo actual con el nombre y boletos

    # --- Método que permite la compra de boletos ---
    def comprar_boleto(self, costo: int, cantidad: int = 1):
        if costo <= 0 or cantidad <= 0:
            return "El costo y la cantidad deben ser mayores a 0."

        total = costo * cantidad # para el total multiplica el costo por la cantidad de boletos comprados
        if self.__saldo >= total:
            self.__saldo -= total
            self.__boletos += cantidad
            return (f"{self.nombre} compró {cantidad} boleto(s) por ${total}. " # retorna la persona la cantidad de boletos que compro
                    f"Saldo restante: ${self.__saldo} | Boletos: {self.__boletos}") # muestra de manera especifica el saldo restante junto con los boletos
        else:
            return "Fondos insuficientes para comprar los boletos." # si no se cumplen las condiciones retorna el mensaje de indicativo.
    
