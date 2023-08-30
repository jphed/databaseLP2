import empleado as e
import os
from tkinter import messagebox
import random

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

        filetext = open("datos.txt", "r")
        #new_filetext = open("datos2.txt", "w")
        #new_filetext.close()
        new_filetext = open("datos2.txt", "a")

        for row in filetext:

            filetext_split = row.split(",")

            if filetext_split[0] != str(e.id):
                new_filetext.write(row)
            else:
                new_filetext.write(f"{e.id},{e.nombre},{e.apellido1},{e.sexo},{e.departamento},{e.sueldo}")

        filetext.close(); new_filetext.close()
        os.remove("datos.txt")

        copyable = open("datos2.txt", "r")
        new_main_textfile = open("datos.txt", "a")

        for i in copyable:
            new_main_textfile.write(i)

        copyable.close(); new_main_textfile.close()
        os.remove("datos2.txt")

        messagebox.showinfo(message="Employee successfully updated", title="update")


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

    @staticmethod
    def genPerson()->e.Empleado:

        #Name and last name randomizer
        filetext = open("names.txt", "r")
        txtlist = []
        c = 0
        for row in filetext:
            c += 1
            split = row.split()
            txtlist.append(split)

        x = random.randint(0,c)
        y = random.randint(0,c)

        a = txtlist[x]
        b = txtlist[y]

        nameGend = ' '.join(a)
        lastnameGend = ' '.join(b)
        


        


        print(nameGend, lastnameGend)

        #Gender randomizer
        amogus = random.randint(0,1)
        if amogus == 0:
            gendergend = "male"
        else:
            gendergend = "female"

        #department randomizer
        sugoma = random.randint(0,3)
        if sugoma == 0:
            departmentGend = 'A'
        elif sugoma == 1:
            departmentGend = 'B'
        elif sugoma == 2:
            departmentGend = 'C'
        elif sugoma == 3:
            departmentGend = 'D'
        
        #salary randomizer

        begula = random.randint(100,1000)
        salaryGend = begula
        
        #id Randomizer
        filetext = open("datos.txt", "r")
        idList = []

        for row in filetext:
            filetext_split = row.split(",")
            idList.append(filetext_split[0])
        

        idGend = random.randint(1,100)
        while str(idGend) in idList:
            idGend = random.randint(1,100)

        
        data = e.Empleado(idGend,nameGend,lastnameGend, gendergend, departmentGend, salaryGend)
        return data


    
        

