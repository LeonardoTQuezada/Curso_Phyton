# Ejercicios propuestos - Clase 4
# Intenta resolverlos sin mirar soluciones externas. Son ligeramente más difíciles que el temario.

# Ejercicio 1: Jerarquía de empleados con herencia múltiple
# Crea una clase base Empleado(nombre, salario) con un método calcular_bonus()
# que devuelva el 10% del salario. Hereda dos clases:
# - Programador(lenguajes: list): el bonus es un 20% del salario.
# - Manager(equipo: list[Empleado]): el bonus es un 30% del salario + 5% por miembro del equipo.
# Implementa __str__ en la clase base mostrando nombre, salario y bonus calculado.
# Usa super() correctamente en todos los constructores.


# Ejercicio 2: Contexto de base de datos simulada (context manager)
# Implementa una clase ConexionDB con __enter__ y __exit__ que simule una conexión.
# Al entrar: imprime "Conectando a la base de datos..."
# Al salir sin error: imprime "Commit realizado. Conexión cerrada."
# Al salir con error: imprime "Rollback realizado: [mensaje_error]. Conexión cerrada."
# El __exit__ debe suprimir el error (devolver True) para que el programa no se detenga.
# Pruébala con un bloque with normal y otro que lance una excepción.


# Ejercicio 3: Sistema de excepciones para una cuenta bancaria
# Crea la clase CuentaBancaria con saldo, limite_credito y lista de transacciones.
# Define excepciones personalizadas: SaldoInsuficiente, MontoInvalido (monto <= 0).
# Implementa: depositar(monto), retirar(monto) y transferir(destino, monto).
# Cada operación añade un registro a la lista de transacciones con el tipo y monto.
# Si retirar pone el saldo por debajo de -limite_credito, lanza SaldoInsuficiente.

# EJERCICIO 


# Ejercicio (veamos como vamos con el temario):
 
# Vamos a hacer el sistema de una sala de seguridad o cámara acorazada.
 
# Tenemos que hacer un sistema de pasos independientes en los que se tienen que cumplir los siguientes:
 
# Se tiene que presentar una tarjeta valida
# Se tiene que introducir un PIN correctamente (para abrir la cámara o sala)
# Se tiene que presentar una huella dactilar correcta
# Los tres pasos anteriores deben realizarse en ese orden, y se deben de especificar por print, por separado
# Si se produce un fallo, todo se reinicia y se debe empezar desde cero
# Si se producen tres fallos consecutivos, el sistema se bloquea para siempre
 
 
#  puntos extra:
 
# que el sistema sea facil de cambiar o mejorar, de forma que se puedan eliminar, añadir, modificar etc... 
# pasos sin que ello suponga rehacer el codigo
 

# t_valida= "T-100"
# pin_valido= "1234"
# def validaTarjeta():
#     tarjeta = input("Ingresa número de tarjeta: ")
#     if tarjeta == t_valida:
#         print("Tarjeta valida")
#         return True
#     else:
#         print("Tarjeta no valida")
#         return False
    
 
# def validaPin():
#     pin = input("Ingresa pin: ").lower()
#     if pin == pin_valido:
#         print("Pin valido")
#         return True
#     else :
#         print("Pin no valido")
#         return False

# def validaHuella():
#     huella = input("Ingresa una huella: ").lower()
#     if huella.lower() == "valida":
#         print("Huella valido")
#         return True
#     else :
#         print("Huella no valido")
#         return False     

# def sistemaSeguridad(*pasos):
#     intentos = 0
#     while True:
#         acceso = True 
#         for paso in pasos:
#             if not paso(): 
#                 acceso = False
#                 intentos+= 1
#                 print(f"Reiniciando sistema... (Fallos consecutivos: {intentos}/3)\n")
#                 break
#         if acceso:
#             print("¡ACCESO CONCEDIDO! La cámara abierta")
#             intentos = 0 
#             break
            
#         if intentos == 3:
#             print("SISTEMA BLOQUEADO")
#             break
        
# sistemaSeguridad( validaTarjeta, validaPin, validaHuella)
        
    
    # EJEERCICIO
#     Hacer una clase que sea ordenador
 
