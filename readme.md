# Actividad Integradora Final – Elementos de Programación  
### Licenciatura en Análisis y Gestión de Datos – Universidad Nacional de San Luis (UNSL)  
### Aula 2 - Grupo 7 – Año 2025  

## Título del trabajo:  
**Generador de Perfiles de Personajes**

## Integrantes  
- **Marín, Cynthia Vanessa**  
- **Sosa, Rodrigo Fabián**

---

## 📌 Objetivo de la Actividad  
Integrar los contenidos trabajados a lo largo del cuatrimestre, con énfasis en **funciones** y **manejo de archivos** (Unidad 6), desarrollando un programa en Python que genere automáticamente perfiles de personajes a partir de datos almacenados en un archivo de texto.

---

## 📁 Archivos incluidos en este proyecto  
El archivo ZIP entregado contiene únicamente:

- **generador.py** → Programa principal.  
  La primera línea incluye el enlace al video explicativo.  

- **datos_ia.txt** → Archivo de entrada con tres listas de características (ocupaciones, comidas y habilidades), con al menos 10 ítems cada una. Cada elemento está escrito en una línea independiente, según especifica la consigna.

---

## 🧠 Descripción del programa  
El programa solicita al usuario:

- Su nombre y apellido.  
- El nombre del personaje (ingresado manualmente o elegido de una lista).  

Luego:

1. **Lee y procesa** los datos del archivo `datos_ia.txt`.  
2. **Selecciona aleatoriamente** un elemento de cada una de las listas usando la librería estándar `random`.  
3. **Genera un archivo de salida (`perfil_personaje.txt`)** que contiene:  
   - nombre del personaje,  
   - una ocupación aleatoria,  
   - una comida o plato preferido,  
   - una habilidad o cualidad especial.  
4. **Muestra por pantalla** el contenido del archivo generado.

---

## ✔ Funciones utilizadas
El programa implementa más de tres funciones:

- `leer_caracteristicas()` → Lee y procesa el archivo de entrada.  
- `seleccionar_caracteristica()` → Selección aleatoria de elementos.  
- `mostrar_resultados()` → Muestra el archivo generado.  
- (Además se incluyen funciones adicionales para mejorar la claridad del flujo.)

---

## 🔧 Tecnologías utilizadas  
- Python 3  
- Librería estándar: **random** (`from random import randint`)

*Nota:* Si bien `random` no es una librería vista explícitamente en el curso, forma parte de la librería estándar de Python. Su uso es permitido según la consigna siempre que se explique en el video, ya que permite realizar la selección aleatoria solicitada.

---

## 📄 Generación del archivo datos_ia.txt  
Para crear las listas iniciales del archivo `datos_ia.txt`, utilizamos ChatGPT para obtener ideas creativas.  
Este fue el prompt empleado:

```Genera 3 listas de 10 ítems cada una para usar en un programa de Python que crea personajes aleatorios.
Las listas deben ser:

Ocupaciones creativas y humorísticas.

Comidas o platos inventados.

Habilidades o cualidades especiales originales.

Cada ítem debe ser corto (máximo una línea) y no debe incluir números ni viñetas, solo el texto plano.
No repitas conceptos.
El resultado final debe incluir solo 30 líneas de texto, una característica por línea.```

