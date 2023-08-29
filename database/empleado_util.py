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
        #opens datos and creates datos2
        filetext = open("datos.txt", "r+")
        new_filetext = open("datos2.txt", "w")
        new_filetext.write("")
        new_filetext.close()

        #const to verify if id is in datos
        c = 0

        for rows in filetext:

            filetext_split = rows.split(",")

            if id != filetext_split[0]:
                c += 1
                new_filetext = open("datos2.txt", "a")
                new_filetext.write(rows)

        if c == 0:
            filetext.close()
            new_filetext.close()
            os.remove("datos2.txt")
            return False
        else:
            filetext.close()
            new_filetext.close()
            os.remove("datos.txt")

            copyable = open("datos2.txt", "r")
            filemodified = open("datos.txt", "a")

            for rowz in copyable:
                filemodified.write(rowz)

            filemodified.close()
            copyable.close()
            os.remove("datos2.txt")
            return True


    @staticmethod
    def actualizar(e:e.Empleado)->None:
        pass