# tiene que tener un método para encenderse y tiene que tener sistema operativo, marca y peso
 
# class Ordenador:
#     sistemaOperativo = "windows"
#     marca = "MSI"
#     peso = 10
#     def __init__(self, encender):
#         self.encender = encender
        
#     def encenderPC(self):
#         self.encender = True
# pc = Ordenador(False)  
# print (pc.encender)
# pc.encenderPC()
# print(pc.encender)


#EJERCICIO

#   class Cliente:
#     def __init__(self, _id: int, nombre_completo: list[str], edad: int,
#                  cantidad_dinero: float, plataforma_de_pago: str = "al contado",
#                  carrito_compra: list[tuple[str, float]] = []):  # [("pan", 1.20), ...]
#         self._id = _id
#         self.nombre = nombre_completo[0]
#         self.apellido = nombre_completo[1]
#         self.edad = edad
#         self.cantidad_dinero = cantidad_dinero
#         self.plataforma = plataforma_de_pago
#         self.carrito = carrito_compra  # ("pan", 1.20)

#     def hacer_compra(self, dinero_a_pagar: float):
#         self.cantidad_dinero -= dinero_a_pagar
#         print(f"Se ha pagado mediante {self.plataforma} {dinero_a_pagar}€ y te quedan {self.cantidad_dinero}€")

#     def validar_compra(self):
#         total_a_pagar = 0
#         for item in self.carrito:
#             total_a_pagar += item[1]  # lo que vale
#         if self.cantidad_dinero < total_a_pagar:
#             print("No se puede pagar!")
#             return False
#         else:
#             self.hacer_compra(total_a_pagar)
#         return True

#     def validar_menor_edad(self):
#         if self.edad < 18:
#             print("Los menores de edad no pueden pagar")
#             return False
#         else:
#             return True

#     def añadir_item_al_carrito(self, item: tuple[str, float]):
#         self.carrito.append(item)

#     def eliminar_item_del_carrito(self, indice_item: int):
#         item_eliminado = self.carrito.pop(indice_item)
#         print(f"Se ha eliminado {item_eliminado[0]}")

#     def mostrar_carrito(self):
#         print(self.carrito)

#     def procesar(self):
#         print(f"Estoy haciendo el pago en {self.plataforma}")
#         if not self.validar_menor_edad():
#             return False
#         if self.validar_compra():
#             print("Todo correcto")
#             return True
#         else:
#             return False

# joa = Cliente(1, "Joaquin Hernandez", 10, 1700.0, "paypal")
# joa.añadir_item_al_carrito(("ordenador", 900))
# joa.añadir_item_al_carrito(("compra_del_mes", 650.23))
# joa.añadir_item_al_carrito(("sumistros", 200.10))
# joa.mostrar_carrito()
# joa.procesar()
# print(joa.cantidad_dinero)  



# EJERCICIO

# Crear una clase e instanciarla 3 veces, que represente un autobus
 
# deberíamos de poder subir y bajar pasajeros (simplemente un numero), 
# deberíamos de tener unos asientos máximos, y deberia de poder arrancar 
# y parar (y no tiene sentido arrancar o parar si esta arrancado o parado)

# class Autonbus:
    
#     def __init__(self,max_pasajeros ):
#         self.max_pasajeros = max_pasajeros
#         self.frenado = False
#         self.en_marcha = False
#         self.pasajeros=0
        
#     def arrancar(self):
#         if not self.en_marcha:
#             self.en_marcha = True
#             print("Autobus arrancado")
#         else:
#              print("No puedes volver a arrancarl el autobus")
             
#     def frenar(self):
#             if self.en_marcha:
#                 self.frenado = True
#                 print("Autobus Frenado")
#             else:
#                  print("No puedes frenar el coche esta apagado")
#     def subirPasajeros(self, pasajeros: int):
#         if self.pasajeros < self.max_pasajeros:
#             self.pasajeros += pasajeros
#             asientos_libres = self.max_pasajeros - pasajeros
#             print(f"Han subido {pasajeros} pasajeros  quedan {asientos_libres} asientos libres")

