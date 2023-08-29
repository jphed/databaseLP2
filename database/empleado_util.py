import empleado as e
import os

class EmpleadoArchivo:
    @staticmethod
    def agregar(emp:e.Empleado)->None:
        f = open("datos.txt", "a")
        f.write(f"{emp.id},{emp.nombre},{emp.apellido1},{emp.sexo},{emp.departamento},{emp.sueldo}\n")
        f.close()

    @staticmethod
    def buscar(id:int)->e.Empleado:
        text_file = open("datos.txt", "r")
        
        for row in text_file:

            list_split = row.split(",")

            if id == int(list_split[0]):
                obj = e.Empleado(int(list_split[0]), list_split[1], list_split[2], list_split[3], list_split[4], list_split[5])
                text_file.close()
                return obj
        
        text_file.close()
        return None
        
    @staticmethod
    def borrar(id:int)->bool:

        text_file = open("datos.txt", "r")
        
        for row in text_file:

            list_split = row.split(",")

            if id == int(list_split[0]):
                text_file.close()
                return True
            
        text_file.close() 
        return False


    @staticmethod
    def actualizar(e:e.Empleado)->None:
        pass