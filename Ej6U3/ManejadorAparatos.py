from aparatos import Aparatos
from heladera import Heladera
from lavarropas import Lavarropas
from televisor import Televisor
from zope.interface import interface
from zope.interface import implementer
from ClaseNodo import Nodo
from Interface import Interface

@implementer(Interface)
class ListaDefProg:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self)->None:
        self.__comienzo = None
        self.__actual = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual = self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            Aparato=self.__actual.getAparato()
            self.__actual=self.__actual.getSiguiente()
            return Aparato

    def AgregarElemento(self,elemento):
        unNodo=Nodo(elemento)
        unNodo.setSiguiente(self.__comienzo)
        self.__comienzo=unNodo
        self.__actual=unNodo
        self.__tope+=1

    def getCabeza(self):
        print(self.__comienzo.getAparato())
    
    def InsertarElemento(self,elemento,pos):
        try:
            aux=self.__comienzo
            ant=None
            i=1
            while aux!=None and i<=pos:
                if pos==i:
                    if aux==self.__comienzo:
                        self.AgregarElemento(elemento)
                    else:
                        print("\nEntra")
                        unNodo=Nodo(elemento)
                        unNodo.setSiguiente(aux)
                        ant.setSiguiente(unNodo)
                i+=1
                ant=aux
                aux=aux.getSiguiente()
        except IndexError:
            print("\n--Posicion no encontrada\n")

    def CrearAparatos(self,elemento):
        unAparato=None
        if elemento=="heladera":
            unAparato=Heladera(input('\nMarca: '),input('\nModelo: '),input('\nColor: '),input('\nPais de fabricacion: '),input('\nPrecio base: '),int(input('\nCapacidad de litros: ')),input('\nFreezer: [VERDADERO] o [FALSO]: '),input('\nCiclica: '))
        elif elemento=="televisor":
            unAparato=Televisor(input('\nMarca: '),input('\nModelo: '),input('\nColor: '),input('\nPais de fabricacion: '),input('\nPrecio base: '),input('\nIngrese tipo de pantalla: '),input('\nIngrese pulgadas: '),input('\nIngrese tipo de definicion: '),input('\nIngrese conexion: ')) 
        elif elemento=="lavarropas":
            unAparato==Lavarropas(input('\nMarca: '),input('\nModelo: '),input('\nColor: '),input('\nPais de fabricacion: '),input('\nPrecio base: '),input('\nIngrese la capacidad de lavado: '),input('\nIngrese velocidad de centrifugado: '),input('\nIngrese la cantidad de programas: '),input('\nIngrese tipo de carga: '))
        else:
            print('\n--ERROR APARATO DESCONOCIDO--\n')
        return (unAparato)
            
    def __toJSON__(self):
        d=dict(__class__=self.__class__.__name__,
        Aparatos=[aparato.__toJSON__() for aparato in self])
        return d

    def Mostrardatos(self):
        aux=self.__comienzo
        while aux!=None:
            print(aux.getDato())
            aux=aux.getSiguiente()
    
    def MostrarTipo(self,elem):
        aux=self.__comienzo
        encontro=False
        i=1
        while aux!=None and encontro==False:
            if elem==i:
                print(aux.getAparato().__class__.__name__)
                encontro=True
            i+=1
            aux=aux.getSiguiente()

    def MostrarPhillips(self):
        for i in self:
            if i.getMarca().lower()=='phillips':
                print(i.getMarca())
    
    def MostrarMarcaLavarropas(self):
        for i in self:
            if isinstance(i,Lavarropas):
                if i.getTipocarga()=='superior':
                    print(i.getMarca())

    def MostrardatosAparatos(self):
        for i in self:
            print(str(i.__class__.__name__)+''+str(i.getMarca())+''+str(i.getPais())+''+str(i.ImporteVenta()))