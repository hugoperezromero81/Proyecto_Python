# Ejercicio 1:
# Escribe una función que reciba una cadena de texto como parámetro 
# y devuelva un diccionario con las frecuencias de cada letra en la cadena.
# Los espacios no deben ser considerados.

def contar_frecuencias(texto):
    frecuencias = {}
    for letra in texto:
        if letra != " ":
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    return frecuencias

# Ejemplo:
print(contar_frecuencias("primer ejercicio"))  # {'h': 1, 'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}


# Ejercicio 2:
# Dada una lista de números, obtén una nueva lista con el doble de cada valor.
# Usa la función map()

numeros = [1, 2, 3, 4, 5]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  # [2, 4, 6, 8, 10]


# Ejercicio 3:
# Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros.
# La función debe devolver una lista con todas las palabras de la lista original
# que contengan la palabra objetivo.

def filtrar_palabras(lista_palabras, palabra_objetivo):
    return [palabra for palabra in lista_palabras if palabra_objetivo in palabra]

# Ejemplo:
palabras = ["manzana", "banana", "naranja", "pan", "mana"]
resultado = filtrar_palabras(palabras, "ana")
print(resultado)


# Ejercicio 4:
# Genera una función que calcule la diferencia entre los valores de dos listas.
# Usa la función map()

def diferencia_listas(lista1, lista2):
    return list(map(lambda x, y: x - y, lista1, lista2))

# Ejemplo:
lista_a = [10, 20, 30]
lista_b = [1, 5, 10]
resultado_diferencia = diferencia_listas(lista_a, lista_b)
print(resultado_diferencia)


# Ejercicio 5:
# Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado,
# que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es
# mayor o igual que nota_aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso".
# La función debe devolver una tupla que contenga la media y el estado.

def evaluar_nota(lista_numeros, nota_aprobado=5):
    if not lista_numeros:
        return (0, "sin datos")
    media = sum(lista_numeros) / len(lista_numeros)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return (media, estado)

# Ejemplo:
notas = [4, 5, 6, 7]
resultado_evaluacion = evaluar_nota(notas)
print(resultado_evaluacion)


# Ejercicio 6:
# Escribe una función que calcule el factorial de un número de manera recursiva.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Ejemplo:
print(factorial(5))


# Ejercicio 7:
# Genera una función que convierta una lista de tuplas a una lista de strings.
# Usa la función map()

def tuplas_a_strings(lista_tuplas):
    return list(map(lambda t: " ".join(map(str, t)), lista_tuplas))

# Ejemplo:
tuplas = [(1, 2), (3, 4), ("a", "b")]
resultado_strings = tuplas_a_strings(tuplas)
print(resultado_strings)


# Ejercicio 8:
# Escribe un programa que pida al usuario dos números e intente dividirlos.
# Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada.
# Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no.

def dividir_usuarios():
    try:
        a = float(input("Introduce el primer número: "))
        b = float(input("Introduce el segundo número: "))
        resultado = a / b
        print(f"Resultado: {resultado}")
    except ValueError:
        print("Error: Debes introducir valores numéricos.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    else:
        print("División realizada con éxito.")

# Ejemplo para comprobar resultado:
dividir_usuarios()


# Ejercicio 9:
# Escribe una función que tome una lista de nombres de mascotas como parámetro
# y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España.
# La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].
# Usa la función filter()

def filtrar_mascotas(mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, mascotas))

# Ejemplo:
lista_mascotas = ["Perro", "Gato", "Mapache", "Cocodrilo", "Conejo"]
mascotas_validas = filtrar_mascotas(lista_mascotas)
print(mascotas_validas)


# Ejercicio 10:
# Escribe una función que reciba una lista de números y calcule su promedio.
# Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

def calcular_promedio(lista):
    try:
        if not lista:
            raise ValueError("La lista está vacía, no se puede calcular el promedio.")
        promedio = sum(lista) / len(lista)
        return promedio
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Ejemplo:
print(calcular_promedio([4, 6, 8]))
print(calcular_promedio([]))     


