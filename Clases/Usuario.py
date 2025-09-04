class Usuario:
    def __init__(self, nombre: str, edad:str, saldo_inicial: int = 0):
        self.nombre = nombre
        self.edad = edad
        self.__saldo = saldo_inicial   #  dinero disponible
        self.__boletos = 0             #  boletos (se inicializa en 0)
     
     #Representacion del objeto
    def __str__(self):
           return (f" Usuario: {self.nombre}\n"
                f" Edad: {self.edad} años\n"
                f" Saldo: ${self.__saldo}\n"
                f" Boletos: {self.__boletos}")

    # --- Método que aumenta el dinero si se gana el premio ---
    def aumentar_dinero(self, cantidad: int):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Se han añadido ${cantidad}. Saldo actual: ${self.__saldo}"
        else:
            return "La cantidad debe ser positiva."
        
    # --- Método que muestra la cantidad de dinero obtenido ---
    def mostrar_saldo(self):
        return f"Saldo actual de {self.nombre}: ${self.__saldo} | Boletos: {self.__boletos}"

    # --- Método que permite la compra de boletos ---
    def comprar_boleto(self, costo: int, cantidad: int = 1):
        if costo <= 0 or cantidad <= 0:
            return "El costo y la cantidad deben ser mayores a 0."

        total = costo * cantidad
        if self.__saldo >= total:
            self.__saldo -= total
            self.__boletos += cantidad
            return (f"{self.nombre} compró {cantidad} boleto(s) por ${total}. "
                    f"Saldo restante: ${self.__saldo} | Boletos: {self.__boletos}")
        else:
            return "Fondos insuficientes para comprar los boletos."
    
    # --- Método para gastar boletos (ej. cuando se juega Bingo) ---
    def usar_boleto(self, cantidad: int = 1):
        if cantidad <= 0:
            return "La cantidad debe ser mayor a 0."
        if self.__boletos >= cantidad:
            self.__boletos -= cantidad
            return f"{self.nombre} usó {cantidad} boleto(s). Boletos restantes: {self.__boletos}"
        else:
            return "No tienes suficientes boletos."