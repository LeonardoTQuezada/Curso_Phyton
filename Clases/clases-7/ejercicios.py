# Ejercicios propuestos - Clase 7
# Intenta resolverlos sin mirar soluciones externas. Son ligeramente más difíciles que el temario.

# Ejercicio 1: Agenda de recordatorios con datetime
# Crea una clase Agenda que almacene recordatorios como una lista de diccionarios
# {titulo, fecha (datetime), prioridad (1-3)}.
# Implementa los métodos:
# - añadir(titulo, fecha_str, prioridad): parsea la fecha con strptime
# - proximos(dias=7): devuelve los recordatorios en los próximos N días, ordenados por fecha
# - vencidos(): devuelve los recordatorios cuya fecha ya pasó
# - resumen(): imprime con pprint un informe agrupado por prioridad
# Usa collections.defaultdict para agrupar y datetime para comparar fechas.


# Ejercicio 2: Validador y extractor de datos con re
# Crea un módulo con las siguientes funciones de validación, cada una usando re:
# - validar_email(s): True si es un email válido (usuario@dominio.extensión)
# - validar_telefono(s): True si es un teléfono español válido (9 dígitos, puede llevar +34)
# - validar_fecha(s): True si tiene formato DD/MM/YYYY y la fecha es real
# - extraer_urls(texto): devuelve lista de URLs (http/https) presentes en el texto
# - censurar_emails(texto): reemplaza emails por "****@****.***"
# Prueba cada función con al menos 3 casos válidos y 3 inválidos.


# Ejercicio 3: Benchmark de funciones con functools y time
# Implementa un decorador benchmark(repeticiones=100) usando functools.wraps que:
# - Ejecute la función decorada N veces
# - Mida el tiempo total y medio con time.perf_counter()
# - Imprima el informe formateado con el nombre de la función, tiempo total y medio
# Aplícalo a tres funciones distintas que hagan cálculos pesados (ej: fibonacci recursivo,
# ordenar listas grandes, contar frecuencias de letras en texto largo).
# Compara los tiempos con y sin lru_cache para la función de fibonacci.


# Ejercicio de fechas:
 
# Crear una función que nos permita calcular cuantos días quedan hasta nuestro aniversario 
# (si no tenemos aniversario, hasta san valentin)
 
# si quedan menos de 10 días, debería apurarnos a comprar un regalo y a preparar algo especial!

# ademas, crear una segunda función que nos permita cambiar cuando es nuestro aniversario (o dia de san valentin)
 
# truco: tendremos que usar correctamente el scope y tendremos que tener un bucle para que el usuario vaya jugando con las fechas)
 
# from datetime import datetime, date

# def dias_hasta_aniversario(aniversario=None):
#     nombre = "tu aniversario"
#     if not aniversario:
#         aniversario = date(date.today().year + 1, 2, 14)  
#         nombre = f"San Valentín"
#     else:
#         aniversario = datetime.strptime(aniversario, "%d/%m/%Y").date()
       
#     hoy = date.today()
#     dias = (aniversario - hoy).days

#     return nombre, dias

# def cambiar_aniversario():
#     while True:
#         nombre, dias = dias_hasta_aniversario()
        
#         nueva_fecha = input("Introduce la nueva fecha (DD/MM/YYYY), Enter para San Valentín o 'salir': ").strip()
#         if nueva_fecha.lower() == 'salir':
#             break
#         try:
#             nombre, dias_restantes = dias_hasta_aniversario(nueva_fecha)

#             if dias_restantes < 0:
#                 print("Esa fecha ya ha pasado. Introduce una fecha futura.")
#             else:
#                 print(f"Quedan {dias_restantes} días hasta {nombre}.")
#                 if dias_restantes < 10:
#                     print("¡Apúrate a comprar un regalo y a preparar algo especial!")
                    
#         except ValueError:
#             print("Formato de fecha incorrecto. Por favor, usa DD/MM/YYYY.")


# cambiar_aniversario() 