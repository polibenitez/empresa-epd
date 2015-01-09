__author__ = 'zadik'

class empresa:
    """
    Modela una empresa

    """
    def __init__(self,nombre_empresa,cif,razon_social):
        """
        Constructor empresa

        :param nombre_empresa:
        :param cif:
        :param razon_social:
        :return: nada
        """
        self.nombre_empresa=nombre_empresa
        self.cif=cif
        self.razon_social=razon_social
        self.lista_depto=[]


