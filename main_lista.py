from Clase_lista_circular import Lista_Circular

class ListaCircularSimple():

    def ListaCircularS(self,TodosLosDatos):
        cantMatrices=TodosLosDatos[-1]
        lista=Lista_Circular()

        lista.Agregar_Al_Final(1)
        lista.Agregar_Al_Inicio(20)
        lista.Agregar_Al_Final(2)
        lista.Agregar_Al_Inicio(11)

        lista.Recorrer_Lista()
        print("al eliminar al final")
        lista.Eliminar_Al_Final()

        lista.Recorrer_Lista()