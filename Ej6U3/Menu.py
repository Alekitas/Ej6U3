from ClaseObjectEnconder import ObjectEncoder
from ManejadorAparatos import ListaDefProg
class Menu:
    __opcion = None
    def __init__(self):
        self.__opcion=0
    def Iniciar(self):
        unObjectEncoder=ObjectEncoder()
        unManejadorLista=ListaDefProg()
        
        while self.__opcion!='-1':

            print('=>1-Leer JSON')
            print('=>2-Cargar aparatos')
            print('=>3-Mostrar')
            print('=>4-Insertar un aparato en la coleccion')
            print('=>5-Mostrar tipo de objeto dado una posicion')
            print('=>6-Mostrar cantidad de aparatos marca Phillips')
            print('=>7-Mostrar marca de lavarropas con carga superior')
            print('=>8-Mostrar datos de aparatos de la empresa')
            print('=>9-Guardar objetos en el archivo .json')

            self.__opcion=input('\n==>Ingrese numero de opcion: ')
            if self.__opcion=='1':
                d=unObjectEncoder.LeerJSON('aparatoselectronicos.json')
                unManejadorLista=unObjectEncoder.DecodificarDicc(d)

            elif self.__opcion=='2':
                unAparato=unManejadorLista.CrearAparatos(input('\nIngrese el tipo de aparato'))
                if unAparato!=None:
                    unManejadorLista.AgregarElemento(unAparato)

            elif self.__opcion=='3':
                unManejadorLista.Mostrardatos()

            elif self.__opcion=='4':
                Aparato=unManejadorLista.CrearAparatos(input('\nIngrese el tipo de aparato: '))
                if Aparato!=None:
                    unManejadorLista.InsertarElemento(Aparato,int(input('\nIngrese la posicion a guardar el aparato: ')))

            elif self.__opcion=='5':
                pos=int(input('\nIngresar posicion: '))
                unManejadorLista.MostrarTipo(pos)

            elif self.__opcion=='6':
                unManejadorLista.MostrarPhillips()

            elif self.__opcion=='7':
                unManejadorLista.MostrarMarcaLavarropas()

            elif self.__opcion=='8':
                unManejadorLista.MostrardatosAparatos()
            
            elif self.__opcion=='9':
                unObjectEncoder.GuardarJSON(unManejadorLista.__toJSON__(),'aparatoselectronicos.json')
                print('\--OBJETOS GUARDADOS--')