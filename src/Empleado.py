__author__ = 'usuarioupo'

class Empleado:
    """
    Modela un empleado

    """
    def __init__(self,nombre,apellidos,dni,direccion,edad,salario,email):
        """
        Constructor de empleado

        :param nombre:
        :param apellidos:
        :param dni:
        :param direccion:
        :param edad:
        :param salario:
        :param email:
        :return:
        """
        self.nombre=nombre
        self.apellidos=apellidos
        self.dni=dni
        self.direccion=direccion
        self.edad=edad
        self.salario
        self.email=email

    def getSalario(self):
        """

        :return: Salario
        """
        return self.salario

    def get_dni(self):
        """

        :return: Dni
        """
        return self.dni

    def get_nombre_apellidos(self):
        """

        :return: nombre completo
        """
        return self.nombre + " " + self.apellidos

    def get_edad(self):
        """

        :return: Edad
        """
        return self.edad

    def get_email(self):
        """

        :return: Email
        """
        return self.email

    def get_direccion(self):
        """

        :return: direccion
        """
        return self.direccion

    def get_salario_mensual(self):
        """

        :return: devuelve el salario mensual
        """
        return self.salario/12

