from os import system
from Clase_Procesar import Procesar
from lecturaXML import Lectura
import lecturaXML

system("cls")
opcion=0
ArchivoXML=""

while opcion!=6:
    try:
        ArchivoEntrada=Procesar()
        LeerArchivo=Lectura()
        print("----------MENÚ PRINCIPAL----------")
        print("1).Cargar Archivo")
        print("2).Procesar Archivo")
        print("3).Escribir Archivo Salida")
        print("4).Mostrar Datos del Estudiante")
        print("5).Generar Gráfica")
        print("6).Salir\n")
        opcion=int(input("-->>Ingrese Opción: "))
        print("----------------------------------")

        if opcion==1:
            print("--CARGAR ARCHIVO XML--")
            RutaArchivo=input("Ingrese la ruta del archivo: ")
            if "\\" in RutaArchivo:
                RutaArchivo=RutaArchivo.replace("\\","/") 
                
            ArchivoXML=LeerArchivo.CargarArchivoXML(RutaArchivo)
            #ArchivoXML=lecturaXML.CargarArchivoXML(RutaArchivo)
        elif opcion==2:
            if ArchivoXML != "":
                print("PROCESAR ARCHIVO--")
                #lecturaXML.ProcesarArchivoXML(ArchivoXML)
                ArchivoEntrada.ProcesarArchivoXML(ArchivoXML)
            else:
                print("\nEs necesario cargar Archivo...\n")
        elif opcion==3:
            pass
        elif opcion==4:
            print("----------------------------------")
            print("-->> carnet: 201800665")
            print("-->> nombre: Samuel Alejandro Pajoc Raymundo")
            print('-->> curso: Introducción a la programación y computación 2, sección "A"')
            input("\n   presione ENTER para continuar...\n")
            print("----------------------------------")

        elif opcion==5:
            pass

    except ValueError:
        print("\n>> solo números <<\n")