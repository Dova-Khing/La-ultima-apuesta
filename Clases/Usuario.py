class Usuario:
    """
    Representa a un jugador dentro del sistema de juegos.

    Atributos:
        nombre (str): Nombre del usuario.
        edad (str): Edad del usuario.
        __saldo (int): Dinero disponible en la cuenta del usuario.
        __boletos (int): Cantidad de boletos comprados por el usuario.
    """

    def __init__(self, nombre: str, edad: str, saldo_inicial: int = 0) -> None:
        """
        Inicializa un nuevo usuario con nombre, edad y saldo inicial.

        Args:
            nombre (str): Nombre del usuario.
            edad (str): Edad del usuario.
            saldo_inicial (int, opcional): Dinero inicial del usuario. Por defecto 0.
        """
        self.nombre = nombre
        self.edad = edad
        self.__saldo = saldo_inicial
        self.__boletos = 0

    def __str__(self) -> str:
        """
        Representación en texto del objeto Usuario.

        Returns:
            str: Información básica del usuario (nombre, edad, saldo y boletos).
        """
        return (
            f" Usuario: {self.nombre}\n"
            f" Edad: {self.edad} años\n"
            f" Saldo: ${self.__saldo}\n"
            f" Boletos: {self.__boletos}"
        )

    def aumentar_dinero(self, cantidad: int) -> str:
        """
        Incrementa el saldo del usuario en la cantidad especificada.

        Args:
            cantidad (int): Dinero a añadir al saldo del usuario.

        Returns:
            str: Mensaje con el resultado de la operación.
        """
        if cantidad > 0:
            self.__saldo += cantidad
            return f"Se han añadido ${cantidad}. Saldo actual: ${self.__saldo}"
        else:
            return "La cantidad debe ser positiva."

    def mostrar_saldo(self) -> str:
        """
        Muestra el saldo actual y la cantidad de boletos del usuario.

        Returns:
            str: Información sobre el saldo y boletos actuales.
        """
        return f"Saldo actual de {self.nombre}: ${self.__saldo} | Boletos: {self.__boletos}"

    def comprar_boleto(self, costo: int, cantidad: int = 1) -> str:
        """
        Permite al usuario comprar uno o varios boletos.

        Args:
            costo (int): Precio de un boleto.
            cantidad (int, opcional): Número de boletos a comprar. Por defecto 1.

        Returns:
            str: Mensaje indicando si la compra fue exitosa o fallida.
        """
        if costo <= 0 or cantidad <= 0:
            return "El costo y la cantidad deben ser mayores a 0."

        total = costo * cantidad
        if self.__saldo >= total:
            self.__saldo -= total
            self.__boletos += cantidad
            return (
                f"{self.nombre} compró {cantidad} boleto(s) por ${total}. "
                f"Saldo restante: ${self.__saldo} | Boletos: {self.__boletos}"
            )
        else:
            return "Fondos insuficientes para comprar los boletos."

    def usar_boleto(self, cantidad: int = 1) -> str:
        """
        Permite al usuario gastar boletos, por ejemplo, al participar en un juego.

        Args:
            cantidad (int, opcional): Número de boletos a usar. Por defecto 1.

        Returns:
            str: Mensaje indicando si la acción fue exitosa o no.
        """
        if cantidad <= 0:
            return "La cantidad debe ser mayor a 0."
        if self.__boletos >= cantidad:
            self.__boletos -= cantidad
            return f"{self.nombre} usó {cantidad} boleto(s). Boletos restantes: {self.__boletos}"
        else:
            return "No tienes suficientes boletos."
