menu = {
    1: "1 Suma",
    2: "2 Resta",
    3: "3 Multiplicación",
    4: "4 División",
    5: "5 Salir"
    
}

def ver_menu ():
    texto = "\n\nCalculadora\n\n"
    for m in menu:
        texto += f"{menu[m]}\n"
    print(texto)    
        
        
