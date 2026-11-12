import pathlib
import shutil


class ExploradorArchivos:
    def __init__(self, ruta_inicial):
        self.ruta_actual = pathlib.Path(ruta_inicial)

    def cambiar_directorio(self, nueva_ruta):
        nueva_ruta = pathlib.Path(nueva_ruta)
        if nueva_ruta.is_dir():
            self.ruta_actual = nueva_ruta
            print(f"Directorio cambiado a: {self.ruta_actual}")
        else:
            print("La ruta especificada no es un directorio válido. ")

    def listar_contenido(self):
        print(f"Contenido de {self.ruta_actual}:")
        for item in self.ruta_actual.iterdir():
            print(item.name)

    def crear_carpeta(self, nombre_carpeta):
        nueva_carpeta = self.ruta_actual / nombre_carpeta
        try:
            nueva_carpeta.mkdir()
            print(f"Carpeta '{nombre_carpeta}' creada.")
        except FileExistsError:
            print(f"La carpeta '{nombre_carpeta}' ya existe.")

    def eliminar_carpeta(self, nombre_carpeta):
        carpeta_a_eliminar = self.ruta_actual / nombre_carpeta
        try:
            carpeta_a_eliminar.rmdir()
            print(f"Carpeta '{nombre_carpeta}' eliminada.")
        except FileNotFoundError:
            print(f"La carpeta '{nombre_carpeta}' no existe.")
        except OSError:
            print(f"La carpeta '{nombre_carpeta}' no está vacía y no puede ser eliminada.")

    def mover_archivo(self, archivo_nombre, destino):
        archivo_origen = self.ruta_actual / archivo_nombre
        destino_path = pathlib.Path(destino)
        if archivo_origen.is_file() and destino_path.is_dir():
            shutil.move(str(archivo_origen), str(destino_path))
            print(f"Archivo '{archivo_nombre}' movido a '{destino}'.")
        else:
            print("Archivo o destino inválido.")

    def copiar_archivo(self, archivo_nombre, destino):
        archivo_origen = self.ruta_actual / archivo_nombre
        destino_path = pathlib.Path(destino)
        if archivo_origen.is_file() and destino_path.is_dir():
            shutil.copy(str(archivo_origen), str(destino_path))
            print(f"Archivo '{archivo_nombre}' copiado a '{destino}'.")
        else:
            print("Archivo o destino inválido.")
