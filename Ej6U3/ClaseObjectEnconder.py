import json
from pathlib import Path
from ManejadorAparatos import ListaDefProg
from heladera import Heladera
from lavarropas import Lavarropas
from televisor import Televisor

class ObjectEncoder:
    def DecodificarDicc(self,d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_=eval(class_name)
            if class_name=='ListaDefProg':
                listaAparatos=d['Aparatos']
                ManejadorAparatos=class_()
                dAparato=listaAparatos[0]
                for i in range(len(listaAparatos)):
                    dAparato=listaAparatos[i]
                    class_name=dAparato.pop('__class__')
                    class__=eval(class_name)
                    atributos=dAparato['__atributos__']
                    unAparato=class__(**atributos)
                    ManejadorAparatos.AgregarElemento(unAparato)
            return ManejadorAparatos
            
    def GuardarJSON(self,diccionario,archivo):
        with Path(archivo).open("w",encoding="UTF-8") as destino:
            json.dump(diccionario,destino,indent=4)
            destino.close()

    def LeerJSON(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario

    def convertirTextoaDiccionario(self,texto):
        return json.loads(texto)        