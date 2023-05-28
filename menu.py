from manejadorFacultad import ManejadorFacultad

class Menu:
    __cod: int
    
    def __init__(self, cod = 0):
        self.__cod = cod
        
    def mostrar_menu(self):
        print('Opcion 1: Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad')
        print('Opcion 2: Dado el nombre de una carrera, mostrar código, nombre y localidad de la facultad donde esta se dicta')
        print('Opcion 0: Finalizar operación')
        
    def ejecutar_menu(self, MF:ManejadorFacultad):
        self.mostrar_menu()
        self.__cod = int(input('Ingrese el codigo'))
        while self.__cod != 0:
            if self.__cod == 1:
                self.opcion1(MF)
            elif self.__cod == 2:
                self.opcion2(MF)
            self.mostrar_menu()
            self.__cod = int(input('Ingrese el codigo'))
            
    def opcion1(self, MF):
        cod = int(input('Ingrese el codigo de una facultad'))
        MF.mostrar_carrera(cod)
        
    def opcion2(self, MF):
        nombre = input('Ingrese el nombre de la carrera')
        MF.buscar_facultad(nombre)