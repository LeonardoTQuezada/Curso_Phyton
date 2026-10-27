# print("Hola mundo")

# nombre= "Leonardo"

# print( f"Hola  {nombre}")
# num1=int( input("dime el numero 1: "))
# num2 = int( input("dime el numero 2:  "))
# print(f"la suma es : {num1 + num2} ")


# nombre = "joaquin hernandez martinez"
# print(len(nombre))

# print("Esto es una linea \
#     Y esto es otra linea distinta\n\tY esta ultima linea esta tabulada")


# lista = ["Edwin", "Leo", "Ana"]
# diccionario= {
#     "id" : 120,
#     "nombre": "Elena",
#     "edad" : 30,
#     "hijos": False
# }

# print (f"El elemento 1 de la lista es { lista[1]}")

# print (f"la edad de {diccionario['nombre']} es: {diccionario['edad']} ")


# Calcular la media de los numeros que tenga en una lista (ej. [1, 2, 3, 5, 6, 3, 2, 7]

#  hola tonto


#Crear un filtro de obscenidad (si me meten un texto tipo "calla, idiota", debería salirme por pantalla "calla, ###"

texto = input ("Dime una Frase: ")

filtro =  ["idiota", "calla"]

for palabra in filtro:
  texto = texto.replace(palabra, "#" * len(palabra))

print(texto)