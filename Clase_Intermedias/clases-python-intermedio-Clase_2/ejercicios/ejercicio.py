# # Ejercicio de Interfaces y Clases Abstractas
# # Crear unas clases para modelar aparatos eléctricos (ventilador, bombilla, motor, etc...)
 
# # y una interfaz para ellos, que sea AparatoElectrico
# #  todos los aparatos eléctricos deben tener una resistencia interna, un interruptor (metodo para encenderlo o apagarlo) 
# # y una funcionalidad (el ventilador da aire, el motor mueve algo, etc...) 


# from abc import ABC, abstractmethod

# class AparatoElectrico(ABC):
#     def __init__(self, resistencia):
#         self.resistencia = resistencia
#         self.encendido = False

#     def encender(self):
#         self.encendido = True

#     def apagar(self):
#         self.encendido = False

#     @abstractmethod
#     def funcionalidad(self):
#         pass
        

# class Ventilador(AparatoElectrico):
#     def funcionalidad(self):
#         if self.encendido:
#             print("El ventilador está dando aire.")
#         else:
#             print("El ventilador está apagado.")

# class Bombilla(AparatoElectrico):
#     def funcionalidad(self):
#         if self.encendido:
#             print("La bombilla está iluminando.")
#         else:
#             print("La bombilla está apagada.")  

# class Motor(AparatoElectrico):
#     def funcionalidad(self):
#         if self.encendido:
#             print("El motor está moviendo algo.")
#         else:
#             print("El motor está apagado.") 


# aparato1 = Ventilador(10)
# aparato1.funcionalidad()  
# aparato1.encender()
# aparato1.funcionalidad()

# Ejercicio orientado a objetos: Crear un circuito eléctrico con una bombilla
 
# Tenemos que crear un circuito (orientación a objetos)
 
# En este circuito tenemos que tener una bombilla, que se enciende y se apaga desde el circuito
 
# class interFaceAparatoElectrico:
#     def __init__(self):
#             self.encendido = False
#     def encender(self):
#            self.encendida = True
#            print("Está encendida.")
   
#     def apagar(self):
#         self.encendida = False
#         print("Está apagada.")


# class Bombilla(interFaceAparatoElectrico):
#   pass


# class Circuito:
#     def __init__(self, objeto):
#         self.objeto = objeto
#         self.interruptor = False   

#     def pulsar_interruptor(self):
#         self.interruptor = not self.interruptor
#         if self.interruptor:
#             self.objeto.encender()
#         else:
#             self.objeto.apagar()

# class Ventilador(interFaceAparatoElectrico):
#     pass


# bombilla = Bombilla()
# circuito = Circuito(bombilla)
# circuito.pulsar_interruptor()
# circuito.pulsar_interruptor()

# ventilador = Ventilador()
# circuito_ventilador = Circuito(ventilador)
# circuito_ventilador.pulsar_interruptor()    


# Ejercicio de inyección de dependencias
 
# Crear un sistema para una misión a Marte
 
# la idea es que tengamos sensores de oxigeno, generadores eléctricos, sistemas de comunicaciones, etc... (podéis ser creativos)
 
# y todo esto debe enviar info al centro de control
 
# los sensores deben avisar si el oxigeno cae a niveles peligrosos, los generadores deben poder cargarse o descargarse
# (y hay alerta si caen a menos del 5%), las comunicaciones deben poder establecerse (y hay alerta si NO están establecidas)
 
# por restricciones de la misión, solo se pueden tener conectados 2 sistemas a la vez, si hacéis mas sistemas por ser creativos, 
# debéis tener obligatoriamente una alerta en ellos (por tanto ya sabéis que cada sistema debe tener una función para alertar al centro de control!)
 
# reto extra: estos sistemas deben poder cambiarse en el futuro, es decir, tal vez el sistema de oxigeno cambie su forma de funcionar 
# de aquí a 1 año! pero eso si, siempre enviara alertas
 
