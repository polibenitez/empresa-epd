from unittest import TestCase
from mockito import *
from Departamento import *

__author__ = 'usuarioupo'



class TestDepartamento(TestCase):
    def test_get_salario_total(self):
        """
        Comprueba si se calcula correctamente el salario total de los empleados. Utiliza mocks para la simulacion de objetos Empleado.

        :return: Exito/Fracaso de la prueba
        """
        empleado1=mock()
        when(empleado1).getSalario().thenReturn(200)

        empleado2=mock()
        when(empleado2).getSalario().thenReturn(100)

        empleado3=mock()
        when(empleado3).getSalario().thenReturn(300)

        departamento = Departamento('hp',2)
        departamento.aniadir_emp(empleado1)
        departamento.aniadir_emp(empleado2)
        departamento.aniadir_emp(empleado3)

        self.assertEqual(departamento.get_salario_total(),600)

    def test_get_salario_total_mensual(self):
        """
        Comprueba si se calcula correctamente el salario total mensual de los empleados. Utiliza mocks para la simulacion de objetos Empleado.

        :return: Exito/Fracaso de la prueba
        """
        empleado1=mock()
        when(empleado1).get_salario_mensual().thenReturn(40)

        empleado2=mock()
        when(empleado2).get_salario_mensual().thenReturn(30)

        empleado3=mock()
        when(empleado3).get_salario_mensual().thenReturn(50)


        departamento = Departamento('hp',2)
        departamento.aniadir_emp(empleado1)
        departamento.aniadir_emp(empleado2)
        departamento.aniadir_emp(empleado3)

        self.assertEqual(departamento.get_salario_total_mensual(),120)
