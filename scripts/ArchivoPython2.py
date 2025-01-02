# 2. Operadores
    #2.1 Operadores Aritméticos:
    #2.2 Operadores de Comparación:
    #2.3 Operadores Logicos

#CONSTANTES de programa
ROJO = "\033[91m"  # Código ANSI para texto rojo
NEGRITA = "\033[1m" # Código ANSI para negrita
AZUL_CLARO = "\033[34m" #Este texto es de color azul claro"
AZUL_OSCURO = "\033[94m" #Este texto es de color azul oscuro"
AMARILLO = "\033[33m" #Este texto es de color amarillo"
AMARILLO_OSCURO = "\033[93m" #Este texto es de color amarillo oscuro"
VERDE = "\033[32m" #Este texto es de color verde"
VERDE_OSCURO = "\033[92m" #Este texto es de color verde oscuro"

CURSIVA = "\033[3m" # Código ANSI para cursiva
RESET = "\033[0m"   # Código ANSI para resetear el formato

"""
#2.1 Operadores Aritméticos:

+ (suma)
- (resta)
* (multiplicación)
/ (división)
// (división entera)
% (módulo o resto)
** (exponenciación)
"""



a = 10
b = 3
suma = a + b      # 13
resta = a - b     # 7
multiplicacion = a * b # 30
division = a / b    # 3.333...
division_entera = a // b # 3
modulo = a % b      # 1
potencia = a ** b    # 1000

#\033[1m: Es el código de escape ANSI para activar el modo de texto en negrita.
#\033[0m: Es el código de escape ANSI para restablecer el formato a normal (sin negrita). Es importante incluirlo para que el resto del texto no aparezca también en negrita.

# usando f-string
print("usando f-string")
print(f"Operadores Aritmeticos:")
print(f"{NEGRITA}La variable a = {RESET} {ROJO} {a} {RESET} {NEGRITA}la variable b = :{ROJO} {b} {RESET}")
print(f"{NEGRITA}La suma = a + b: {ROJO}{suma}{RESET}")
print(f"La resta = a - b: {resta}")
print(f"La multiplicacion = a * b: {multiplicacion}")
print(f"La division = a / b: {division}")
print(f"La division_entera = a // b: {division_entera}")
print(f"El modulo = a % b: {modulo}")
print(f"La potencia = a ** b: {potencia}")

"""
2.2 Operadores de Comparación:

== (igual a)
!= (no igual a)
> (mayor que)
< (menor que)
>= (mayor o igual que)
<= (menor o igual que)
"""
x = 5
y = 10
x == y  # False
x != y  # True
x < y   # True

print("")
print("Operadores de Comparacion:")
print(f"La variable x = : {x} la variable y = :{y}")
print(f"Comparar x == y: {x == y}")
print(f"Comparar x != y: {x != y}")
print(f"Comparar x < y: {x < y}")


"""
2.3 Lógicos:

and (y lógico): Devuelve True si ambas condiciones son verdaderas.
or (o lógico): Devuelve True si al menos una condición es verdadera.
not (no lógico): Niega una condición.

"""

edad = 20
es_estudiante = True
evaluacion1 = edad >= 18 and es_estudiante  # True
evaluacion2 = edad < 18 or es_estudiante   # True
evaluacion3 = not es_estudiante           # False

print("")
print("Operadores Logico:")
print(f"La variable edad = {edad} y la variable es_estudiante = {es_estudiante}")
print(f"Al evaluar la expresion edad >= 18 and es_estudiante el resultado es:  {evaluacion1}")
print(f"Al evaluar la expresion edad < 18 or es_estudiante el resultado es:  {evaluacion2}")
print(f"Al evaluar la expresion not es_estudiante el resultado es:  {evaluacion3}")