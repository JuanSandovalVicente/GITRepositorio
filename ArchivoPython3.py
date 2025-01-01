#3. Estructuras de Control

"""
Condicionales (if, elif, else): Permiten ejecutar diferentes bloques de código según se cumplan 
        o no ciertas condiciones.
"""
print("")
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


edad = 18
resultado = ""
if edad >= 18:
    resultado = "Eres mayor de edad."
elif edad >= 13:
    resultado = "Eres adolescente."
else:
    resultado = "Eres menor de edad."

print("")
print("Estructuras de Control")
print("")
print("Condicionales (if, elif, else)")
print(f"La variable a evaluar \033[1medad\033[0m tiene un valor de {edad}")
print(f"El resultado de la evaluacion es {NEGRITA}{VERDE_OSCURO}{resultado}{RESET}")


"""
Bucles (for, while): Permiten repetir un bloque de código múltiples veces.
"""

# for: Itera sobre una secuencia (como una lista, cadena o rango).
print("")
print("for: Itera sobre una secuencia (como una lista, cadena o rango).")
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(f"La fruta es: {NEGRITA}{fruta}{RESET}")

print("")
print("for: Itera sobre una secuencia rango. Imprime cada numero en una fila")
for i in range(5): #recorre del 0 al 4
    print(i)


print("")
print("for: Itera sobre una secuencia rango. Imprime todos los numeros en una sola fila")
cadena=""
for i in range(5): #recorre del 0 al 4
    cadena = cadena + str(i)
print (f"Despues del for queda la variable cadena asi: {cadena}")

cadena = " ".join(str(cadena))
print (f"Usando la funcion de texto .join, agregamos un espacio en blanco por cada caracter de Cadena {cadena}")

mi_lista = [1, 2, 3, 4, 5]
cadena = " ".join(str(elemento) for elemento in mi_lista)
print(cadena)


#while: Repite un bloque de código mientras se cumpla una condición.
print("")
print("while: Repite un bloque de código mientras se cumpla una condición.")

contador = 0
while contador < 5:
    print(contador)
    contador += 1 #equivale a contador = contador + 1