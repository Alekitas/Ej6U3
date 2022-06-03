from aparatos import Aparatos
import json
from pathlib import Path

class Televisor(Aparatos):
    __tipopantalla=str
    __pulgadas=None
    __tipodefinicion=None
    __conexion=bool
    def __init__(self,marca,modelo,color,pais,precio,tipopantalla,pulgadas,tipodefinicion,conexion):
        super().__init__(marca,modelo,color,pais,precio)
        self.__tipopantalla=tipopantalla
        self.__pulgadas=pulgadas
        self.__tipodefinicion=tipodefinicion
        self.__conexion=conexion
    def getTipopantalla(self):
        return self.__tipopantalla
    def getPulgadas(self):
        return self.__pulgadas
    def getTipodef(self):
        return self.__tipodefinicion
    def getConexion(self):
        return self.__conexion
    def __str__(self):
        return 'Tipo de pantalla: {} Pulgadas: {} Tipo de definicion: {} Conexion: {}'.format(self.__tipopantalla,self.__pulgadas,self.__tipodefinicion,self.__conexion)
    def __toJSON__(self):
        d=dict(__class__=self.__class__.__name__,
        __atributos__=dict(
            marca=self.getMarca(),
            modelo=self.getModelo(),
            color=self.getColor(),
            paisfabr=self.getPais(),
            preciobase=self.getPreciobase(),
            tipopantalla=self.__tipopantalla,
            pulgadas=self.__pulgadas,
            tipodefinicion=self.__tipodefinicion,
            conexion=self.__conexion,
        ))
        return d
    def ImporteVenta(self):
        importe=self.getPreciobase()
        if self.__tipodefinicion=='SD':
            importe+=self.getPreciobase()+(1/100)
        elif self.__tipodefinicion=='HD':
            importe+=self.getPreciobase()+(2/100)
        elif self.__tipodefinicion=='FULL HD':
            importe+=self.getPreciobase()+(3/100)
        elif self.__conexion=='Falso':
            importe+=self.getPreciobase()+(10/100)
        return importe