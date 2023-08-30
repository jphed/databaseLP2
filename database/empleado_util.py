import empleado as e
import os
from tkinter import messagebox

class EmpleadoArchivo:
    @staticmethod
    def agregar(emp:e.Empleado)->None:

        verify = open("datos.txt", "r")
        id_in_use = False
        for row in verify:

            verify_split = row.split(",")
            if emp.id == int(verify_split[0]):
                id_in_use = True

        verify.close()

        if id_in_use == True:
            messagebox.showerror(title="Error", message="ID is already in use")
        else:
            f = open("datos.txt", "a")
            f.write(f"{emp.id},{emp.nombre},{emp.apellido1},{emp.sexo},{emp.departamento},{emp.sueldo}\n")
            f.close()
            messagebox.showinfo(title="Addition", message="user was successfully added")

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

        #const to verify if id is in datos.txt
        c = 0; k = 0

        for rows in filetext:
            c += 1
            filetext_split = rows.split(",")
        
            if id != filetext_split[0]:
                k += 1
                new_filetext = open("datos2.txt", "a")
                new_filetext.write(rows)
        
        if c == k:
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

    @staticmethod
    def nextfree(num:int)->int:
        filetext = open("datos.txt", "r")
        IDlist = []
        statement = True
        for row in filetext:
            filetext_split = row.split(",")
            IDlist.append(filetext_split[0])

        filetext.close()

        while statement:
            if str(num) in IDlist:
                num += 1
            else:
                statement = False
                return int(num)

            


