import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
import empleado as e
import empleado_util as eu

# Empleados

class App():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Employees")
        self.window.geometry("700x300")

        #Imagen
        #tren = tk.PhotoImage(file='./img/empleados.png') 
        #ttk.Label(self.window, image=tren).grid(column=0,row=0, columnspan=4)

        # Entry (ID)
        ttk.Label(self.window, text="Employee ID").grid(column=0,row=1, sticky="W", ipadx=5, ipady=5)
        self.id = tk.IntVar()        
        ttk.Entry(self.window, textvariable=self.id, width=15).grid(column=1,row=1, sticky="WE", padx=20)         

        # Entry (Nombre)
        ttk.Label(self.window, text="First name").grid(column=0,row=2, sticky="W", ipadx=5, ipady=5)
        self.name = tk.StringVar()
        ttk.Entry(self.window, textvariable=self.name, width=15).grid(column=1, row=2, sticky="WE", padx=20) 

        # Entry (Apellido1)
        ttk.Label(self.window, text="Last name").grid(column=0,row=3, sticky="W", ipadx=5, ipady=5)
        self.last_name = tk.StringVar()
        ttk.Entry(self.window, textvariable=self.last_name, width=15).grid(column=1, row=3, sticky="WE", padx=20) 

        # Radiobutton (Sexo)
        self.gender = tk.StringVar()
        ttk.Label(self.window, text="Gender:").grid(column=0,row=4, sticky="W", ipadx=5, ipady=5)
        ttk.Radiobutton(self.window, text='Male', variable=self.gender, value='male').grid(column=0,row=5, sticky="W", padx=20)
        ttk.Radiobutton(self.window, text='Female', variable=self.gender, value='female').grid(column=1,row=5, sticky="W", padx=20)
        
        # Combobox (Departamento)

        ttk.Label(self.window, text="Department").grid(column=0,row=6, sticky="W", ipadx=5, ipady=5)
        self.department = ttk.Combobox(state="readonly", values=["A", "B", "C", "D"])
        self.department.grid(column=0,row=7, sticky="W", padx=5, pady=5)


        # Entry (Sueldo)
        ttk.Label(self.window, text="Salary").grid(column=0,row=8, sticky="W", ipadx=5, ipady=5)
        self.salary = tk.StringVar()
        ttk.Entry(self.window, textvariable=self.salary, width=15).grid(column=1, row=8, sticky="WE", padx=20) 
                       
        # Botones uwu
        ttk.Button(self.window, text="Add", command=self.agregar).grid(column=0,row=15, sticky="WE", padx=10)
        ttk.Button(self.window, text="Update", command=self.actualizar).grid(column=1,row=15, sticky="WE", padx=10)
        ttk.Button(self.window, text="Delete", command=self.borrar).grid(column=2,row=15, sticky="WE", padx=10)
        ttk.Button(self.window, text="Search", command=self.buscar).grid(column=3,row=15, sticky="WE", padx=10)
        ttk.Button(self.window, text="New", command=self.nuevo).grid(column=0,row=16, columnspan=3, sticky="WE", padx=10)
        ttk.Button(self.window, text="Quit", command= self.window.destroy).grid(column=3,row=16, sticky="WE", padx=10)

        self.nuevo()
        self.window.mainloop()
        
    def agregar(self): 
        empleado = e.Empleado(self.id.get(), self.name.get(), self.last_name.get(), self.gender.get(), self.department.get(), self.salary.get())
        eu.EmpleadoArchivo.agregar(empleado)

    def buscar(self):

        data = eu.EmpleadoArchivo.buscar(self.id.get())
        self.id.set(data.id)
        self.name.set(data.nombre)
        self.last_name.set(data.apellido1)
        self.gender.set(data.sexo) #esto todavia no sirve xd



    def borrar(self):
        pass

    def actualizar(self):
        pass

    def nuevo(self):
        self.id.set("")
        self.name.set("")
        self.last_name.set("")
        self.gender.set("")
        self.department.set("")
        self.salary.set("")

if __name__ == '__main__':
    App()
