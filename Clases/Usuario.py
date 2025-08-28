class Usuario:
    def __init__(self, nombre, saldo_inicial:int=0):
        self.nombre = nombre
        self.__saldo = saldo_inicial   # privado
        self.__boletos = 0            # cantidad de boletos comprados

    # --- Método que aumenta el dinero si se gana el premio ---
    def aumentar_dinero(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Se han añadido ${cantidad}. Saldo actual: ${self.__saldo}"
        else:
            return "La cantidad debe ser positiva."
        
    # --- Método que muestra la cantidad de dinero obtenido ---
    def mostrar_saldo(self):
        return f"Saldo actual de {self.nombre}: ${self.__saldo}"

    # --- Método que permite la compra de boletos ---
    def comprar_boleto(self, costo, cantidad=1):
        if costo <= 0 or cantidad <= 0:
            return "El costo y la cantidad deben ser mayores a 0."

        total = costo * cantidad
        if self.__saldo >= total:
            self.__saldo -= total
            self.__boletos += cantidad
            return (f"{self.nombre} compró {cantidad} boleto(s) por ${total}. "
                    f"Saldo restante: ${self.__saldo}")
        else:
            return "Fondos insuficientes para comprar los boletos."
        
    # --- Método que muestra la cantidad de boletos para jugar ---
    def mostrar_boletos(self):
        return f"{self.nombre} tiene {self.__boletos} boleto(s)."
