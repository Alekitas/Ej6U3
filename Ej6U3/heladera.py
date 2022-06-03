from aparatos import Aparatos
from gc import freeze
import json
from pathlib import Path
class Heladera(Aparatos):
    __capacidadlitros=int
    __freezer=str
    __ciclica=str
    def __init__(self,marca,modelo,color,paisfabr,preciobase,capacidadlitros,freezer=False,ciclica=False):
        super().__init__(marca,modelo,color,paisfabr,preciobase)
        self.__capacidadlitros=int(capacidadlitros)
        self.__freezer=freezer
        self.__ciclica=ciclica
    
    def getCapacidad(self):
        return self.__capacidadlitros
    
    def getFreezer(self):
        return self.__freezer
    
    def getCiclica(self):
        return self.__ciclica
    
    def __str__(self):
        return 'Capacidad de litros: {} Frezzer: {} Ciclica: {}'.format(self.__capacidadlitros,self.__freezer,self.__ciclica)
    
    def __toJSON__(self):
        d=dict(__class__=self.__class__.__name__,
        __atributos__=dict(
            marca=self.getMarca(),
            modelo=self.getModelo(),
            color=self.getColor(),
            paisfabr=self.getPais(),
            preciobase=self.getPreciobase(),
            capacidadlitros=self.__capacidadlitros,
            freezer=self.__freezer,
            ciclica=self.__ciclica
            )
        )
        return d

    def ImporteVenta(self):
        importe=self.getPreciobase()
        if self.__freezer==False:
            importe+=self.getPreciobase()+(1/100)
        elif self.__freezer==True:
            importe+=self.getPreciobase()+(5/100)
        elif self.__ciclica==True:
            importe+=self.getPreciobase()+(10/100)
        return importe