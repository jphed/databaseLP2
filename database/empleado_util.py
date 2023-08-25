import empleado as e
import os

class EmpleadoArchivo:
    @staticmethod
    def agregar(emp:e.Empleado)->None:
        f = open("datos.txt", "a")
        f.write(f"{emp.id},{emp.nombre},{emp.apellido1},{emp.departamento},{emp.sexo},{emp.sueldo}")
        f.close()

    @staticmethod
    def buscar(id:int)->e.Empleado:
        pass

    @staticmethod
    def borrar(id:int)->bool:
        pass

    @staticmethod
    def actualizar(e:e.Empleado)->None:
        pass