# autobus1 = Autonbus(15)
# autobus1.arrancar()
# autobus1.frenar()
# autobus1.subirPasajeros(5)


# EJERCICIO
# Hacer dos clases, una que sea un medico, y otra un paciente
 
# El paciente deberá tener un atributo enfermedad (por ejemplo, gripe),
# y el medico deberia poder curar a un paciente (la enfermedad se pone a None)
 
# es decir vamos a tener que tener un objeto interactuando con otro objeto

# class Pasciente:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad
#         self.enfermedad = None
#     def definirEnfermedad(self, enfermedad):
#         self.enfermedad= enfermedad
# class Medico:
#     def __init__(self, nombre , especializacion):
#         self.nombre = nombre
#         self.especializacion = especializacion
        
#     def curarPasiente(self, pasiente: Pasciente):
#         if pasiente.enfermedad is None :
#             print("el pasiente no tiene enfermedades")
#         elif self.especializacion.lower() == "general":
#            pasiente.enfermedad = None
#            print("Pasiente curado")
#         else:
#              print(f"El médico {self.nombre} no es General, no puede curar la enfermedad: {pasiente.enfermedad}.")
            
# medico1 = Medico("Juan", "General")     
# medico2 = Medico("Ana", "Oftalmologa")

# pasiente = Pasciente("Elena", 25)     

# medico1.curarPasiente(pasiente)  
# pasiente.definirEnfermedad("gripe")     
# medico2.curarPasiente(pasiente)  
# medico1.curarPasiente(pasiente) 


# EJERCICIO

# Tenemos un simulador eléctrico, y queremos simular un circuito que enciende y apaga una bombilla, este circuito
# simplemente tiene un interruptor, que debería de poder encender y apagar una bombilla
 
# la bombilla es un objeto en si mismo, lo mismo que el circuito

# class Bombilla:
#     def __init__(self, color , estado= False):
#         self.color = color
#         self.estado = estado
        
#     def cambiaEstado(self, estado):
#         self.estado = estado
#         if self.estado:
#             print("Bombilla encendida")
#         else:
#             print("Bombilla apagada")
        
    
# class Circuito:
#     def __init__(self, interruptor:bool, bombilla: Bombilla):
#         self.interruptor = interruptor
#         self.bombilla = bombilla
    
#     def activaInterruptor(self):
#         self.interruptor = not self.interruptor
#         self.bombilla.cambiaEstado(self.interruptor)
        
# bombilla1= Bombilla("blanco")     
# circuito_electrico = Circuito(False,bombilla1 )      

# circuito_electrico.activaInterruptor()
# circuito_electrico.activaInterruptor()


# class SistemaPagos:
#     def __init__(self, _id: int, entidad: str, destinatario: str):
#         self._id = _id
#         self.entidad = entidad
#         self.destinatario = destinatario

#     def pagar(self):
#         print(f"Se ha pagado correctamente a {self.destinatario} mediante {self.forma_pago}")

# class PagoPaypal(SistemaPagos):
#     def procesar_pago(self, cantidad: float):
#         self.forma_pago = "paypal"
#         self.ultima_cantidad_pagada = cantidad
#         self.pagar()
#         print(f"Se ha pagado {cantidad}€ a {self.destinatario}")

# class PagoCredito(SistemaPagos):
#     def procesar_pago(self, cantidad: float):
#         self.forma_pago = "credito"
#         self.ultima_cantidad_pagada = cantidad
#         self.pagar()
#         print(f"Se ha pagado {cantidad}€ a {self.destinatario}")

# sp = PagoCredito(3, "BBVA", "12345678A")
# sp.procesar_pago(1000)


 

# EJERCICIO


 
# Hacer una clase vehículo, que nos va a servir de base para otras
 
# los vehículos tienen atributos y métodos generales, pero especialmente un deposito de combustible y un método para arrancar o parar
 
# además, quiero que hagamos un tren, un avión y un barco
 
