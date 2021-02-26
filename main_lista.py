from lista_circular import Lista_Circular
from os import system       #se realiza esta importacion para que cada vez que se ejecute el programa,
system("cls")               #la consola se encuentre limpia.

lista=Lista_Circular()
lista.Agregar_Al_Final(1)
lista.Agregar_Al_Inicio(20)
lista.Agregar_Al_Final(2)
lista.Agregar_Al_Inicio(11)

lista.Recorrer_Lista()
print("al eliminar al final")
lista.Eliminar_Al_Final()

lista.Recorrer_Lista()

