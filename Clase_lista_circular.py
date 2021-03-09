from nodo import Nodo

class Lista_Circular():                              #Se crea una lista a la cual se irá agregando los nodos
    def __init__(self):
        self.primero=None                           #Se crea un head
        self.ultimo=None                            #Se crea un end

    def Lista_Vacia(self):
        return self.primero==None                   #Informa cuando la lista está vacía(devuelve true si esta vacía)

    def Agregar_Al_Inicio(self,dato):                   #Se agrega un dato al inicio de la lista
        if self.Lista_Vacia():
            self.primero=self.ultimo=Nodo(dato)
            self.ultimo.siguiente=self.primero
        else:
            aux=Nodo(dato)
            aux.siguiente=self.primero
            self.primero=aux
            self.ultimo.siguiente=self.primero

    def Agregar_Al_Final(self,dato):
        if self.Lista_Vacia():
            self.primero=self.ultimo=Nodo(dato)
            self.ultimo.siguiente=self.primero
        else:
            aux=self.ultimo
            self.ultimo=aux.siguiente=Nodo(dato)
            self.ultimo.siguiente=self.primero

    def Eliminar_Al_Final(self):
        if self.Lista_Vacia():
            print("lista vacía")
        elif self.primero==self.ultimo:
            self.primero=self.ultimo=None
        else:
            aux=self.primero
            while aux.siguiente != self.ultimo:
                aux=aux.siguiente
            aux.siguiente=self.primero
            self.ultimo=aux

    def Recorrer_Lista(self):
        aux=self.primero
        while aux:
            print(aux.dato)
            aux=aux.siguiente
            if aux==self.primero:
                break