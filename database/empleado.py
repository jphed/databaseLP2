class Empleado:
    def __init__(self, id, nombre, apellido1, sexo, departamento, sueldo):
        self.id = id
        self.nombre = nombre
        self.apellido1 = apellido1
        self.sexo = sexo
        self.departamento = departamento
        self.sueldo = sueldo

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        if not isinstance(id, (int)):
            raise TypeError("id debe ser un número")
        if not (id>0 and id <= 100):
            raise ValueError("Valor debe estar entre 1 y 100")
        self.__id = id

    def __str__(self):
        return f"{self.id},{self.nombre},{self.apellido1},{self.sexo},{self.departamento},{self.sueldo}"
    
