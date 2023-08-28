import empleado as e
import os

class EmpleadoArchivo:
    @staticmethod
    def agregar(emp:e.Empleado)->None:
        f = open("datos.txt", "a")
        f.write(f"{emp.id},{emp.nombre},{emp.apellido1},{emp.departamento},{emp.sexo},{emp.sueldo}\n")
        f.close()

    @staticmethod
    def buscar(id:int)->e.Empleado:
        text_file = open("datos.txt", "r")
        
        for row in text_file:

            list_split = row.split(",")

            if id == int(list_split[0]):
                obj = e.Empleado(int(list_split[0]), list_split[1], list_split[2], list_split[3], list_split[4], list_split[5])
                return obj
                
                
            
        text_file.close()
        
        

        

    @staticmethod
    def borrar(id:int)->bool:
        pass

    @staticmethod
    def actualizar(e:e.Empleado)->None:
        pass