import menu
import operaciones
import ingresos

while True:
    menu.ver_menu()
    opcion = int(input("Ingresa una opción: "))
    if opcion == 5:
        print("¡Hasta luego!")
        break
    n1 = ingresos.ingresaNumeros(1)
    n2 = ingresos.ingresaNumeros(2)
    if opcion == 1:
        print( f"el resultado de la suma es {operaciones.suma(n1,n2)}")
    elif opcion == 2:
        print( f"el resultado de la resta es {operaciones.resta(n1,n2)}")
    elif opcion == 3:
            print( f"el resultado de la multiplicación es {operaciones.multiplicacion(n1,n2)}")
    elif opcion == 4:
            print( f"el resultado de la divisiónes {operaciones.division(n1,n2)}")
    else:
        break