# Ejercicio 11:
# Escribe un programa que pida al usuario que introduzca su edad.
# Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado
# (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")
        print(f"Tu edad es {edad}.")
    except ValueError as e:
        print(f"Error: {e}")

# Ejemplo:
pedir_edad()


# Ejercicio 12:
# Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra.
# Usa la función map()

def longitudes_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

# Ejemplo:
frase_ejemplo = "Asturias Patria Querida"
resultado_longitudes = longitudes_palabras(frase_ejemplo)
print(resultado_longitudes)

# Ejercicio 13:
# Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas
# con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas.
# Usa la función map()

def letras_mayus_minus(caracteres):
    unicas = set(caracteres)
    return list(map(lambda c: (c.upper(), c.lower()), unicas))

# Ejemplo:
print(letras_mayus_minus("Oviedo"))


# Ejercicio 14:
# Crea una función que retorne las palabras de una lista de palabras que comience con una letra en específico.
# Usa la función filter()

def palabras_por_letra(lista_palabras, letra):
    return list(filter(lambda palabra: palabra.startswith(letra), lista_palabras))

# Ejemplo:
palabras = ["gato", "perro", "conejo", "loro"]
print(palabras_por_letra(palabras, "g"))


# Ejercicio 15:
# Crea una función lambda que sume 3 a cada número de una lista dada.

numeros = [1, 2, 3, 4, 5]
sumados = list(map(lambda x: x + 3, numeros))
print(sumados)


# Ejercicio 16:
# Escribe una función que tome una cadena de texto y un número entero n como parámetros
# y devuelva una lista de todas las palabras que sean más largas que n.
# Usa la función filter()

def palabras_largas(cadena, n):
    palabras = cadena.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))

# Ejemplo:
frase = "Real Oviedo equipo de primera división"
print(palabras_largas(frase, 6))


# Ejercicio 17:
# Crea una función que tome una lista de dígitos y devuelva el número correspondiente.
# Por ejemplo, [5,7,2] corresponde al número 572.
# Usa la función reduce()

from functools import reduce

def lista_a_numero(digitos):
    return reduce(lambda x, y: x * 10 + y, digitos)

# Ejemplo:
print(lista_a_numero([5, 7, 2]))


# Ejercicio 18:
# Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes
# (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 90.
# Usa la función filter()

estudiantes = [
    {"nombre": "Hugo", "edad": 20, "calificacion": 95},
    {"nombre": "Servan", "edad": 22, "calificacion": 88},
    {"nombre": "Cati", "edad": 21, "calificacion": 91},
    {"nombre": "Maribel", "edad": 23, "calificacion": 84},
]

excelentes = list(filter(lambda est: est["calificacion"] >= 90, estudiantes))
print(excelentes)


# Ejercicio 19:
# Crea una función lambda que filtre los números impares de una lista dada.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
impares = list(filter(lambda x: x % 2 != 0, numeros))
print(impares)


# Ejercicio 20:
# Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int.
# Usa la función filter()

elementos = [1, "dos", 3, "cuatro", 5, 6, "siete"]
solo_enteros = list(filter(lambda x: isinstance(x, int), elementos))
print(solo_enteros)


# Ejercicio 21:
# Crea una función que calcule el cubo de un número dado mediante una función lambda

cubo = lambda x: x ** 3
print(cubo(3))


# Ejercicio 22:
# Dada una lista numérica, obtén el producto total de los valores de dicha lista.
# Usa la función reduce()

from functools import reduce

numeros = [1, 2, 3, 4, 5]
producto_total = reduce(lambda x, y: x * y, numeros)
print(producto_total)


# Ejercicio 23:
# Concatena una lista de palabras.
# Usa la función reduce()

palabras = ["trabajando", "en", "este", "proyecto", "de", "Python"]
frase = reduce(lambda x, y: x + " " + y, palabras)
print(frase)


# Ejercicio 24:
# Calcula la diferencia total en los valores de una lista.
# Usa la función reduce()

