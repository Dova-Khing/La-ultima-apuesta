# Importo clases
from Clases.Usuario import Usuario  # Importa clase Usuario
from Clases.Loteria import Loteria  # Importa clase Loteria
from Clases.Ruleta import Ruleta  # Importa clase Ruleta
from Clases.Bingo import Bingo  # Importa clase Bingo


class Validaciones:

    def validar_nombre() -> str:
        nombre = input("Ingrese su nombre: ").strip()
        while not nombre.isalpha():  # Solo letras
            print(" El nombre solo debe contener letras.")
            nombre = input("Ingrese su nombre: ").strip()
        return nombre.capitalize()

    def validar_edad() -> int:
        edad_str = input("Ingrese su edad: ").strip()
        # La edad tiene que estar entre 18 o 90
        while not edad_str.isdigit() or not (17 < int(edad_str) <= 90):
            print(" Edad inválida. Debe ser mayor o tener 18 años y menor de 90")
            edad_str = input("Ingrese su edad: ").strip()
            # retorna la edad
        return int(edad_str)

    def validar_saldo() -> float:
        saldo_str = input("Ingrese su saldo inicial : ").strip()
        # El saldo no puede estar vacio, debe ser un digito y no puede ser menor a 0
        while not saldo_str.replace(".", "", 1).isdigit() or float(saldo_str) < 0:
            print(" El saldo debe ser un número positivo.")
            saldo_str = input("Ingrese su saldo inicial : ").strip()
            # retorna el saldo
        return float(saldo_str)
