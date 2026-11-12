# Ejercicios propuestos - Clase 6
# Intenta resolverlos sin mirar soluciones externas. Son ligeramente más difíciles que el temario.

# Ejercicio 1: Gestor de logs rotativo
# Crea una clase GestorLogs con un método registrar(nivel, mensaje) donde nivel
# puede ser "INFO", "WARNING" o "ERROR". Los mensajes se escriben en un archivo
# "app.log" con formato "[NIVEL] YYYY-MM-DD HH:MM:SS - mensaje".
# Cuando el archivo supere 1KB, debe "rotar": renombra el actual añadiendo un
# sufijo con timestamp (ej: "app_20240101_120000.log") y crea uno nuevo vacío.
# Usa pathlib para las rutas y el módulo datetime para el timestamp.


# Ejercicio 2: Explorador de directorios estadístico
# Crea una función explorar(ruta: str, extensiones: list[str] = None) que use pathlib
# para recorrer recursivamente un directorio y devuelva un diccionario:
# {".py": {"archivos": 5, "tamaño_total": 12340}, ".txt": {...}, ...}
# Si extensiones no es None, filtra solo esas extensiones.
# Imprime el resumen formateado mostrando extensión, cantidad y tamaño (B, KB o MB).


# Ejercicio 3: Juego de cartas "Guerra" con registro en archivo
# Usando las clases Carta y Baraja del notebook, implementa el juego "Guerra":
# - Reparte todas las cartas entre dos jugadores (listas).
# - Cada ronda: ambos revelan su primera carta; quien tenga mayor valor se lleva ambas.
# - En empate: cada jugador pone 1 carta boca abajo y juegan la siguiente.
# - El juego termina cuando uno se queda sin cartas.
# Registra cada ronda en un archivo "guerra.log" usando context managers (with).
# Los valores van de As(1) a Rey(13); usa un diccionario para mapear nombres a números.


# Ejercicio 4: Crear y leer archivo de texto

# Hacer un script donde se cree un archivo prueba.txt y se escriba dentro en dos líneas vuestro nombre y en la siguiente línea que estáis estudiando python
 
# posteriormente, intentad leedlo en el mismo script, deberías verlo como dos lineas
 
# puntos extra si después de ver que funciona cambiáis algo del texto y lo leeis, y veis el cambio
 
# archivo = open("prueba.txt", "w")  # Modo de escritura
# archivo.write("Edwin\n")
# archivo.write("Estoy estudiando Python")
# archivo.close()

# archivo = open("prueba.txt", "r")  # Modo de lectura
# contenido = archivo.read()

# print(contenido)    


# d = f"{random.uniform(MIN, MAX):.2f}€"

# import random

# MIN = 1.00
# MAX = 99.99

# random.seed(666)

# for _ in range(10):
#     d = f"{random.uniform(MIN, MAX):.2f}€"
#     print(d)



# import random

# dias_semana = "LMXJVSD"
# # dia_aleatorio = random.choice(dias_semana)
# dia_aleatorio = random.choices(dias_semana, k=2)
# print(dia_aleatorio)

# import sys

# print(sys.argv)

# Ordenar de acuerdo a extensiones

# import pathlib
# import shutil

# path = pathlib.Path() / "test"

# for archivo in path.iterdir():
#     extension = archivo.suffix[1:]
#     path_origen = path / extension
#     path_archivo_destino = path / f"{extension}/{archivo.name}"
#     path_archivo_original = path / archivo.name
#     try:
#         pathlib.Path.mkdir(path_origen)
#         shutil.move(path_archivo_original, path_archivo_destino)
#     except FileExistsError:
#         shutil.move(path_archivo_original, path_archivo_destino)
 


 
# Ejercicio
 
# Crear un explorador de archivos, necesitamos tener un menú que nos permita hacer lo siguiente:
 
# movernos a una ruta (directorio)
# consultar que hay dentro de ese directorio
# crear una carpeta en su interior
# eliminar una carpeta VACIA de su interior
# mover/copiar un archivo de dentro de esa carpeta a otro lugar
 
# puntos extra si lo dividimos en dos modulos distintos
 



