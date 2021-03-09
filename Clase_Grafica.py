from graphviz import Digraph
class Grafica():

 def CrearGrafica(self,ListaTodosLosDatos):
    CantMatrices=ListaTodosLosDatos[-1] #Toma el ultimo dato de ListaTodosLosDatos
    PosicionNombre=0
    PosicionMatrizR=1
    Dimenciones=2

    

    for repeticion in range(CantMatrices):
        g=Digraph('G',filename='grafica'+str(repeticion))
        DatoFila=ListaTodosLosDatos[Dimenciones][0]     #Se Re-establece las dimenciones de la nueva matriz
        DatoColumna=ListaTodosLosDatos[Dimenciones][1]
        NombreMatriz=ListaTodosLosDatos[PosicionNombre]
        
        g.node(NombreMatriz,label=NombreMatriz)
        g.node(str(DatoFila),label=str(DatoFila))
        g.node(str(DatoColumna),label=str(DatoColumna))
        g.node('dimencion',label="dimencion")

        g.edge(NombreMatriz,'dimencion')

        g.edge('dimencion', str(DatoColumna))
        g.edge('dimencion', str(DatoFila))
        

        g.node('datos',label='datos')
        g.edge(NombreMatriz,'datos')
            
        
        if DatoFila == 1:
            for NuevaC in range(DatoColumna):
                g.node(str(NuevaC)+'f0',label=str(ListaTodosLosDatos[PosicionMatrizR][0][NuevaC]))
                g.edge('datos',str(NuevaC)+'f0')

        else:
            for nuevaF in range(DatoFila):
                for NuevaC in range(DatoColumna):
                    if nuevaF==0:
                        g.node('c'+str(nuevaF)+str(NuevaC), label=str(ListaTodosLosDatos[PosicionMatrizR][nuevaF][NuevaC]))
                        g.edge('datos','c'+str(nuevaF)+str(NuevaC))
                    
                    else:
                        g.node('c'+str(nuevaF)+str(NuevaC), label=str(ListaTodosLosDatos[PosicionMatrizR][nuevaF][NuevaC]))
                        g.edge('c'+str(nuevaF-1)+str(NuevaC), 'c'+str(nuevaF)+str(NuevaC))
                

        Dimenciones+=4
        PosicionNombre+=4
        PosicionMatrizR+=4
        g.view()