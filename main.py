from os import system
from main_lista import ListaCircularSimple
from Clase_Procesar import Procesar
from Clase_EscribirXML import Escribir
from Clase_Grafica import Grafica
from lecturaXML import Lectura
import time

system("cls")
opcion=0
ArchivoXML=""
DatosProcesados=""
proceder=False

while opcion!=6:
    try:
        ArchivoEntrada=Procesar()
        LeerArchivo=Lectura()
        EscribirNuevo=Escribir()
        GraficaNueva=Grafica()
        ListaNuevaC=ListaCircularSimple()

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
            if ".xml" in RutaArchivo:
                if "\\" in RutaArchivo:
                    RutaArchivo=RutaArchivo.replace("\\","/") 
                    
                ArchivoXML=LeerArchivo.CargarArchivoXML(RutaArchivo)
                proceder=False
            else:
                print("\nruta No valida...\n")
                time.sleep(2)
            
        elif opcion==2:
            if ArchivoXML != "":
                print("--PROCESAR ARCHIVO--")
                TodosLosDatosProcesados=ArchivoEntrada.ProcesarArchivoXML(ArchivoXML)
                #ListaNuevaC.Lista_CircularS(TodosLosDatosProcesados)
                proceder=True
            else:
                print("\nEs necesario cargar Archivo...\n")
                time.sleep(2)

        elif opcion==3:
            if proceder==True:
                print("--ESCRIBIR ARCHIVO SALIDA--")
                RutaNuevoXML=input("ingrese la ruta de salida: ")
                if ".xml" in RutaNuevoXML:
                    if "\\" in RutaNuevoXML:
                        RutaNuevoXML=RutaNuevoXML.replace("\\","/")
                    EscribirNuevo.EscribirNuevoXML(RutaNuevoXML,TodosLosDatosProcesados)
                else:
                    print("\nruta No valida...\n")
                    time.sleep(2)
            else:
                print("\nEs necesario PROCESAR Archivo...\n")    
                time.sleep(2)


        elif opcion==4:
            print("----------------------------------")
            print("-->> carnet: 201800665")
            print("-->> nombre: Samuel Alejandro Pajoc Raymundo")
            print('-->> curso: Introducción a la programación y computación 2, sección "A"')
            input("\n   presione ENTER para continuar...\n")
            print("----------------------------------")

        elif opcion==5:
            if proceder ==True:
                GraficaNueva.CrearGrafica(TodosLosDatosProcesados)
            else:
                print("\nEs necesario PROCESAR Archivo...\n")
                time.sleep(2)

    except ValueError:
        print("\n>> solo números <<\n")