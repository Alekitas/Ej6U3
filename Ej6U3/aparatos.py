import abc
from abc import ABC
import json
class Aparatos(ABC):
    __marca=str
    __modelo=str
    __color=str
    __paisfabr=str
    __preciobase=float
    def __init__(self,marca,modelo,color,paisfabr,preciobase):
        self.__marca=marca
        self.__modelo=modelo
        self.__color=color
        self.__paisfabr=paisfabr
        self.__preciobase=float(preciobase)
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getColor(self):
        return self.__color
    def getPais(self):
        return self.__paisfabr
    def getPreciobase(self):
        return self.__preciobase
    def __str__(self)->str:
        return 'Marca: {} Modelo: {} Color: {} Pais de fabricacion: {} Preciobase: {}'.format(self.__marca,self.__modelo,self.__color,self.__paisfabr,self.__preciobase)
    @abc.abstractclassmethod
    def ImporteVenta(self):
        pass