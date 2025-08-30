# 🎲 Sistema de Lotería y Apuestas  

Este proyecto es una simulación de **juegos de azar en consola** desarrollada en **Python**.  
El usuario puede crear su cuenta ingresando **nombre, edad y saldo inicial** (con validaciones incluidas).  
Una vez creado, podrá jugar:  

- 🃏 **Bingo**  
- 🎰 **Ruleta**  
- 🎟️ **Lotería**  

Cada juego descuenta el costo correspondiente del saldo y entrega premios en caso de ganar.  

---

## 📌 Requisitos previos  
---
Antes de ejecutar el proyecto, asegúrate de tener instalado:  

- 🐍 **Python 3.8 o superior** → [Descargar aquí](https://www.python.org/downloads/)  
- **Git** (para clonar el repositorio) → [Descargar aquí](https://git-scm.com/downloads)  

> ✅ No necesitas instalar librerías externas, solo la **librería estándar de Python**.  

---

## 📥 Instalación y ejecución  

1. **Clonar el repositorio**  
```bash
git clone https://github.com/Dova-Khing/La-ultima-apuesta.git 
```

2. **Entrar en la carpeta del proyecto**
Para ejecutar esto necesitas abrir la consola de comandos del editor o del propio windows 
```bash
cd C:\Users\'Tu nombre de usuario'\La-ultima-apuesta
```

3. **Ejecutar el programa principal desde la consola:**
```bash
python main.py 
```
⚠️ Importante: este proyecto se ejecuta en consola/terminal. No es una aplicación gráfica.

## 🕹️ Cómo jugar

1. Ingresa tu **nombre**, **edad** y **saldo inicial**.
   - La edad debe ser **mayor a 18**.
   - El saldo debe ser **mayor a 0**.

2. Elige entre los juegos disponibles:

   - 🎲 **Bingo** → Se genera automáticamente un cartón y se sortean números hasta 30 intentos.  
   - 🎡 **Ruleta** → Apuesta a un número (0-36) o a un color (Rojo/Negro).  
     ⚠️ Si ingresas algo inválido, el sistema lo tomará como **Negro o 1**.  
   - 🎟️ **Lotería** → Compra boletos y participa en el sorteo.  

3. Resultados:
   - 🏆 **Si ganas**, tu saldo aumentará según el premio.  
   - ❌ **Si pierdes**, verás un mensaje y tu saldo se mantendrá o disminuirá.  