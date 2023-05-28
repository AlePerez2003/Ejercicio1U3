import csv
from claseFacultad import Facultad

class ManejadorFacultad:
    __facultades = []
    
    def __init__(self):
        self.__facultades = []
        
    def cargar_facultades(self):
        
        indice = 0
        
        with open('facultades.csv')as file:
            
            reader = csv.reader(file, delimiter = ',')
            
            for fila in reader:
                
                if int(fila[0]) == indice:
                    
                    self.__facultades[indice-1].agregar_carrera(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
                    
                else:
                    
                    unaFacultad = Facultad(fila[0],fila[1],fila[2],fila[3],fila[4])
                    self.__facultades.append(unaFacultad)
                    indice = int(fila[0])
        print('Facultades cargadas con éxito')
        
    def mostrar_carrera(self, cod):
        
        print('Nombre de la Facultad: ' + self.__facultades[cod-1].get_nombre())
        print('Carreras que se dictan:')
        carreras = self.__facultades[cod-1].get_carreras()
        
        for carrera in carreras:
            
            print('- ' + carrera.get_nombre())
            print('Duración: ' + carrera.get_duracion())
            
    def mostrar_datos_nombre(self, pos_f, pos_c):
        
        carrera = self.__facultades[pos_f].get_carrera(pos_c)
        print('Codigo Carrera: ' + carrera.get_cod())
        print('Nombre de la Facultad: ' + self.__facultades[pos_f].get_nombre())
        print('Localidad: ' + self.__facultades[pos_f].get_localidad())
            
    def buscar_facultad(self, nombre):
        
        i = 0
        valor_retorno = -1
        bandera = False
        
        while i < len(self.__facultades) and not bandera:
            
            carreras = self.__facultades[i].get_carreras()
            pos = self.buscar_carrera(nombre, carreras)
            
            if pos != -1:
                
                valor_retorno = i
                bandera = True
                
            else:
                
                i+=1
        self.mostrar_datos_nombre(valor_retorno, pos)
            
    def buscar_carrera(self, nombre, carreras):
        
        i = 0
        valor_retorno = -1
        bandera = False
        
        while i < len(carreras) and not bandera:
            
            if carreras[i].get_nombre() == nombre:
                
                valor_retorno = i
                bandera = True
                
            else:
                
                i+=1
        return valor_retorno