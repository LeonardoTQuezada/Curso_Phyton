from exploradorArchivos import ExploradorArchivos


class MenuExplorador:
    def __init__(self, explorador: ExploradorArchivos):
        self.explorador = explorador

    def mostrar_menu(self):
        while True:
            print("\n--- Menú del Explorador de Archivos ---")
            print("1. Cambiar directorio")
            print("2. Listar contenido")
            print("3. Crear carpeta")
            print("4. Eliminar carpeta")
            print("5. Mover archivo")
            print("6. Copiar archivo")
            print("7. Mostrar ruta actual")
            print("8. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nueva_ruta = input("Ingrese la nueva ruta: ")
                self.explorador.cambiar_directorio(nueva_ruta)
            elif opcion == "2":
                self.explorador.listar_contenido()
            elif opcion == "3":
                nombre_carpeta = input("Ingrese el nombre de la nueva carpeta: ")
                self.explorador.crear_carpeta(nombre_carpeta)
            elif opcion == "4":
                nombre_carpeta = input("Ingrese el nombre de la carpeta a eliminar: ")
                self.explorador.eliminar_carpeta(nombre_carpeta)
            elif opcion == "5":
                archivo_nombre = input("Ingrese el nombre del archivo a mover: ")
                destino = input("Ingrese la ruta de destino: ")
                self.explorador.mover_archivo(archivo_nombre, destino)
            elif opcion == "6":
                archivo_nombre = input("Ingrese el nombre del archivo a copiar: ")
                destino = input("Ingrese la ruta de destino: ")
                self.explorador.copiar_archivo(archivo_nombre, destino)
            elif opcion == "7":
                print(f"Ruta actual: {self.explorador.ruta_actual}")
            elif opcion == "8":
                print("Saliendo del menú.")
                break
            else:
                print("Opción inválida. Intente nuevamente.")