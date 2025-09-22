from Clases.Usuario import Usuario
from Clases.Loteria import Loteria
from Clases.Ruleta import Ruleta
from Clases.Bingo import Bingo


class Validaciones:
    """
    Contiene métodos estáticos para validar datos de entrada del usuario.

    Los métodos piden datos por consola e implementan validaciones
    específicas para asegurar que sean correctos antes de retornarlos.
    """

    def validar_nombre() -> str:
        """
        Solicita y valida que el nombre contenga únicamente letras.

        Returns:
            str: Nombre capitalizado (primera letra en mayúscula).
        """
        nombre = input("Ingrese su nombre: ").strip()
        while not nombre.isalpha():
            print(" El nombre solo debe contener letras.")
            nombre = input("Ingrese su nombre: ").strip()
        return nombre.capitalize()

    def validar_edad() -> int:
        """
        Solicita y valida la edad del usuario.

        La edad debe ser un número entero entre 18 y 90 años.

        Returns:
            int: Edad validada del usuario.
        """
        edad_str = input("Ingrese su edad: ").strip()
        while not edad_str.isdigit() or not (17 < int(edad_str) <= 90):
            print(" Edad inválida. Debe ser mayor o tener 18 años y menor de 90")
            edad_str = input("Ingrese su edad: ").strip()
        return int(edad_str)

    def validar_saldo() -> float:
        """
        Solicita y valida el saldo inicial del usuario.

        El saldo debe ser un número positivo (entero o decimal).

        Returns:
            float: Saldo inicial validado.
        """
        saldo_str = input("Ingrese su saldo inicial : ").strip()
        while not saldo_str.replace(".", "", 1).isdigit() or float(saldo_str) < 0:
            print(" El saldo debe ser un número positivo.")
            saldo_str = input("Ingrese su saldo inicial : ").strip()
        return float(saldo_str)