numeros = [100, 20, 5]
diferencia_total = reduce(lambda x, y: x - y, numeros)
print(diferencia_total)


# Ejercicio 25:
# Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(cadena):
    return len(cadena)

# Ejemplo:
print(contar_caracteres("Oviedo es azul"))


# Ejercicio 26:
# Crea una función lambda que calcule el resto de la división entre dos números dados.

resto = lambda x, y: x % y
print(resto(10, 3))


# Ejercicio 27:
# Crea una función que calcule el promedio de una lista de números.

def calcular_promedio(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

# Ejemplo:
print(calcular_promedio([10, 20, 30]))


# Ejercicio 28:
# Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_duplicado(lista):
    vistos = set()
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None

# Ejemplo:
print(primer_duplicado([1, 2, 3, 2, 5]))


# Ejercicio 29:
# Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres
# con el carácter '#', excepto los últimos cuatro.

def enmascarar_variable(variable):
    texto = str(variable)
    if len(texto) <= 4:
        return texto
    return '#' * (len(texto) - 4) + texto[-4:]

# Ejemplo:
print(enmascarar_variable(123456789))


# Ejercicio 30:
# Crea una función que determine si dos palabras son anagramas, es decir,
# si están formadas por las mismas letras pero en diferente orden.

def son_anagramas(palabra1, palabra2):
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

# Ejemplo:
print(son_anagramas("Roma", "Amor"))


# Ejercicio 31:
# Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en
# esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se
# lanza una excepción.

def buscar_nombre():
    try:
        nombres = input("Introduce una lista de nombres separados por comas: ").split(',')
        nombres = [nombre.strip() for nombre in nombres]
        nombre_a_buscar = input("Introduce el nombre a buscar: ").strip()
        if nombre_a_buscar in nombres:
            print(f"{nombre_a_buscar} ha sido encontrado en la lista.")
        else:
            raise ValueError("El nombre no se encuentra en la lista.")
    except ValueError as e:
        print(e)

# Ejemplo
buscar_nombre()


# Ejercicio 32:
# Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y
# devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona
# no trabaja aquí.

def buscar_empleado(nombre_completo, empleados):
    for empleado in empleados:
        if empleado['nombre'].lower() == nombre_completo.lower():
            return f"{nombre_completo} trabaja como {empleado['puesto']}"
    return f"{nombre_completo} no trabaja aquí"

# Ejemplo:
empleados = [
    {'nombre': 'Hugo Pérez', 'puesto': 'Ingeniero'},
    {'nombre': 'Cati Martiño', 'puesto': 'Diseñadora'},
    {'nombre': 'Isabel Romero', 'puesto': 'Analista'}
]

print(buscar_empleado("Cati Martiño", empleados))
print(buscar_empleado("Ana López", empleados))


# Ejercicio 33:
# Crea una función lambda que sume elementos correspondientes de dos listas dadas.

sumar_listas = lambda lista1, lista2: list(map(lambda x, y: x + y, lista1, lista2))

# Ejemplo:
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print(sumar_listas(lista1, lista2))


# Ejercicio 34:
# Crea la clase Arbol, define un árbol genérico con un tronco y ramas como atributos.
# Métodos: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol

class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            del self.ramas[posicion]
        else:
            print("Posición inválida para eliminar rama.")

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

# Caso de uso:
arbol = Arbol()               # Crear un árbol
arbol.crecer_tronco()         # Hacer crecer el tronco una unidad
arbol.nueva_rama()            # Añadir una nueva rama
arbol.crecer_ramas()          # Hacer crecer todas las ramas una unidad
arbol.nueva_rama()            # Añadir una nueva rama
arbol.nueva_rama()            # Añadir otra nueva rama
arbol.quitar_rama(2)          # Eliminar la rama situada en la posición 2
print(arbol.info_arbol())     # Obtener información del árbol


# Nota: En el PDF del proyecto no se encuentra el ejercicio 35.


# Ejercicio 36:
# Crea la clase UsuarioBanco para representar a un usuario con nombre, saldo y cuenta corriente.
# Métodos: retirar_dinero, transferir_dinero, agregar_dinero

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente=True):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente para retirar dinero.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if cantidad > otro_usuario.saldo:
            raise ValueError(f"{otro_usuario.nombre} no tiene suficiente saldo para transferir.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

# Caso de uso:
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

bob.agregar_dinero(20)                # Bob agrega 20 unidades
alicia.transferir_dinero(bob, 80)     # Bob transfiere 80 a Alicia
alicia.retirar_dinero(50)             # Alicia retira 50 unidades

print(f"Saldo final de Alicia: {alicia.saldo}")
print(f"Saldo final de Bob: {bob.saldo}")


# Ejercicio 37:
# Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras,
# reemplazar_palabras, eliminar_palabra. Estas opciones son otras funciones que tenemos que definir primero
# y llamar dentro de la función procesar_texto.

from collections import Counter

def contar_palabras(texto):
    palabras = texto.lower().split()
    return dict(Counter(palabras))

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p != palabra]
    return ' '.join(palabras_filtradas)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar" and len(args) == 2:
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar" and len(args) == 1:
        return eliminar_palabra(texto, args[0])
    else:
        return "Opción no válida o argumentos insuficientes."

