import time
class Procesar():

    def ProcesarArchivoXML(self,ArchivoXML):#referencia a todas los datos con su respectiva etiqueta dentro del archivo
        matrices=ArchivoXML.getElementsByTagName("matriz")  #toma todas las matrices(con etiqueta matriz), elemento Raiz
        datos=ArchivoXML.getElementsByTagName("dato")       #toma todos los datos(con etiqueta dato)
        iterador=0

        for matriz in matrices: #Se obtiene un dato en especifico dentro del archivo
            NombreMatriz=matriz.getAttribute("nombre")  #obtiene el dato del atributo de una etiqueta
            Fila=int(matriz.getAttribute("n"))
            Columna=int(matriz.getAttribute("m"))
            
            print("nombre matriz:%s" % NombreMatriz)
            print("Filas:",str(Fila))
            print("columnas:",str(Columna))

            contador=(Fila*Columna)+iterador
            #print("contador: "+str(contador))

            #Se obtiene cada valor del atributo x,y
            ListaDatosXML=[]
            MatrizDatosXML=[]
            while iterador < contador: 
                dato=datos[iterador]
                ValorX=int(dato.getAttribute("x"))
                ValorY=int(dato.getAttribute("y"))

                if ValorX<=Fila and ValorY<=Columna:
                    #print("x:%s " % ValorX +"y:%s " % ValorY + "dato:%s " % dato.firstChild.data)
                    ListaDatosXML.append(int(dato.firstChild.data))

                    if ValorY==Columna:
                        MatrizDatosXML.append(ListaDatosXML)
                        ListaDatosXML=[]

                iterador+=1

            print("\nMATRIZ NORMAL")
            for fila in MatrizDatosXML:
                print(fila)

            #crea la matriz binaria
            matriz_Intercambio=[]
            lista_Intercambio=[]

            for fila in MatrizDatosXML:
                for elemento in fila:
                    if elemento > 0:
                        lista_Intercambio.append(1)
                    else:
                        lista_Intercambio.append(0)  

                matriz_Intercambio.append(lista_Intercambio)
                lista_Intercambio=[]

            print("\nMatriz BINARIA")
            for fila in matriz_Intercambio:
                    print(fila)
            print("\n")
            #Verificar y sumar filas de matrizXML---------------------------------------------------------------
            banderaFinalizar=False
            banderaNoMatch=False
            CantCoinciden=0
            FilaTemporal=0
            ListaFilasIguales=[]
            MatrizAuxIguales=[]
            AumentarFila=1
            while banderaFinalizar==False:
                for i in range(Fila):
                    for j in range(Columna):
                        #print("Fijo:["+str(FilaTemporal)+"]["+str(j)+"]--Movible:["+str(i+AumentarFila)+"]["+str(j)+"]")
                        if i+AumentarFila>=Fila:
                            #print("Se pasa")
                            break
                        elif matriz_Intercambio[FilaTemporal][j]==matriz_Intercambio[i+AumentarFila][j]:
                            CantCoinciden+=1
                        else:
                            #print("No coinciden")
                            CantCoinciden=0
                            break    
                    
                    if CantCoinciden==Columna:
                        #print("coinciden")
                        if FilaTemporal not in ListaFilasIguales:
                            ListaFilasIguales.append(FilaTemporal)
                        ListaFilasIguales.append(i+AumentarFila)
                        CantCoinciden=0
                
                FilaTemporal+=1
                AumentarFila+=1
                if ListaFilasIguales !=[]:
                    MatrizAuxIguales.append(ListaFilasIguales)
                    ListaFilasIguales=[]

                if FilaTemporal>=Fila or AumentarFila>=Fila:
                    banderaFinalizar=True

            print("\n--->>>filas que coinciden<<<---")
            for linea in MatrizAuxIguales:
                print(linea)
            print("mostro...coiciden")
            #Eliminar filas repetidas dentro de MatrizAuxIguales----------------------------------
            if MatrizAuxIguales!=[]:
                band1=True
                band2=True
                i=1
                j=0
                Temporal_i=0
                Temporal_j=0
                while band1:
                    while band2:
                        if i == len(MatrizAuxIguales):
                            #print("entro break 1")
                            break

                        #print("Temporal:["+str(Temporal_i)+"]["+str(Temporal_j)+"]--Movible:["+str(i)+"]["+str(j)+"]")    
                        if MatrizAuxIguales[Temporal_i][Temporal_j]==MatrizAuxIguales[i][j]:
                            #print("elimina")
                            MatrizAuxIguales.remove(MatrizAuxIguales[i])
                            j=0
                        else:
                            j+=1
                            if j==len(MatrizAuxIguales[i]):
                                Temporal_j+=1
                                j=0
                                if Temporal_j>=len(MatrizAuxIguales[Temporal_i]):
                                    i+=1
                                    Temporal_j=0
                    Temporal_i+=1
                    Temporal_j=0
                    i=Temporal_i+1
                    if Temporal_i == len(MatrizAuxIguales):
                        break
            
            print("\nSIMPLIFICADA")
            for linea in MatrizAuxIguales:
                print(linea)

            if MatrizAuxIguales != []:
                #Suma las filas correspondientes-------------------------------------------------------
                listaResultadoSumas=[]
                MatrizReducida=[]
                ListaTemporal=[]
                Resultadosuma=0
                
                for listasSumar in MatrizAuxIguales:
                    for UbicarLista in listasSumar:
                        ListaTemporal.append(MatrizDatosXML[UbicarLista])
                        
                    for Posicion_j in range(len(ListaTemporal[0])): #columnas de MatrizAuxIguales
                        for Posicion_i in range(len(ListaTemporal)):    #Filas de MatrizAuxIguales
                            Resultadosuma+=ListaTemporal[Posicion_i][Posicion_j]    

                        listaResultadoSumas.append(Resultadosuma)
                        Resultadosuma=0

                    MatrizReducida.append(listaResultadoSumas)
                    listaResultadoSumas=[]          #Se reinician las listas para poder almacenar la siguiente suma de filas
                    ListaTemporal=[]
                        

                print("\nlistas sumadas")
                for lista in MatrizReducida:
                    print(lista)
                #Agrega las filas que no se sumaron a la MatrizReducida-----------------------------------------------
                ContadorVerificar=0
                for PosicionVerificar in range(len(MatrizDatosXML)): 
                    for VerificarFila in range(len(MatrizAuxIguales)):
                        if PosicionVerificar not in MatrizAuxIguales[VerificarFila]:
                            ContadorVerificar+=1
                            if ContadorVerificar == len(MatrizAuxIguales):
                                ContadorVerificar=0
                                if PosicionVerificar < len(MatrizReducida):
                                    MatrizReducida.insert(PosicionVerificar,MatrizDatosXML[PosicionVerificar])  
                                else:
                                    MatrizReducida.append(MatrizDatosXML[PosicionVerificar])
                        else:
                            ContadorVerificar=0
                            break
            else:
                MatrizReducida=MatrizDatosXML[:]
            
            print("\nMATRIZ FINAL")
            for lista in MatrizReducida:
                print(lista)
            print("------------------------------------\n\n")