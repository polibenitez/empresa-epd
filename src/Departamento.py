__author__ = 'usuarioupo'

class Departamento:
    """
    Modela un Departamento

    """
    def __init__(self,nombre_depto,id_depto):
        """
        Constructor departamento

        :param nombre_depto:
        :param id_depto:
        :return:
        """
        self.nombre_depto=nombre_depto
        self.id_depto=id_depto
        self.lista_emp=[]

    def aniadir_emp(self,Empleado):
        """
        Anade empleado a la lista de empleados

        :param Empleado:
        :type Empleado: objeto  empleado
        :return: no devuelve nada
        """
        self.lista_emp.append(Empleado)

    def get_salario_total(self):
        """
        Recorre la lista de empleados obteniendo su salario

        :return: salario total de los empelados de la empresa
        """
        total=0
        for i in self.lista_emp:
            total+=i.getSalario()
        return total

    def get_nombre_depto(self):
        """

        :return: nombre del departamento
        """
        return self.nombre_depto

    def get_salario_total_mensual(self):
        """
        Recorre la lista de empleados obteniendo su salario mensual

        :return: salario total mensual de los empleados
        """
        total=0
        for i in self.lista_emp:
            total+=i.get_salario_mensual()
        return total



