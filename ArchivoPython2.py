# 2. Operadores
    #2.1 Operadores Aritméticos:
    #2.2 Operadores de Comparación:
    #2.3 Operadores Logicos
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

# usando f-string
print("usando f-string")
print(f"Operadores Aritméticos:")
print(f"La variable a = : {a} la variable b = :{b}")
print(f"La suma = a + b: {suma}")
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
print("Operadores de Comparación:")
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