# Importo datetime para manejar las fechas de nacimiento
from datetime import datetime, date
#Importo usuario 
from Clases.Usuario import Usuario # Importa clase usuario
from Clases.Loteria import Loteria # Importa clase loteria
from Clases.Ruleta import Ruleta   # Importa clase Ruleta
from Clases.Bingo import Bingo     # Importa clase Bingo

def mostrar_menu()->None:

  print("""
===========================================
   ♠️🎰  MENÚ DEL LA ULTIMA APUESTA 🎰♠️
===========================================
1. Jugar Lotería
2. Jugar Ruleta
3. Jugar Bingo
4. Ver datos del usuario
5. Salir
""")



# Solicita los datos al jugador y devuelve una instancia de usuario
def registrar_Usuario() -> Usuario:  # retorna un objeto Usuario
    print("""
    ====================================
    [ INGRESE SUS DATOS POR FAVOR 🐉 ]      
    ====================================            
    """)

    nombre: str = input("Ingrese su Nombre: ").strip() # Elimina espacios en blanco saltos de linea 
    edad: int = int(input("Ingrese su Edad: ").strip()) # Elimina espacios en blanco saltos de linea 

    fecha_nacimiento_str: str = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ").strip()
    # Convertimos el dato a tipo de dato datetime
    fecha_nacimiento: date = datetime.strptime(fecha_nacimiento_str, "%Y-%m-%d").date()

    # Se construye instancia de Usuario
    jugador: Usuario = Usuario(nombre, edad, fecha_nacimiento)
    
    return jugador   

def main()->None:
    # Empezamos con registro de Usuario
    print("""
=============================================
   ♠️🎰 BIENVENIDO A LA ULTIMA APUESTA🎰♠️
=============================================
    """)

# Se registra al jugador antes de jugar
jugador:Usuario=registrar_Usuario()

print("\n=== Usuario registrado con éxito ===")

print(jugador)


#--Flujo del Menu Principal--#

while True:
   mostrar_menu()
   opcion:str=input("Ingrese una Opcion:")

   if opcion=="1":
      Loteria().jugar()
      
   elif opcion== "2":
      Ruleta().jugar()

#Opcion 3 activara el Bingo
   elif opcion == "3":
      Bingo().jugar()

#Opcion 4 mostrara los datos que el usuario ingreso
   elif opcion == "4":
      print("\n== DATOS DEL USUARIO ==")
      print(jugador)

#{usamos corchetes para insertar la variable exacta que quiero mostrar}
   elif opcion == "5":
         print(" ! Hasta Pronto !, Gracias por jugar {jugador.nombre} ")
         break
   
   #Si la opcion seleccionada es diferente de 5
   else:
      print ("✖️OPCION INVALIDA, INTENTE NUEVAMENTE✖️")

main()