# ideas creativas de mas sistemas: temperatura, comida, registro de horas de trabajo para los ingenieros, etc...
 
# from abc import ABC, abstractmethod
 
# class Sistema(ABC):
 
#     @abstractmethod
#     def enviar_alerta(self):
#         pass
 
# class SistemaOxigeno(Sistema):
#     def __init__(self, nivel_oxigeno):
#         self.nivel_oxigeno = nivel_oxigeno

#     def enviar_alerta(self):
#         if self.nivel_oxigeno < 20:
#             return "Alerta: Nivel de oxígeno peligroso!"
#         else:
#             return "Nivel de oxígeno adecuado."

# class SistemaElectrico(Sistema):
#     def __init__(self, carga):
#         self.carga = carga

#     def enviar_alerta(self):
#         if self.carga < 5:
#             return "Alerta: Carga del generador eléctrica baja!"
#         else:
#             return "Carga del generador eléctrica adecuada."

#     def cargar(self, cantidad):
#      if self.carga + cantidad <= 100:
#             self.carga += cantidad


#     def descargar(self, cantidad):
#         if self.carga - cantidad >= 0:
#             self.carga -= cantidad

# class SistemaComunicaciones(Sistema):

#     def __init__(self, establecida):
#         self.establecida = establecida

#     def establecer_comunicacion(self):
#         self.establecida = True


#     def enviar_alerta(self):
#         if not self.establecida:
#             return "Alerta: Comunicaciones no establecidas!"
#         else:
#             return "Comunicaciones establecidas correctamente."
# class SistemaAlimentacion(Sistema):
#     def __init__(self, nivel_comida):
#         self.nivel_comida = nivel_comida

#     def enviar_alerta(self):
#         if self.nivel_comida < 10:
#             return "Alerta: Nivel de comida bajo!"
#         else:
#             return "Nivel de comida adecuado."
#     def agregar_comida(self, cantidad):
#         if self.nivel_comida + cantidad <= 100:
#             self.nivel_comida += cantidad
#         else:
#             print("No se puede agregar más comida. Nivel máximo alcanzado.")
#     def consumir_comida(self, cantidad):
#         if self.nivel_comida - cantidad >= 0:
#             self.nivel_comida -= cantidad
#         else:
#             print("No hay suficiente comida para consumir esa cantidad.")
# class SistemasOxigenoV2(Sistema):
#     def __init__(self, nivel_oxigeno):
#         self.nivel_oxigeno = nivel_oxigeno

#     def enviar_alerta(self):
#         if self.nivel_oxigeno < 10:
#             return f"Alerta: Nivel de oxígeno crítico! ({self.nivel_oxigeno}%)"
#         elif self.nivel_oxigeno < 40:
#             return f"Alerta: Nivel de oxígeno bajo! ({self.nivel_oxigeno}%)"
#         else:
#             return "Nivel de oxígeno adecuado."
        
# class CentroControl:
    
#     def __init__(self):
#         self.sistemas = []

#     def agregar_sistema(self, sistema):
#         if len(self.sistemas) < 2:
#             self.sistemas.append(sistema)
#         else:
#             print("No se pueden agregar más sistemas. Solo se permiten 2 sistemas conectados a la vez.")

#     def enviar_alertas(self):
#         for sistema in self.sistemas:
#             print(sistema.enviar_alerta())

#     def desconectar_sistema(self, sistema):
#         if sistema in self.sistemas:
#             self.sistemas.remove(sistema)
#         else:
#             print("El sistema no está conectado al centro de control.")

# ## Ejemplo de uso
# sistema_oxigeno = SistemaOxigeno(nivel_oxigeno=15)
# sistema_electrico = SistemaElectrico(carga=3)   
# sistema_comunicaciones = SistemaComunicaciones(establecida=False)
# sistema_alimentacion = SistemaAlimentacion(nivel_comida=50)

