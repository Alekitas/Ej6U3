import json
from aparatos import Aparatos
from pathlib import Path
from gc import freeze
class Lavarropas(Aparatos):
    __capacidadlavado=None
    __velcentrif=None
    __cantprog=None
    __tipocarga=None
    def __init__(self,marca,modelo,color,pais,precio,capacidadlavado,velcentrif,cantprog,tipocarga):
        super().__init__(marca,modelo,color,pais,precio)
        self.__capacidadlavado=capacidadlavado
        self.__velcentrif=velcentrif
        self.__cantprog=cantprog
        self.__tipocarga=tipocarga
    def getCapacidad(self):
        return self.__capacidadlavado
    def getVelocidad(self):
        return self.__velcentrif
    def getCantprog(self):
        return self.__cantprog
    def getTipocarga(self):
        return self.__tipocarga
    def __str__(self):
        return 'Capacidad: {} Velocidad: {} Cantidad de programas: {} Tipo de Carga: {}'.format(self.__capacidadlavado,self.__velcentrif,self.__cantprog,self.__tipocarga)
    def __toJSON__(self):
        d=dict(__class__=self.__class__.__name__,
        __atributos__=dict(
            marca=self.getMarca(),
            modelo=self.getModelo(),
            color=self.getColor(),
            pais=self.getPais(),
            precio=self.getPrecio(),
            capacidadlavado=self.__capacidadlavado,
            velcentrif=self.__velcentrif,
            cantprog=self.__cantprog,
            tipocarga=self.__tipocarga
        ))
        return d
    def ImporteVenta(self):
        importe=self.getPreciobase()
        if self.__capacidadlavado<=5:
            importe+=self.getPreciobase()+(1/100)
        elif self.__capacidadlavado>5:
            importe+=self.getPreciobase()+(5/100)
        return importe