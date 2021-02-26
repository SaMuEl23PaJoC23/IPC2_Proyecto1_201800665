from os import system
system("cls")
opcion=0
while opcion!=6:
    try:
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
            print("entro")

    except ValueError:
        print("\n>> solo números <<\n")