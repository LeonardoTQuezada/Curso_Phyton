
# lista = {
#     "comida": 20,
#     "cena": 100,
#     "desayuno":50
# }

# def gastos(lista, max_gasto):
#     gasto_total=0
#     lista_gastos =[]
#     lista_cat = []
#     lista_max = []
#     for clave, valor  in lista.items():
#         gasto_total += valor
#         lista_gastos.append(valor)
#         lista_cat.append(clave)
#         if valor >= max_gasto:
#             lista_max.append(valor)
    
#     max_valor = max(lista_gastos)
#     indice = lista_gastos.index(max_valor)
#     categoria = lista_cat[indice]
#     resumen ={
#         "categoria": categoria,
#         "Gasto total": gasto_total,
#         "Lista gastos max": lista_max
#     }

#     return resumen


# class Gastos:
#     def __init__(self,categoria: str, gasto: float):
#         self.categoria = categoria
#         self.gasto = gasto
    
# class GestorGastos:
#     def __init__(self, lista = []):
#         self.lista = lista
    
#     def addGasto(self,categoria , gasto):
#         nuevo = Gastos(categoria,gasto)
#         for  cat in self.lista:
#             if cat.categoria == categoria:
#                 cat.gasto += gasto 
#                 print(f" Añadido: {categoria} -> {gasto}€ ")
#                 return 
#         self.lista.append(nuevo)
#         print(f" Añadido: {categoria} -> {gasto}€ ")
        
        
#     def deleteGasto (self, categoria):
#         nuevo_lista = []
#         for cat in self.lista:
#             if cat.categoria != categoria:
#                 nuevo_lista.append(cat)   
       
#         self.lista = nuevo_lista
#         print(f"Eliminada la categoría: {categoria}")
        
#     def lista_maxGasto(self, cantidad):
#         resultado = []
#         for cat in self.lista:
#             if cat.gasto > cantidad:
#                 resultado.append(cat)
#         return resultado
    
#     def categoriaMax(self):
#         mayor = self.lista[0]            
#         for cat in self.lista:
#             if cat.gasto > mayor.gasto:   
#                 mayor = cat               
#         print(f"El mayor gasto es {mayor.categoria} con: {mayor.gasto}€")
        
#     def info_gasto(self):
#         for cat in self.lista:
#             print(f"{cat.categoria}: {cat.gasto}€ ")

            
    
# gastos = GestorGastos()

# gastos.addGasto("merienda",40)
# gastos.addGasto("cena",50)
# gastos.addGasto("desayuno",50)
# gastos.addGasto("desayuno",1000)

# gastos.categoriaMax()
# # gastos.info_gasto()
# # gastos.maxGasto(30)
# # gastos.deleteGasto("cena")
# # gastos.info_gasto()

# def deleteGasto (self, categoria):
#         for gasto in self.lista:
#             if gasto.categoria == categoria:
#                 self.lista.remove(gasto)



# Ejercicio 1

# Hacer un sistema de gestión de alumnos donde podamos crear, 
# eliminar y modificar alumnos de un curso de Python
# los alumnos tienen nombre, edad y una descripción

# puntos extra: estos alumnos estudian Python, pero seria 
# genial que el sistema nos permita crear alumnos especiales que estudien PHP, 
# Javascript, Java, ...


class Alumno:
    lenguaje = "Python"
    def __init__(self, nombre: str, edad: int, descripcion: str):
        self.nombre = nombre
        self.edad = edad
        self.descripcion = descripcion

 
    def modificar(self, nombre: str = None, edad: int = None, descripcion: str = None):
        if nombre:
            self.nombre = nombre
        if edad:
            self.edad = edad
        if descripcion:
            self.descripcion = descripcion
        print(f"El alumno {self.nombre} ha sido modificado.")
        
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Descripción: {self.descripcion}. Lenguaje de estudio: {self.lenguaje}")


class AlumnoEspecial(Alumno):
    def __init__(self, nombre: str, edad: int, descripcion: str, lenguaje: str):
        super().__init__(nombre, edad, descripcion)
        self.lenguaje = lenguaje

    def mostrar_info(self):
        super().mostrar_info()


class SistemaGestionAlumnos:
    def __init__(self):
        self.alumnos = []

    def existe_alumno(self, nombre: str):
        for alumno in self.alumnos:
            if alumno.nombre == nombre:
                return alumno
        return None

    def crear_alumno(self, nombre: str, edad: int, descripcion: str):
        if self.existe_alumno(nombre):
            print(f"El alumno {nombre} ya existe.")
            return
        alumno = Alumno(nombre, edad, descripcion)
        self.alumnos.append(alumno)
        print(f"Alumno {nombre} creado.")

    def crear_alumno_especial(self, nombre: str, edad: int, descripcion: str, lenguaje: str):
        if self.existe_alumno(nombre):
            print(f"El alumno {nombre} ya existe.")
            return
        alumno = AlumnoEspecial(nombre, edad, descripcion, lenguaje)
        self.alumnos.append(alumno)
        print(f"Alumno especial {nombre} creado.")

    def eliminar_alumno(self, nombre: str):
        alumno = self.existe_alumno(nombre)
        if alumno:
            self.alumnos.remove(alumno)
            print(f"Alumno {nombre} eliminado.")
        else:
            print(f"No se encontró al alumno {nombre}.")

        

    def modificar_alumno(self, nombre: str, nuevo_nombre: str = None, nueva_edad: int = None, nueva_descripcion: str = None):
        for alumno in self.alumnos:
            if alumno.nombre == nombre:
                alumno.modificar(nuevo_nombre, nueva_edad, nueva_descripcion)
                return
        print(f"No se encontró al alumno {nombre}.")

    def mostrar_alumnos(self):
        for alumno in self.alumnos:
            alumno.mostrar_info()


sistema = SistemaGestionAlumnos()
sistema.crear_alumno("Elena", 20, "Estudiante de Python")
sistema.crear_alumno_especial("María", 22, "Estudiante de PHP", "PHP")
sistema.mostrar_alumnos()   
sistema.crear_alumno("Elena", 20, "Estudiante de Python")
sistema.modificar_alumno("Elena", nueva_edad=21)

sistema.eliminar_alumno("María")

sistema.mostrar_alumnos() 

 