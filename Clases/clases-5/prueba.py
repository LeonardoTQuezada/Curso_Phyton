
lista = {
    "comida": 20,
    "cena": 100,
    "desayuno":50
}

def gastos(lista, max_gasto):
    gasto_total=0
    lista_gastos =[]
    lista_cat = []
    lista_max = []
    for clave, valor  in lista.items():
        gasto_total += valor
        lista_gastos.append(valor)
        lista_cat.append(clave)
        if valor >= max_gasto:
            lista_max.append(valor)
    
    max_valor = max(lista_gastos)
    indice = lista_gastos.index(max_valor)
    categoria = lista_cat[indice]
    resumen ={
        "categoria": categoria,
        "Gasto total": gasto_total,
        "Lista gastos max": lista_max
    }

    return resumen


class Gastos:
    def __init__(self,categoria: str, gasto: float):
        self.categoria = categoria
        self.gasto = gasto
    
class GestorGastos:
    def __init__(self, lista = []):
        self.lista = lista
    
    def addGasto(self,categoria , gasto):
        nuevo = Gastos(categoria,gasto)
        for  cat in self.lista:
            if cat.categoria == categoria:
                cat.gasto += gasto 
                print(f" Añadido: {categoria} -> {gasto}€ ")
                return 
        self.lista.append(nuevo)
        print(f" Añadido: {categoria} -> {gasto}€ ")
        
        
    def deleteGasto (self, categoria):
        nuevo_lista = []
        for cat in self.lista:
            if cat.categoria != categoria:
                nuevo_lista.append(cat)   
       
        self.lista = nuevo_lista
        print(f"Eliminada la categoría: {categoria}")
        
    def lista_maxGasto(self, cantidad):
        resultado = []
        for cat in self.lista:
            if cat.gasto > cantidad:
                resultado.append(cat)
        return resultado
    
    def categoriaMax(self):
        mayor = self.lista[0]            
        for cat in self.lista:
            if cat.gasto > mayor.gasto:   
                mayor = cat               
        print(f"El mayor gasto es {mayor.categoria} con: {mayor.gasto}€")
        
    def info_gasto(self):
        for cat in self.lista:
            print(f"{cat.categoria}: {cat.gasto}€ ")

            
    
gastos = GestorGastos()

gastos.addGasto("merienda",40)
gastos.addGasto("cena",50)
gastos.addGasto("desayuno",50)
gastos.addGasto("desayuno",1000)

gastos.categoriaMax()
# gastos.info_gasto()
# gastos.maxGasto(30)
# gastos.deleteGasto("cena")
# gastos.info_gasto()

def deleteGasto (self, categoria):
        for gasto in self.lista:
            if gasto.categoria == categoria:
                self.lista.remove(gasto)