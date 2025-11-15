# Video explicativo: https://....
#
# NO MAS DE 3 minutos de video, no explicar linea por linea lo que hace el código, sino la lógica general y las decisiones tomadas. Ademas de explicar como generamos el archivo datos_ia.txt (SI usamos GPT ponemos el prompt utilizado). Ambos entregamos el mismo archivo zip con el codigo pytho (y el link video), el archivo datos_ia.txt en el aula virtual. Hay que explicar las funciones que fueron creadas y no estaban pedidas en el enunciado, explicar random para que lo utilizamos...agregar comentarios en el codigo para explicar las decisiones tomadas.


# Generador de personajes aleatorios
# Aula 2 - Grupo 7: MARIN CYNTHIA VANESSA / SOSA RODRIGO FABIAN

from random import randint  # Librería estándar para selección aleatoria

# --- DEFINICION DE FUNCIONES ---


# Saludo inicial al usuario
def usuario():
    nombre_usuario = input("Ingresa tu Nombre: ")
    apellido_usuario = input("Ingresa tu Apellido: ")
    print(
        f"\n¡Hola {nombre_usuario} {apellido_usuario}! Vamos a crear un personaje muy divertido."
    )
    return nombre_usuario, apellido_usuario


# Selección manual del nombre del personaje
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

    # Mostrar opciones numeradas
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


# Leer características desde archivo externo
def leer_caracteristicas():
    archivo = open("datos_ia.txt", "r")
    contenido = archivo.readlines()
    archivo.close()

    # Sacamos los saltos de línea
    contenido_limpio = []
    for linea in contenido:
        contenido_limpio.append(linea.strip())

    return contenido_limpio


# Seleccionar características aleatorias
def seleccionar_caracteristica():
    contenido = leer_caracteristicas()

    # 0-9 ocupaciones, 10-19 comidas, 20-29 habilidades
    ocupacion = contenido[randint(0, 9)]
    comida = contenido[randint(10, 19)]
    habilidad = contenido[randint(20, 29)]

    return ocupacion, comida, habilidad


# Mostrar resultados por pantalla
def mostrar_resultados():
    archivo = open("perfil_personaje.txt", "r")
    contenido = archivo.read()
    print(contenido)
    archivo.close()


# Crear archivo de salida
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


# Las importaciones se realizan al inicio del código para seguir las mejores prácticas de programación.
# las variables y funciones en python se nombran utilizando minúsculas y guiones bajos para mejorar la legibilidad.
# random es parte de la librería estándar de Python, no es una librería externa. Explicar en el video quee la utilizamos para que la elección sea aleatoria.