# centro_control = CentroControl()
# centro_control.agregar_sistema(sistema_oxigeno) 
# centro_control.agregar_sistema(sistema_electrico)
# centro_control.agregar_sistema(sistema_comunicaciones)  
# print("\n****Alertas****")
# centro_control.enviar_alertas()  

# sistema_electrico.cargar(10)
# sistema_oxigeno.nivel_oxigeno = 25


# print("\n****Alertas****")
# centro_control.enviar_alertas()

# centro_control.desconectar_sistema(sistema_electrico)
# centro_control.agregar_sistema(sistema_alimentacion)
# sistema_alimentacion.consumir_comida(400)
# print("\n****Alertas****")
# centro_control.enviar_alertas()


# sistema_oxigeno_v2 = SistemasOxigenoV2(nivel_oxigeno=35)
# centro_control.desconectar_sistema(sistema_oxigeno)
# centro_control.agregar_sistema(sistema_oxigeno_v2)  
# print("\n****Alertas****")
# centro_control.enviar_alertas()



# Ejercicio:
 
# Vamos a hacer un sistema de Uber Eats o de comida en general.
 
# La App debe permitirnos realizar pedidos, y notificar al cliente cuando el pedido sale
 
# lo que pasa es que hay varias formas de enviar notificaciones (whatsapp, email, sms, etc...)
 
# queremos tener un sistema sencillo para cambiar fácilmente de una forma de enviar mensajes a otra
 
# reto extra: añadir un callback para el pago, donde le podamos meter cualquier sistema de pago (una función)
 
# debería estar esto en la interfaz? en las formas de notificación? en el gestor de notificaciones?
 
from abc import ABC, abstractmethod

class Notificador(ABC):
    @abstractmethod
    def enviar_notificacion(self, mensaje):
        pass

class NotificadorWhatsApp(Notificador):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando notificación por WhatsApp: {mensaje}")

class NotificadorEmail(Notificador):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando notificación por Email: {mensaje}")

class NotificadorSMS(Notificador):
    def enviar_notificacion(self, mensaje):
        print(f"Enviando notificación por SMS: {mensaje}")

class AppComida:
    def __init__(self, notificador):
        self.notificador = notificador

    def realizar_pedido(self, pedido):
        print(f"Pedido realizado: {pedido}")
        self.notificador.enviar_notificacion(f"Tu pedido '{pedido}' ha sido realizado.")

    def cambiar_notificador(self, nuevo_notificador):
        self.notificador = nuevo_notificador
        print(f"Notificador cambiado a: {type(nuevo_notificador).__name__} ")

    def pedido_saliendo(self, pedido):
        print(f"Pedido saliendo: {pedido}")
        self.notificador.enviar_notificacion(f"Tu pedido '{pedido}' está saliendo.")

    def pago(self, pedido, metodo_pago):
        print(f"Procesando pago para el pedido: {pedido}")
        metodo_pago(pedido) 

class SistemaPago:
    @staticmethod
    def pago_tarjeta(pedido):
        print(f"Pago con tarjeta procesado para el pedido: {pedido}")

    @staticmethod
    def pago_paypal(pedido):
        print(f"Pago con PayPal procesado para el pedido: {pedido}")


# Ejemplo de uso
notificador_whatsapp = NotificadorWhatsApp()
notificador_email = NotificadorEmail()
notificador_sms = NotificadorSMS()

app = AppComida(notificador_whatsapp)
app.realizar_pedido("Pizza Margherita")
app.pago("Pizza Margherita", SistemaPago.pago_tarjeta)
app.pedido_saliendo("Pizza Margherita")

print("\nCambiando notificador a Email...\n")
app.cambiar_notificador(notificador_email)
app.realizar_pedido("Sushi")
app.pago("Sushi", SistemaPago.pago_paypal)
app.pedido_saliendo("Sushi")
