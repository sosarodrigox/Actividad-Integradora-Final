# Generador.py
# Generador de personajes aleatorios
# Aula 2 - Grupo 7: MARIN CYNTHIA VANESSA / SOSA RODRIGO FABIAN
# Video explicativo: https://tu_link

from random import randint  # Llamado de funcion randint

# 1- DEFINICION DE FUNCIONES:


# Saludo inicial al usuario
def usuario():
    nombre_usuario = input("Ingresa tu Nombre: ")
    apellido_usuario = input("Ingresa tu Apellido: ")
    print(
        f"\n¡Hola {nombre_usuario} {apellido_usuario}! Vamos a crear un personaje muy divertido."
    )
    return (nombre_usuario, apellido_usuario)


# Nombre del personaje. Elige el Nombre de una lista de opciones
def nombre_personaje():
    print(
        "\nEscribe el nombre y apellido de tu personaje o puedes seleccionar uno de la lista: "
    )

    opciones = [
        "1.Murruño Lopez",
        "2.Patilapa Perez",
        "3.Lichin Caspareli",
        "4.Guindita Carabajal",
        "5.Sinunmango Montero",
    ]  # Lista con alternativas opcionales
    for personaje in opciones:
        print(personaje)

    elegido = input("\nEl nombre elgido es: ")
    print(
        f"\n¡{elegido} es un excelente nombre!\n \nLos datos de {elegido} se guardaran en el archivo 'perfil_personaje.txt' dentro de tu ordenador.\n"
    )

    return elegido


# Caracteristicas del personaje. Lee las caracteristicas del personaje sobre una lista desde un archivo externo
def leer_caracteristicas():
    archivo = open("datos_ia.txt", "r")
    contenido = archivo.readlines()
    archivo.close()
    return contenido


# Seleccionar las caracteriticas del personaje. Toma aleatoriamente caracteriticas del personaje
def seleccionar_caracteristica():
    contenido = leer_caracteristicas()

    for caracteristica in contenido:
        ocupacion = contenido[randint(0, 9)]  # Selecciòn aleatoria de ocupación
        comida = contenido[randint(10, 19)]  # Selección aleatoria de un plato preferido
        habilidades = contenido[randint(20, 29)]  # Selección aleatoria de una habilidad
    return (ocupacion, comida, habilidades)


# Llamado de funciones
(nombre_usuario, apellido_usuario) = usuario()
elegido = nombre_personaje()
(ocupacion, comida, habilidades) = seleccionar_caracteristica()


# Generar un archivo de salida con los datos del personaje
def generar_salida():

    # Crea un archivo de salida con los resultados de las funciones
    archivo = open("perfil_personaje.txt", "w")
    archivo.write(
        f"¡{nombre_usuario} {apellido_usuario}, has generado un nuevo personaje con éxito!"
    )
    archivo.write(
        f"\n\nTu personaje se llama {elegido}, y tiene las siguientes caracteristicas:\n \nOCUPACION: {ocupacion} \nPLATO PREFERIDO: {comida}\nHABILIDAD: {habilidades}"
    )
    archivo.close()


generar_salida()


def mostrar_resultados():
    archivo = open("perfil_personaje.txt", "r")
    contenido = archivo.read()
    print(contenido)
    archivo.close()


mostrar_resultados()


# 1- FLUJO PRINCIPAL DEL PROGRMA:

# Las importaciones se realizan al inicio del código para seguir las mejores prácticas de programación.
# las variables y funciones en python se nombran utilizando minúsculas y guiones bajos para mejorar la legibilidad.
# random es parte de la librería estándar de Python, no es una librería externa. Explicar en el video quee la utilizamos para que la elección sea aleatoria.
