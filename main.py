from menu import Menu
from manejadorFacultad import ManejadorFacultad

if __name__ == '__main__':
    menu = Menu()
    MF = ManejadorFacultad()
    MF.cargar_facultades()
    menu.ejecutar_menu(MF)
    