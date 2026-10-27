# Ejercicios propuestos - Clase 1
# Intenta resolverlos sin mirar soluciones externas. Son ligeramente más difíciles que el temario.

# Ejercicio 1: Pirámide de números
# Pide al usuario un número N e imprime una pirámide de números del 1 a N usando bucles anidados.
# Ejemplo para N=4:
# 1
# 1 2
# 1 2 3
# 1 2 3 4

# num = int(input("dime un numero: "))

# for i in range(1, num + 1):
#     fila = "" 
#     for j in  range(1, i + 1):
#         fila += str(j) + " "
#     print(fila)

# Ejercicio 2: Calculadora de notas con clasificación
# Pide 5 notas al usuario (entre 0 y 10) y calcula la media.
# Clasifica el resultado: Suspenso (<5), Aprobado (5-6.9), Notable (7-8.9), Sobresaliente (9-10).
# Muestra también cuántas notas están por encima y cuántas por debajo de la media.

# notas = 0
# for i in range(1, 6):
#     nota = float(input(f"dime la nota {i} : "))
#     while nota < 0 or nota > 10:
#         nota = float(input(f"dime la nota {i} : "))
#     notas+= nota
# media = notas / 5
# if(media < 5): 
#     print(f"Suspendido con {media}")
# elif (media >= 5 or media < 7):
#      print(f"Aprobado con {media}")
# else:
#      print(f"Sobresaliente con {media}")



# Ejercicio 3: Conversor de temperatura
# Pide una temperatura y la unidad de origen (C, F o K) y conviértela a las otras dos unidades.
# Muestra los resultados formateados con 2 decimales.
# Fórmulas: F = C * 9/5 + 32,  K = C + 273.15

# temp = float( input ("dime la temperatura : "))
# unidad = (input ("Unidad de origen (C, F o K)")).lower()

# if unidad == "c" :
#     f = round(temp * 9/5 + 32,2)
#     k = round(temp + 273.15,2)
#     print(f"{temp}°C equivale a {f}°F y {k} K")
# elif unidad == "f":
#     c = round((temp - 32) * 5/9,2)
#     k = round(c + 273.15,2)
#     print(f"{temp}°F equivale a {c}°C y {k} K")
# elif unidad == "k":
#     c = round(temp - 273.15,2)
#     f = round( c * 9/5 + 32,2)
#     print(f"{temp} K equivale a {c}°C y {f}°F")
# else:
#     print("Unidad no válida")
# Crear un sistema de contraseñas, va tener dos pasos:
 
# Primer paso, crear la contraseña. Solo me debería dejar crear una contraseña que tenga al menos 8 caracteres, si tiene menos, se guarda como None
 
# Segundo paso, usar la contraseña. Pedimos al usuario que meta su contraseña, y si es distinta, no le dejamos entrar

#Ejercicio 4  Crear un sistema de usuarios con contraseñas y emails
# usuarios = {
#     1: {
#         "nombre": "Juan",
#         "contraseña": "abc123!",
#         "email": "test@test.com"
#     },
#     2: {
#             "nombre": "Marta",
#             "contraseña": "1234",
#             "email": "marta@test.com"
#         },
#     3: {
#             "nombre": "Joaquin",
#             "contraseña": "666",
#             "email": "joa_profe@test.com"
#         },
#     4: {
#             "nombre": "Ana",
#             "contraseña": "kjabsdk",
#             "email": None
#         }
# }

# # Logica de programacion
# mi_usuario = input("Pon tu usuario: ")
# mi_contraseña = input("Pon tu contraseña: ")
# usuario_encontrado = False
# for usuario in usuarios.values():
#     if mi_usuario.lower() == usuario["nombre"].lower():
#         usuario_encontrado = True
#         if mi_contraseña == usuario["contraseña"]:
#             print("Usuario y contraseña correctos!")
#             break
#         else:
#             print("La contraseña no fue correcta!")
#         if not usuario["email"]:  # Si no tenemos un email
#             nuevo_email = input("Tu usuario no tiene email, crea uno!\n")
#             if nuevo_email.count("@") == 1:  # todo bien!
#                 usuario["email"] = nuevo_email
#             else:
#                 print("Ese email no fue valido!")

# if not usuario_encontrado:
#     print("El usuario no se encontro")
    
    
#     # Vamos a hacer un menu

# menu = """
# ### Bienvenido al codigo de Tajamar! ###

# 1. Leer datos
# 2. Nueva entrada
# 3. Actualizar entrada
# 4. Salir
# """

# print(menu)
# comportamiento = {
#     1: "leer datos",
#     2: "crear entrada",
#     3: "actualizar una entrada",
#     4: "salir"
# }

# eleccion = None
# while not eleccion:
#     eleccion_usuario = int(input("\n¿Que opcion tomas?\n"))
#     if eleccion_usuario in comportamiento:
#         eleccion = eleccion_usuario
#         break
#     else:
#         print("Esa eleccion no es valida!")

# print(f"Has elegido la opcion {eleccion} ---> {comportamiento[eleccion]}")
 


# Ejercicio 5 Hacer un sistema que valide DNIs (tienen 8 numeros y un noveno carácter que es una letra mayuscula)

dni = input("dime tu DNI: ")
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letra = dni[8]
valido  = True
if len(dni) == 9:
    if letra.lower() in letras.lower():
        for i in range(0,8):
            if not dni[i].isdigit():
                valido = False
    else:
       valido = False
else:
    valido = False
    
if valido == True:
    print("DNI valido")
else:
    print("DNI no valido")
