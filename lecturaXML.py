from xml.dom import minidom
import time
class Lectura():
        
    def CargarArchivoXML(self,RutaArchivoXML):   #C:/Users/samal/Desktop/lectura xml/Ejemplo_prueba.xml
        try:                                #C:/Users/samal/Desktop/entrada1.xml
            archivoXML=minidom.parse(RutaArchivoXML)    #obtiene el contenido del documento por medio de una ruta
            print("\n>> !!Archivo procesado Exitosamente!! <<\n")
            time.sleep(2)
            return archivoXML
        except FileNotFoundError:
            print("\n>>> Archivo NO existente...<<<\n")
            time.sleep(2)
            archivoXML=""
            return archivoXML