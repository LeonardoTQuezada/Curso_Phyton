
# Diseño de software

# Principios SOLID

# 1 - Single responsability (responsabilidad unica)

# class ErrorConexion(Exception):
#     pass

# class Conexion:
#     def __init__(self, ruta: str, puerto: int, usuario: str, contraseña: str, validadores: dict[function] = {}, *
#                  , contexto: dict = {}):
#         self.ruta = ruta
#         self.puerto = puerto
#         self.uri = f"{ruta}:{puerto}"
#         self.usuario = usuario
#         self.contraseña = contraseña
#         self.validadores = validadores
#         self.contexto = contexto

#     def get_uri(self):
#         return self.uri

#     def validar_usuario(self):
#         if self.validadores:
#             validador = self.validadores.get("validar_usuario")
#             resultado = validador(self.usuario)
#             return resultado

#     def validar_contraseña(self):
#         if self.validadores:
#             validador = self.validadores.get("validar_contraseña")
#             resultado = validador(self.contraseña)
#             return resultado

#     def validar(self):
#         resultados = []
#         for validador, validador_funcion in self.validadores.items():
#             if validador == "validar_usuario":
#                 resultados.append(validador_funcion(self.usuario))
#             elif validador == "validar_contraseña":
#                 resultados.append(validador_funcion(self.contraseña))
#             resultados.append(validador_funcion(self.contexto))
#         return resultados

#     def conectar_base_datos(self):
#         try:
#             exito_validar = self.validar()
#             if False in exito_validar:
#                 raise ErrorConexion("La conexion a base de datos ha fallado")
#             print("Se ha conectado a base de datos")
#             ...
#         except Exception as error:
#             print(f"Error: {repr(error)}")
#             return 


# Ejercicio
 
# hacer una clase calculadora que pueda sumar, restar, multiplicar y dividir
 
# ojo que tiene que cumplir el primer principio!!
 
# una vez hecho, y solo cuando este hecho, vamos a tener en cuenta el siguiente caso:
 
# nuestro cliente quiere que además la calculadora pueda elevar al cuadrado y calcular la raíz cuadrada
# (recordad que tenes sqrt en modulo math)
# import math


# class Calculadora:
#     def __init__(self, a: float = 0, b: float = 0):
#         self.a = a
#         self.b = b

#     def sumar(self):
#         return self.a + self.b

#     def restar(self):
#         return self.a - self.b

#     def multiplicar(self):
#         return self.a * self.b

#     def dividir(self):
#         if self.b == 0:
#             raise ValueError("No se puede dividir por cero")
#         return self.a / self.b

#     def elevar_cuadrado(self):
#         return self.a ** 2

#     def calcular_raiz_cuadrada(self):
#         if self.a < 0:
#             raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
#         return math.sqrt(self.a)

# calculadora = Calculadora(4, 2)
# print(calculadora.sumar())


# Ejercicio 2 interfaces

# Crear unas clases para modelar aparatos eléctricos (ventilador, bombilla, motor, etc...)
 
# y una interfaz para ellos, que sea AparatoElectrico
# todos los aparatos eléctricos deben tener una resistencia interna, un interruptor (metodo para encenderlo o apagarlo)
# y una funcionalidad (el ventilador da aire, el motor mueve algo, etc...)

