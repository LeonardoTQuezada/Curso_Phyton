import pathlib

from exploradorArchivos import ExploradorArchivos
from menuExplorador import MenuExplorador




ruta_proyecto = str(pathlib.Path().resolve())
explorador = ExploradorArchivos(ruta_proyecto)

menu = MenuExplorador(explorador)

menu.mostrar_menu()
