# FUNCIONS

# Definición y llamada de funciones

# Para definir una función en Python, utilizamos la palabra clave def seguida del
# nombre de la función y paréntesis. Opcionalmente, podemos especificar parámetros
# dentro de los paréntesis. El bloque de código de la función se indenta después
# de los dos puntos.

def saludo():
    print("¡Hola, mundo!")

# Para llamar a una función, simplemente escribimos el nombre
# de la función seguido de paréntesis:

saludo()  # Imprime "¡Hola, mundo!"


# Parámetros y argumentos

# Las funciones pueden aceptar parámetros, que son valores que se pasan a la función
# cuando se la llama. Los parámetros se especifican dentro de los paréntesis en la
# definición de la función.

def saludo1(nombre):
    print(f"¡Hola, {nombre}!")

# Al llamar a la función, proporcionamos los argumentos correspondientes a los parámetros:

saludo1("Juan")  # Imprime "¡Hola, Juan!"
saludo1("María")  # Imprime "¡Hola, María!"


# Valores de retorno

# Las funciones pueden devolver valores utilizando la palabra clave return.
# El valor de retorno puede ser utilizado por el código que llama a la función.

def suma(a, b):
    return a + b

resultado = suma(3, 4)
print(resultado)  # Imprime 7


# Funciones anónimas (lambda)

# Python permite crear funciones anónimas o funciones lambda, que son funciones
# sin nombre definidas en una sola línea. Se utilizan comúnmente para funciones
# pequeñas y concisas.

cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime 25


# Alcance de las variables (local vs. global)

# Las variables definidas dentro de una función tienen un alcance local,
# lo que significa que solo son accesibles dentro de la función. Por otro lado,
# las variables definidas fuera de cualquier función tienen un alcance global
# y pueden ser accedidas desde cualquier parte del programa.

def funcion():
    variable_local = 10
    print(variable_local)  # Accesible dentro de la función

variable_global = 20

def funcion2():
    print(variable_global)  # Accesible desde cualquier lugar

funcion()  # Imprime 10
funcion2()  # Imprime 20
print(variable_global)  # Imprime 20
print(variable_local)  # Genera un error, la variable no está definida en este alcance.


# Funciones definidas por el usuario
# Documentación de funciones (docstrings)

# Es una buena práctica documentar nuestras funciones utilizando docstrings.
# Los docstrings son cadenas de texto que describen el propósito, los parámetros
# y el valor de retorno de una función. Se colocan inmediatamente después de
# la definición de la función y se encierran entre triples comillas dobles.

