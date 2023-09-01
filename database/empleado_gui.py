import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import empleado as e
import empleado_util as eu
from tkinter import messagebox
from tkinter.simpledialog import askstring
import tkinter.scrolledtext as st

# Empleados

class App():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Employees Manager")
        self.window.geometry("550x500")

        #Imagen
        begula = tk.PhotoImage(file='./img/ez.png') 
        ttk.Label(self.window, image=begula).grid(column=0,row=0, columnspan=4)

        # Entry (ID)
        ttk.Label(self.window, text="Employee ID").grid(column=0,row=1, sticky="W", ipadx=5, ipady=5, padx=10)
        self.id = tk.IntVar()        
        ttk.Entry(self.window, textvariable=self.id, width=15).grid(column=1,row=1, sticky="", padx=20)     

        #next free button
        ttk.Button(self.window, text="Next free ID", command=self.nextidfree).grid(column=3,row=1, sticky="WE", padx=10)

        #generate person button
        ttk.Button(self.window, text="Generate random data", command=self.generatePerson).grid(column=3,row=2, sticky="WE", padx=10)

        #show the list button
        ttk.Button(self.window, text="Show list", command=self.show).grid(column=3,row=3, sticky="WE", padx=10)

        # Entry (Nombre)
        ttk.Label(self.window, text="First name").grid(column=0,row=2, sticky="W", ipadx=5, ipady=5, padx=10)
        self.name = tk.StringVar()
        ttk.Entry(self.window, textvariable=self.name, width=15).grid(column=1, row=2, sticky="WE", padx=20) 

        # Entry (Apellido1)
        ttk.Label(self.window, text="Last name").grid(column=0,row=3, sticky="W", ipadx=5, ipady=5, padx=10)
        self.last_name = tk.StringVar()
        ttk.Entry(self.window, textvariable=self.last_name, width=15).grid(column=1, row=3, sticky="WE", padx=20) 

        # Radiobutton (Sexo)
        self.gender = tk.StringVar()
        ttk.Label(self.window, text="Gender:").grid(column=0,row=4, sticky="W", ipadx=5, ipady=5, padx=10)
        ttk.Radiobutton(self.window, text='Male', variable=self.gender, value='male').grid(column=0,row=5, sticky="W", padx=20)
        ttk.Radiobutton(self.window, text='Female', variable=self.gender, value='female').grid(column=1,row=5, sticky="W", padx=20)
        
        # Combobox (Departamento)

        ttk.Label(self.window, text="Department").grid(column=0,row=6, sticky="W", ipadx=5, padx=10)
        self.department = ttk.Combobox(state="readonly", values=["A", "B", "C", "D"])
        self.department.grid(column=0,row=7, sticky="W", padx=10, pady=5)


        # Entry (Sueldo)
        ttk.Label(self.window, text="Salary").grid(column=0,row=8, sticky="W", ipadx=5, ipady=5, padx=10)
        self.salary = tk.StringVar()
        ttk.Entry(self.window, textvariable=self.salary, width=15).grid(column=1, row=8, sticky="WE", padx=20) 
                       
        # Botones uwu
        ttk.Button(self.window, text="Add", command=self.agregar).grid(column=0,row=15, sticky="WE", padx=10, pady=5)
        ttk.Button(self.window, text="Update", command=self.actualizar).grid(column=1,row=15, sticky="WE", padx=10)
        ttk.Button(self.window, text="Delete", command=self.borrar).grid(column=2,row=15, sticky="WE", padx=10)
        ttk.Button(self.window, text="Search", command=self.buscar).grid(column=3,row=15, sticky="WE", padx=10)
        ttk.Button(self.window, text="Clear", command=self.nuevo).grid(column=0,row=16, columnspan=3, sticky="WE", padx=10)
        ttk.Button(self.window, text="Exit", command= self.window.destroy).grid(column=3,row=16, sticky="WE", padx=10)

        self.nuevo()
        self.window.mainloop()
        
    def agregar(self): 
        data = e.Empleado(self.id.get(), self.name.get(), self.last_name.get(), self.gender.get(), self.department.get(), self.salary.get())
        eu.EmpleadoArchivo.agregar(data)

    def buscar(self):

        employeeID = askstring('EmployeeID', 'Type the employee ID')
        data = eu.EmpleadoArchivo.buscar(int(employeeID))

        if data == None:
            messagebox.showerror("IDnotFound", "Couldn't find employee with such ID")
        else:
            self.id.set(data.id)
            self.name.set(data.nombre)
            self.last_name.set(data.apellido1)
            self.gender.set(data.sexo)
            self.department.set(data.departamento)
            self.salary.set(data.sueldo)
        

    def borrar(self):
        employeeID = askstring('EmployeeID', 'Type the employee ID')
        data = eu.EmpleadoArchivo.borrar(employeeID)

        if data == True:
            messagebox.showinfo(title="Done",message="Employee's Informations was successfully deleted")
        elif data == False:
            messagebox.showerror(title="Error",message="ID doesn't match with any employee")

    def actualizar(self):
        data = e.Empleado(self.id.get(), self.name.get(), self.last_name.get(), self.gender.get(), self.department.get(), self.salary.get())
        eu.EmpleadoArchivo.actualizar(data)

    def nuevo(self):
        self.id.set("")
        self.name.set("")
        self.last_name.set("")
        self.gender.set("")
        self.department.set("")
        self.salary.set("")

    def nextidfree(self):
        data = eu.EmpleadoArchivo.nextfree(1)
        self.id.set(data)

    def generatePerson(self):
        data = eu.EmpleadoArchivo.genPerson()
        self.id.set(data.id)
        self.name.set(data.nombre)
        self.last_name.set(data.apellido1)
        self.gender.set(data.sexo)
        self.department.set(data.departamento)
        self.salary.set(data.sueldo)

    def show(self):
        self.kfc = tk.Tk()
        self.kfc.title("Employees list")
        self.kfc.geometry('1200x600')

        self.scrollt = st.ScrolledText(self.kfc, width = 40, height = 8, font = ("Courier",15))
        self.scrollt.grid(column = 0, row=0, columnspan=3, padx=10, pady=10)
        self.scrollt.pack(side="left", fill="both", expand=True)

        self.scrollt.delete("1.0",tk.END)
        self.scrollt.insert(tk.INSERT, f"ID\t\tNAME\t\tLAST NAME\t\tGENDER\t\tDEPARTMENT\t\tSALARY\n")

        
        filedata = open("datos.txt", "r")

        for row in filedata:
            split_filedata = row.split(",")
            self.scrollt.insert(tk.INSERT, f"{split_filedata[0]}\t\t{split_filedata[1]}\t\t{split_filedata[2]}\t\t{split_filedata[3]}\t\t{split_filedata[4]}\t\t{split_filedata[5]}\n")


        self.scrollt.config(state="disabled")

        
if __name__ == '__main__':
    App()
