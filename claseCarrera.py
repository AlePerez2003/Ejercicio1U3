class Carrera:
    __cod: str
    __nombre: str
    __fecha_inicio: str
    __duracion: str
    __titulo: str
    
    def __init__(self, cod, nombre, fecha_inicio, duracion, titulo):
        self.__cod = cod
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__duracion = duracion
        self.__titulo = titulo
    
    def get_nombre(self):
        return self.__nombre
        
    def get_duracion(self):
        return self.__duracion
    
    def get_cod(self):
        return self.__cod