def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.

    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.

    Returns:
        float: El área del rectángulo.
    """
    return base * altura


# Funciones con número variable de argumentos

# Python permite definir funciones que acepten un número variable de argumentos.
# Esto se logra utilizando el operador * antes del nombre del parámetro.

def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(suma_variable(1, 2, 3))  # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22


# MANEJO DE ERRORES Y EXCEPCIONES
# Errores comunes en Python

# Error de sintaxis (SyntaxError)
# Ocurre cuando el código no sigue las reglas de sintaxis de Python, como olvidar
# dos puntos después de una declaración de función o un bucle.
def mi_funcion() # Falta los dos puntos
    print("Hola")


# Error de nombre (NameError)
# Ocurre cuando se hace referencia a una variable o función que no ha sido definida.
print(variable_no_definida)


# Error de tipo (TypeError)
# Ocurre cuando se realiza una operación con tipos de datos incompatibles,
# como intentar sumar un número y una cadena.
resultado = 5 + "10"


# Error de índice (IndexError)
# Ocurre cuando se intenta acceder a un índice fuera del rango
# válido de una lista o secuencia.
lista = [1, 2, 3]
print(lista[3])  # El índice 3 está fuera del rango


# MANEJO DE EXCEPCIONES

# Try

# El bloque try contiene el código que puede generar una excepción.
# Si ocurre una excepción dentro del bloque try, el flujo de ejecución se
# transfiere al bloque except correspondiente.

try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")


# Except

# El bloque except especifica el tipo de excepción que se desea capturar y manejar.
# Puedes tener múltiples bloques except para manejar diferentes tipos de excepciones.

try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")


# Finally

# El bloque finally es opcional y se ejecuta siempre, independientemente de si
# ocurrió una excepción o no. Se utiliza comúnmente para realizar tareas de
# limpieza o liberación de recursos.

try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción


# LECTURA Y ESCRITURA DE ARCHIVOS

# Python nos permite leer y escribir datos en archivos externos. Podemos abrir
# archivos en diferentes modos, como lectura ("r"), escritura ("w") o anexar ("a"),
# y realizar operaciones de lectura y escritura.

# Lectura de archivos

# Para leer el contenido de un archivo, primero debemos abrirlo utilizando la
# función open() en modo de lectura ("r"). Luego, podemos leer el contenido
# del archivo utilizando métodos como read() o readlines().

archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

# En este ejemplo, se abre el archivo "datos.txt" en modo de lectura utilizando open().
# Luego, se lee todo el contenido del archivo utilizando el método read() y se
# almacena en la variable contenido. Finalmente, se muestra el contenido en la
# pantalla y se cierra el archivo utilizando el método close().


# Escritura de archivos

# Para escribir datos en un archivo, lo abrimos en modo de escritura ("w")
# utilizando la función open(). Si el archivo no existe, se creará automáticamente.
# Si el archivo ya existe, su contenido se sobrescribirá.

archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()
# Es importante cerrar siempre los archivos después de utilizarlos para
# liberar los recursos del sistema.

# IMPORTACIÓN Y CREACIÓN DE MÓDULOS
# Funciones y clases de módulos estándar

# La biblioteca estándar de Python ofrece una amplia gama de módulos con funciones
# y clases útiles. Algunos ejemplos comunes incluyen:

# Math --- Proporciona funciones matemáticas, como sqrt() (raíz cuadrada),
# sin() (seno), cos() (coseno), entre otras.
# Random --- Ofrece funciones para generar números aleatorios, como random()
# (número aleatorio entre 0 y 1), randint() (número entero aleatorio en un rango), entre otras.
# Datetime --- Permite trabajar con fechas y horas, como datetime.now()
# (fecha y hora actual), datetime.date() (fecha), datetime.time() (hora), entre otras.

import random
import datetime

numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10

fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual

# CREACIÓN DE MÓDULOS PROPIOS
# Crear y utilizar módulos personalizados

# Para crear un módulo personalizado, simplemente creamos un nuevo archivo Python
# con el nombre deseado y definimos las funciones, clases y variables que queremos
# incluir en el módulo. Por ejemplo, creamos un archivo (en el mismo directorio
# donde estamos ejecutando Python) llamado mi_modulo.py con el siguiente contenido:

#mi_modulo.py
def saludar(nombre):
    print(f"Hola, {nombre}!")
def calcular_suma(a, b):
    return a + b

# Luego, podemos importar y utilizar las funciones definidas en mi_modulo.py
# en otro archivo Python. En este ejemplo, se importa el módulo mi_modulo y se
# utilizan las funciones saludar() y calcular_suma() definidas en él.

import mi_modulo

mi_modulo.saludar("Juan")  # Imprime "Hola, Juan!"
resultado = mi_modulo.calcular_suma(5, 3)
print(resultado)  # Imprime 8

# Organización del código en módulos

# A medida que nuestros programas crecen en tamaño y complejidad, es una buena
# práctica organizar nuestro código en módulos separados según su funcionalidad.
# Esto nos permite conservar un código más legible, agrupado en módulos y fácil
# de mantener.
# Por ejemplo, podemos tener un módulo operaciones.py que contenga
# funciones relacionadas con operaciones matemáticas, y otro módulo utilidades.py
# que contenga funciones de uso general.

# operaciones.py
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

# utilidades.py
def imprimir_mensaje(mensaje):
    print(mensaje)

def obtener_nombre_usuario():
    return input("Ingresa tu nombre: ")

# Luego, podemos importar y utilizar estas funciones en nuestro programa principal.

import operaciones
import utilidades

resultado = operaciones.sumar(5, 3)
utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")

nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f"Hola, {nombre}!")

# PAQUETES

# Un paquete es una forma de organizar módulos relacionados en una estructura
# jerárquica de directorios. Los paquetes nos permiten agrupar módulos relacionados
# y evitar conflictos de nombres entre módulos.

# Crear y utilizar paquetes

# Para crear un paquete, creamos un directorio con el nombre deseado y agregamos
# un archivo especial llamado __init__.py dentro del directorio. Este archivo puede
# estar vacío o contener código de inicialización del paquete.
# Por ejemplo, creamos un directorio llamado mi_paquete con la siguiente estructura:

mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py

# Luego, podemos importar y utilizar los módulos del paquete en nuestro programa.

from mi_paquete import modulo1, modulo2

modulo1.funcion1()
modulo2.funcion2()

# En este ejemplo, se importan los módulos modulo1 y modulo2 del paquete mi_paquete y se utilizan
# las funciones definidas en ellos.