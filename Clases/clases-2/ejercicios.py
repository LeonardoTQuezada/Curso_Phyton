# Ejercicios propuestos - Clase 2
# Intenta resolverlos sin mirar soluciones externas. Son ligeramente más difíciles que el temario.

# Ejercicio 1: Detector de anagramas
# Dadas dos palabras introducidas por el usuario, comprueba si son anagramas
# (contienen exactamente las mismas letras). No uses sort(): hazlo construyendo
# un diccionario que cuente la frecuencia de cada letra en cada palabra y compáralos.
# Ignora mayúsculas y espacios.

# palabra1 =  input("Dime una palabra: ").lower().split()
# palabra2 = input("Dime otra palabra: ").lower().split()

# print(palabra1)
# print(palabra2)



# Ejercicio 2: Top 3 de estudiantes
# Dado un diccionario de estudiantes con sus listas de notas:
# {"Ana": [7, 8, 6], "Luis": [9, 5, 8], "Marta": [10, 9, 8], ...}
# Calcula la media de cada alumno y muestra el top 3 con mayor media.
# Usa slicing para obtener los 3 primeros tras ordenar el resultado.


# Ejercicio 3: Inventario de tienda
# Modela un inventario como un diccionario {producto: (precio, cantidad)}.
# Implementa las siguientes operaciones usando métodos de diccionario:
# - Añadir producto (con .setdefault para evitar sobreescribir si ya existe)
# - Actualizar stock de un producto
# - Calcular el valor total del inventario (precio * cantidad de cada producto)
# - Listar los productos agotados (cantidad == 0)




# # Ejercicio 4
# # Monitor de servidores

# servidores = {
#     "web-1": {"cpu": 40, "ram": 800, "health": True},  # health es encendido o apagado
#     "web-2": {"cpu": 85, "ram": 2000, "health": False},
#     "db-1": {"cpu": 99, "ram": 80, "health": True},
#     "db-2": {"cpu": 20, "ram": 10000, "health": False},
#     "web-3": {"cpu": 5, "ram": 512, "health": False},
#     "front-1": {"cpu": 97, "ram": 2048, "health": True},
# }

# # Detectar:
# #   CPU superior a 80%  |  RAM menos de 512  |  Criticos estan encendidos y cumplen ambas

# servidores_criticos = []
# for servidor, valores_servidor in servidores.items():
#     cpu_alta = 80
#     memoria_baja = 512
#     estado_servidor = 0  # 1 esta mal, 2 esta critico

#     if valores_servidor["cpu"] >= cpu_alta:
#         estado_servidor += 1

#     if valores_servidor["ram"] <= memoria_baja:
#         estado_servidor += 1

#     if valores_servidor["health"]:
#         if estado_servidor <= 0:
#             print(f"El servidor {servidor} esta estable")
#         elif estado_servidor == 1:
#             print(f"El servidor {servidor} esta en mal estado")
#         elif estado_servidor == 2:
#             servidores_criticos.append(servidor)
#             print(f"El servidor {servidor} esta en estado critico!")
#     else:
#         print(f"El servidor {servidor} esta apagado")

# print("-" * 50)  # separador en el menu

# print(f"Tenemos {len(servidores_criticos)} servidores criticos, que son {servidores_criticos}")
 
 
 # Sistema de autenticacion de usuarios

# usuarios = {
#     "joaquin": {
#         "rol": "admin",
#         "permisos": ["lectura", "escritura", "devops", "admin"],
#         "activo": True
#     },
#     "maria": {
#             "rol": "devops",
#             "permisos": ["lectura", "devops"],
#             "activo": True
#     },
#     "juan": {
#             "rol": "developer",
#             "permisos": ["lectura", "escritura"],
#             "activo": True
#     },
#     "silvia": {
#             "rol": "sales",
#             "permisos": ["lectura"],
#             "activo": False
#     },
# }

# usuarios["silvia"]["activo"] = True
# usuarios.update({"pedro": {"rol": "developer", "permisos": ["lectura", "escritura"], "activo": True}})
# usuarios["juan"]["activo"] = False

# permiso_a_consultar = input("Que permiso quieres consultar?\n")

# usuarios_con_permisos = []
# for usuario, info in usuarios.items():
#     permisos = info["permisos"]
#     activo = info["activo"]
#     if permiso_a_consultar in permisos and activo:
#         usuarios_con_permisos.append(usuario)

# print(f"Los usuarios con permisos de {permiso_a_consultar} son {len(usuarios_con_permisos)}\n{usuarios_con_permisos}")


# Crear un contador de errores en un servidor
 
# Nos va a llegar una lista tal que así:
 
# logs = ["ERROR", "INFO", "WARNING", "ERROR", "ERROR", "INFO"]
 
# tenemos que contabilizar cuantos errores de cada tipo hemos tenido
 
# (pista, lo idea es guardar esto en un diccionario!)
 
 
# logs = ["ERROR", "INFO", "WARNING", "ERROR", "ERROR", "INFO"]

# servidor = { "EROOR": logs.count('ERROR'),
#             "INFO": logs.count('INFO'),
#             "WARNING": logs.count("WARNING"),
            
#             }

# print(servidor)


# # OTRA MANERA 

# claves_logs = list(set(logs))  # elimino duplicados y hago mi lista de claves
# resultado = {}  # hago el diccionario
# for clave in claves_logs:
#     resultado[clave] = logs.count(clave)  # relleno el diccionario

# print(resultado)


# Ejercicio - registro de usuarios
 
# Tendremos una lista de usuarios

# y queremos un sistema que nos pida un usuario, si el usuario ya existe, se le dice que ya existe y no se añade, 
# si no existe, se añade y se notifica (y damos el total de usuarios)
# punto extra:
 
# en vez de pedir un usuario, pedimos los usuarios que queramos, hasta poner STOP

usuarios = ["joaquin", "ana", "maria", "pablo"]
 
lis_user = []

while True:
    nombre = input("Dime un usuarios: ").lower()
    if nombre == "stop":
        break
    lis_user.append (nombre)

for nombre in lis_user:
    if nombre in usuarios:
        print(f"usuario existe: {nombre}")
    else:
        usuarios.append(nombre)
        print(f"Se añadio el usuario {nombre} y hay un total de {len(usuarios)}")