# el tren, el avion y el barco solo deberían poder marchar, volar o navegar si están encendidos
 
 
# class Vehiculo:
#     def __init__(self, deposito, estado = False):
#         self.deposito = deposito
#         self.estado = estado
#     def arrancar(self):
#         self.estado = not self.estado
#         if self.estado :
#             print("Vehículo arrancado")
#         else:
#             print("Vehículo apagado")
            
        
# class Tren (Vehiculo):
#     def marchar (self):
#         if self.estado:
#             print("El Tren se ha puesto en marcha ")
#         else:
#             print("No se puede marchar: el Tren está apagado") 
# class Avion (Vehiculo):
#     def despegar (self):
#         if self.estado:
#             print("El Avion esta despegando ")
#         else:
#             print("No puede despegar: el Avion está apagado")   
# class Barco (Vehiculo):
#     def navegar (self):
#         if self.estado:
#             print("El Barco esta navegando")
#         else:
#             print("No puede navegar: el Barco está apagado")     

# vehiculo1 = Tren(100)
# vehiculo1.arrancar()
# vehiculo1.marchar()

# vehiculo2 = Avion(100)
# vehiculo2.despegar()

# vehiculo3 = Barco(100)
# vehiculo3.navegar()
 

 
#  Ejercicio:
 
# Crear un sistema bancario, en este sistema tenemos información de una cuenta bancaria, es decir, cuanto dinero hay depositado
 
# Además, deberíamos de poder añadir y retirar dinero
 
# Sin embargo, si se intenta retirar mas dinero del que se tiene, deberíamos de tener una excepción que sea ErrorRetiradaIncorrecta
 
# por ultimo, cuando lo utilicéis como ejemplo, quiero que hagáis un try/except controlando para ese error concreto
 
# class ErrorRetiradaIncorrecta(Exception):
#   pass
# class CuentaBancaria:
#     def __init__(self, saldo= 0):
#         self.saldo = saldo
#     def  depositar(self, ingreso = float):
#         self.saldo += ingreso
        
#     def retirar (self, retiro):
#         if retiro > self.saldo:
#             raise ErrorRetiradaIncorrecta("¡Saldo insuficiente!")
#         self.saldo -= retiro 
#         print(f"Retiro exitoso. Saldo restante: {self.saldo}")



# cuenta_corriente = CuentaBancaria(1000.0)
# try:
#     cuenta_corriente.retirar(2000.0)
# except ErrorRetiradaIncorrecta as error:
#     print(f"{error}")
    
    
#     Segundo ejercicio
 
# Crear un sistema de pagos, en el que tengamos pago por Paypal, pago por tarjeta de crédito y pago por transferencia
 
# Además, todos ellos deberían tener el mismo método de pagar(), pero un poco especial:
 
# el sistema Paypal requiere de un token, y devuelve un True/False si fue bien
# el sistema por crédito no requiere nada, y devuelve la cantidad, ya que representa una deuda para el banco (que aun debe procesarse)
# el sistema por transferencia requiere de un IBAN o SWIFT, y devuelve True/False si fue bien
# Por ultimo, crear un error para la clase padre, en la que controlemos que algo haya ido mal con el pago

class ErrorPagoIncorrecto(Exception):
  pass
class MetodoPago:
    
    def procesar_pago(self, cantidad):
       resultado = self.pagar(cantidad)
       if resultado is False:
            raise ErrorPagoIncorrecto("Algo ha ido mal con el pago.")
       return resultado

class PagoPaypal(MetodoPago):
    def __init__(self, token):
        self.token = token
       
    def pagar(self, cantidad: float):
        if not self.token:
            return False
        print(f"Pago de {cantidad} procesado por PayPal.")
        return True
class PagoTarjeta(MetodoPago):
  def pagar(self, cantidad: float) :
    print(f"Pago de {cantidad} registrado en la tarjeta de crédito.")
    return cantidad  

class PagoTransferencia(MetodoPago):
    def __init__(self, iban: str):
            self.iban = iban
    def pagar(self, cantidad: float) :
        if not self.iban:
            return False
        print(f"Pago de {cantidad} enviado a la cuenta {self.iban}.")
        return True

try:
    paypal = PagoPaypal("token")
    paypal.procesar_pago(200)
    tarjeta = PagoTarjeta()
    tarjeta.procesar_pago(2000)
except ErrorPagoIncorrecto as error:
    print(f"{error}")