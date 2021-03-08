import xml.etree.cElementTree as ET
class Escribir():

    def EscribirNuevoXML(self, RutaNuevoXML, ListaTodosLosDatos):
        CantMatrices=ListaTodosLosDatos[-1] #Toma el ultimo dato de ListaTodosLosDatos
        PosicionNombre=0
        PosicionMatrizR=1
        PosicionFrecuencia=3
        Dimenciones=2   #posicion en que inicia el primer par de dimenciones
        if len(ListaTodosLosDatos)>4:
            SiguienteGrupo=4
        else:
            SiguienteGrupo=0

        Etiqueta_Matrices=ET.Element("matrices")
           
        for repetir in range(CantMatrices):
            DatoFila=ListaTodosLosDatos[Dimenciones][0]     #Se Re-establece las dimenciones de la nueva matriz
            DatoColumna=ListaTodosLosDatos[Dimenciones][1]

            #Se crea la etiqueta "matriz", y se le agregan sus atributos(nombre y dimenciones)
            Etiqueta_Matriz=ET.SubElement(Etiqueta_Matrices,"matriz",nombre=ListaTodosLosDatos[PosicionNombre]+"_Salida",n=str(DatoFila),m=str(DatoColumna),g=str(len(ListaTodosLosDatos[PosicionFrecuencia])))

            #Se crea cada etiqueta "dato", y se le agregan sus atributos(n-fila, m-columna)
            for NuevaFila in range(DatoFila):
                for NuevaColumna in range(DatoColumna):
                    dato=ET.SubElement(Etiqueta_Matriz,"dato",x=str(NuevaFila+1), y=str(NuevaColumna+1)).text=str(ListaTodosLosDatos[PosicionMatrizR][NuevaFila][NuevaColumna])
            
            for fElemento in ListaTodosLosDatos[PosicionFrecuencia]: 
                frecuencia=ET.SubElement(Etiqueta_Matriz,"frecuencia",g=str(fElemento[0]+1)).text=str(fElemento[1])
                
            Dimenciones+=4
            PosicionNombre+=4
            PosicionMatrizR+=4
            PosicionFrecuencia+=4

        #Se escribe y genera el nuevo archivo XML  
        NuevoArchivoXML=ET.ElementTree(Etiqueta_Matrices)
        NuevoArchivoXML.write(RutaNuevoXML)

