# Video explicativo: https://....

# Generador de personajes aleatorios
# Aula 2 - Grupo 7: MARIN CYNTHIA VANESSA / SOSA RODRIGO FABIAN

# --- SOBRE EL ARCHIVO datos_ia.txt ---
# El archivo 'datos_ia.txt' contiene una lista de características para generar personajes.

"""
PROMPT UTILIZADO PARA GENERAR EL ARCHIVO datos_ia.txt

Necesito que me generes contenido para un archivo de texto llamado datos_ia.txt, que voy a usar en un programa de Python.
El archivo debe contener 3 listas de 10 elementos cada una, todas en español y con un tono humorístico y creativo.

Las listas deben ser las siguientes:

1) [Lista de ocupaciones]
   10 ocupaciones inventadas, absurdas o divertidas, escritas en una sola línea cada una.
   No numerarlas, no usar viñetas, solo el texto plano.

2) [Lista de comidas]
   10 comidas inventadas o graciosas, también en una sola línea cada una, sin numeración.

3) [Lista de habilidades]
   10 habilidades inusuales o fantásticas, escritas en una sola línea cada una.

FORMATO EXACTO:
- Escribir el título entre corchetes: [Lista de ocupaciones], [Lista de comidas], [Lista de habilidades].
- Debajo de cada título incluir los 10 ítems, uno por línea.
- No incluir texto adicional, explicaciones ni espacios en blanco al final.

El resultado final debe tener exactamente 33 líneas: 3 títulos y 30 ítems.
"""

from random import randint  # Librería estándar para selección aleatoria


# --- DEFINICION DE FUNCIONES ---


# Función Extra: Saludo inicial al usuario
def usuario():
    nombre_usuario = input("Ingresa tu Nombre: ")
    apellido_usuario = input("Ingresa tu Apellido: ")
    print(
        f"\n¡Hola {nombre_usuario} {apellido_usuario}! Vamos a crear un personaje muy divertido."
    )
    return nombre_usuario, apellido_usuario


# Función Extra: Selección manual del nombre del personaje
def nombre_personaje():
    print(
        "\nEscribe el nombre y apellido de tu personaje o puedes seleccionar uno de la lista:"
    )

    opciones = [
        "Murruño Lopez",
        "Patilapa Perez",
        "Lichin Caspareli",
        "Guindita Carabajal",
        "Sinunmango Montero",
    ]

    # Muestro las opciones numeradas
    for i in range(len(opciones)):
        print(f"{i + 1}. {opciones[i]}")

    elegido = input(
        "\nEl nombre elegido es: "
    )  # Entrada del usuario distinta de las opciones 1-5

    # Si el usuario ingresa un numero del 1 al 5
    if elegido.isdigit():
        numero = int(elegido)
        if 1 <= numero <= 5:
            elegido = opciones[numero - 1]  # Convertimos número a nombre real

    print(
        f"\n¡{elegido} es un excelente nombre!\n\nLos datos de {elegido} se guardarán en el archivo 'perfil_personaje.txt'.\n"
    )

    return elegido


# Función solicitada en la consigna: Una función que lea información desde un archivo
def leer_caracteristicas():

    archivo = open("datos_ia.txt", "r")
    contenido = archivo.readlines()
    archivo.close()

    # Sacamos los saltos de línea
    contenido_limpio = []
    for linea in contenido:
        contenido_limpio.append(linea.strip())

    return contenido_limpio


# Función solicitada en la consigna: Una función que procese los datos leídos y seleccione resultados aleatorios
"""
Usamos randint de la librería estándar random para seleccionar al azar una ocupación, comida y habilidad desde el archivo datos_ia.txt.
"""


def seleccionar_caracteristica():
    contenido = leer_caracteristicas()

    # 1-10 ocupaciones, 13-22 comidas, 25-34 habilidades
    ocupacion = contenido[randint(1, 10)]
    comida = contenido[randint(13, 22)]
    habilidad = contenido[randint(25, 34)]

    return ocupacion, comida, habilidad


# Función solicitada en la consigna: Una función que muestre información en pantalla
def mostrar_resultados():
    archivo = open("perfil_personaje.txt", "r")
    contenido = archivo.read()
    print(contenido)
    archivo.close()


# Función solicitada en la consigna: Una función que genere un archivo de salida
def generar_salida():
    archivo = open("perfil_personaje.txt", "w")

    archivo.write(
        f"¡{nombre_usuario} {apellido_usuario}, has generado un nuevo personaje con éxito!\n\n"
    )
    archivo.write(
        f"Tu personaje se llama {elegido}, y tiene las siguientes características:\n\n"
    )
    archivo.write(f"OCUPACIÓN: {ocupacion}\n")
    archivo.write(f"PLATO PREFERIDO: {comida}\n")
    archivo.write(f"HABILIDAD: {habilidad}\n")

    archivo.close()


# --- LLAMADO A FUNCIONES PRINCIPALES ---

nombre_usuario, apellido_usuario = usuario()
elegido = nombre_personaje()
ocupacion, comida, habilidad = seleccionar_caracteristica()

generar_salida()

mostrar_resultados()

input("\nPresione Enter para finalizar...")
