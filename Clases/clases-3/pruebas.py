# import math


# def solve(n):
#     for i in range(1, n + 1):
#         fila = ""
#         num = 1  # Todos los inicios de fila empiezan en 1
        
#         for j in range(1, i + 1):
#             fila += str(num) + " "
            
#             # PROPIEDAD MATEMÁTICA: 
#             # Calcula el siguiente número de la izquierda en tiempo real
#             # basándose en la posición actual de la fila (i) y la columna (j).
#             num = (i - j + 1) * math.comb(i + j - 2, j - 1) 
            
#         print(fila)

# solve(5)

# Crear una funcion formatear_nombre a la que le demos por posición el nombre, el apellido,
# y el apellido 2 de alguien, y que tenga dos args extra como clave valor, uno que sea upper (por defecto False) 
# que ponga todo en mayúscula, y otro que sea añadir, y que añada un texto al final en una línea nueva (con "\n")
 
# una vez hecho esto, quiero que lo hagamos con empaquetamiento, ya que habrá nombres con solo un apellido,
# o nombres con 2 nombres (y por tanto con 4 strings), es decir, habrá que usar empaquetamiento por posicion
 
# def formatear_nombre(nombre, apellido1, apellido2, upper=False, añadir=""):
   
#     fullName = f"{nombre} {apellido1} {apellido2}"
#     if upper:
#         fullName = fullName.upper()
#     if añadir:
#         fullName = f"{fullName}\n{añadir}"  
#     return fullName

# def formatear_nombre2(**formato):

#     name = f"{formato.get('nombre')} {formato.get('apellido1')} {formato.get('apellido2')}"
#     if formato.get("upper"):
#         name = name.upper()
#     texto_extra = formato.get("añadir")
#     if texto_extra:
#         name = f"{name}\n{texto_extra}"
#     return name


# print(formatear_nombre2(nombre="Elena",apellido1="Martinez",apellido2="Fernandez", upper=True, añadir="Hola"))

# EJERCICIO

# nos van a dar una lista con tuplas nombre, dinero
 
# en este caso representa un grupo de amigos intentando pagar la cuenta de un restaurante
 
# queremos hacer una funcion que nos de la cuenta dividida, es decir, cuando habría que pagar entre todos
 
# por ejemplo si tenemos [1, 2, 3] la media es 6/3 = 2 por lo que nuestra funcion devolvería 2
 
# ademas de esto, deberia tener una opción especial que es la propina, como clave valor, de forma que
 
# repartir_cuenta(2, 3, 4, propina=3) de como resultado 2

# es decir, 2 + 3 + 4 + 3 (la propina) = 12
 
# y 12 / 3 (total de personas) son 4 

# pagos = [
#     ("Ana", 18.50),
#     ("Luis", 24.00),
#     ("Marta", 15.50),
#     ("Pedro", 22.00)
# ]

# def repartir_cuenta( *gastos, propina: float = 0   ) -> float:
#     suma= propina
#     for nom, cantidad  in gastos:
#         suma += cantidad
#     return suma / len(gastos)

# print(repartir_cuenta(*pagos,propina = 3  ))

# Ejercicio callback


# def filtrar_por_tipo(lista: list, tipo: type, tamaño: int) -> list:
#     lista_final = []
#     for elemento in lista:
#         if isinstance(elemento, tipo):
#             lista_final.append(elemento)
#     return lista_final

# def filtrar_por_tamaño(lista: list, tipo: type, tamaño: int):
#     lista_final = []
#     for elemento in lista:
#         if isinstance(elemento, (int, float)):
#             if elemento >= tamaño:
#                 lista_final.append(elemento)
#         elif isinstance(elemento, (str, tuple, list, dict)):
#             if len(elemento) >= tamaño:
#                 lista_final.append(elemento)
#     return lista_final

# def pipeline_de_filtrado(datos: list, tipo: type, tamaño: int, *filtros):
#     for filtro in filtros:
#         datos = filtro(datos, tipo, tamaño)
#     return datos

# datos = [1, 4, 100, 80, 50.5, -20, "abcjksbdjbsdkbnajksbd", "kjsd", (1, 2, 3, 4, 5, 6), "abc"]
# res = pipeline_de_filtrado(datos, int, 5, filtrar_por_tipo, filtrar_por_tamaño)
# print(res)


# Ejercicio 

# Hacer un callback de validaciones de datos (concretamente para numeros)
 
# queremos saber si un numero es....
 
# par
# impar
# entero o flotante
# primo
 
# asi que hay que hace run callback donde le demos un numero y me haga esas validaciones
#  UNA VEZ HECHO
 
# añadir estas tres lógicas:
 
# ese numero es una edad ---> ver si es mayor o menor de edad
 
# ese numero es la presion de un neumatico ---> ver si entra en los valores adecuados entre 180 y 460
 
# ese numero es un numero de intentos ---> ver si hay mas de 3 intentos para bloquear temporalmente al usuario

# el callback se puede llamar validar() perfectamente
 
# def validar(num :int | float, *valida  ):
#      for funcion in valida: 
#         funcion(num)   

# def isPar(num):
#     if num % 2 == 0:
#         print("Es par")
#     else:
#         print("No es par")
   
# def esEntero (num:int | float) :
#     if  isinstance(num, int)  :
#          print("Es entero")
#     else:
#         print("Es float")
        
# def esPrimo (num:int | float):
#     if num <= 1 or isinstance(num, float):
#         print("No es primo")  
#         return;  
#     for i in range(2, num):
#         if num % i == 0:
#             print("No es primo") 
#             return     
#     print("Es primo") 

# def  esEdad(num: int | float):
#     if num < 1 or num >= 105:
#         print("No es edad")  
#         return; 
#     print("Es mayor de edad") if num >= 18 else  print("Es menor de edad")
    
# def  esPresionAdecuada(num: int | float):
#     print("Presión adecuada") if num >= 180 and num <= 460  else  print("Presión irregular")

# def validarintentos(num: int | float):
#     num= int(num)
#     print("Intentos superados") if num >3  else  print(f"Te quedan {3-num} intentos")
# num = 2
# validar(num,  esEdad, esPresionAdecuada, validarintentos )  


# print(*[f"{k}: {v}" for k, v in locals().items() if not k.startswith("__")], sep="\n")

# EJERCICIO 
# Hacer las siguientes lambdas:
 
# tomar una lista de números y darme su suma
# tomar un string y dármelo en mayúsculas y añadiendo un espacio y su tamaño al final (ejemplo "abc" deberia darme "ABC 3"
# tomar un diccionario y devolverme una tupla, primero con una tupla de sus claves y después una tupla de sus valores
 
lista = lambda lista :sum(lista)

print(lista([1,2,3]))

texto = lambda texto :  texto.upper() +" "+ str(len(texto))

print( texto("abc"))

usuario = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

darTupla_key = lambda dicionario :  tuple(dicionario.keys())
darTupla_valor = lambda dicionario :  tuple(dicionario.values())

print(darTupla_key(usuario))
print(darTupla_valor(usuario))