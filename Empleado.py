__author__ = 'usuarioupo'

class Empleado:
    def __init__(self,nombre,apellidos,dni,direccion,edad,salario,email):
        self.nombre=nombre
        self.apellidos=apellidos
        self.dni=dni
        self.direccion=direccion
        self.edad=edad
        self.salario
        self.email=email

    def getSalario(self):
        return self.salario

    def get_dni(self):
        return self.dni

    def get_nombre_apellidos(self):
        return self.nombre + " " + self.apellidos

    def get_edad(self):
        return self.edad

    def get_email(self):
        return self.email

    def get_direccion(self):
        return self.direccion

    def get_salario_mensual(self):
        return self.salario/12