# Caso de uso:
texto_prueba = "el Real Oviedo es un gran equipo y el Real Oviedo juega bien"
print(procesar_texto(texto_prueba, "contar"))
print(procesar_texto(texto_prueba, "reemplazar", "Oviedo", "Sporting"))
print(procesar_texto(texto_prueba, "eliminar", "Real"))


# Ejercicio 38:
# Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.

def momento_del_dia(hora):
    if 6 <= hora < 12:
        return "Es de día"
    elif 12 <= hora < 20:
        return "Es tarde"
    else:
        return "Es de noche"

# Ejemplo:
hora_usuario = 15
print(momento_del_dia(hora_usuario))


# Ejercicio 39:
# Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica.

def calificacion_texto(nota):
    if 0 <= nota <= 69:
        return "insuficiente"
    elif 70 <= nota <= 79:
        return "bien"
    elif 80 <= nota <= 89:
        return "muy bien"
    elif 90 <= nota <= 100:
        return "excelente"
    else:
        return "Nota fuera de rango"

# Ejemplo:
nota_alumno = 85
print(calificacion_texto(nota_alumno))


# Ejercicio 40:
# Escribe una función que tome dos parámetros: figura (cadena: "rectangulo", "circulo" o "triangulo") y
# datos (una tupla con los datos necesarios para calcular el área de la figura).
import math

def calcular_area(figura, datos):
    if figura == "rectangulo" and len(datos) == 2:
        base, altura = datos
        return base * altura
    elif figura == "circulo" and len(datos) == 1:
        radio = datos[0]
        return math.pi * radio ** 2
    elif figura == "triangulo" and len(datos) == 2:
        base, altura = datos
        return (base * altura) / 2
    else:
        return "Datos incorrectos o figura no reconocida"

# Ejemplos de uso:
print(calcular_area("rectangulo", (5, 10)))
print(calcular_area("circulo", (7,)))
print(calcular_area("triangulo", (6, 4)))


# Ejercicio 41:
# Programa que determina el precio final de una compra tras aplicar un descuento si se tiene cupón.

def aplicar_descuento():
    precio_original = float(input("Introduce el precio original del artículo: "))
    tiene_cupon = input("¿Tienes un cupón de descuento? (sí/no): ").lower()

    if tiene_cupon == "sí" or tiene_cupon == "si":
        valor_cupon = float(input("Introduce el valor del cupón: "))
        if valor_cupon > 0:
            precio_final = precio_original - valor_cupon
        else:
            print("El valor del cupón no es válido. Se aplicará el precio original.")
            precio_final = precio_original
    else:
        precio_final = precio_original

    print(f"El precio final de la compra es: {precio_final:.2f} €")

#Ejemplo:
aplicar_descuento()
