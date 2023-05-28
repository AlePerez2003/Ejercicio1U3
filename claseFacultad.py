from claseCarrera import Carrera

class Facultad:
    __cod: str
    __nombre: str
    __direccion: str
    __localidad: str
    __tel: str
    __carreras: list
    
    def __init__(self, cod, nombre, direccion, localidad, tel):
        self.__cod = cod
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__tel = tel
        self.__carreras = []
        
    def agregar_carrera(self, codf, codc, nombre, fecha_inicio, duracion, titulo):
        cod = codf + '.' + codc
        unaCarrera = Carrera(cod, nombre, fecha_inicio, duracion, titulo)
        self.__carreras.append(unaCarrera)
        
    def get_nombre(self):
        return self.__nombre
    
    def get_carreras(self):
        return self.__carreras
    
    def get_carrera(self, pos):
        return self.__carreras[pos]
    
    def get_cod(self):
        return self.__cod
    
    def get_localidad(self):
        return self.__localidad