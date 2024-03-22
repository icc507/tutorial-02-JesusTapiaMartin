#Problema 2  / 7 ptos x4 pruebas / 28 puntos
#Ingreso de valores en árbol TRI-nario
#---------------------------------------------------------------------------------
# Confeccione un programa que lea varios números y cree un árbol trinario con listas
# esto es igual que el binario, pero los elementos que son iguales van en una lista
# centro, de la forma [numero, [subarbol IZQ], [mismo NUM], [subarbol DER] ]
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 30 90 90 8 5 90
#La salida debe ser
#         [20, [8, [5, [], [], []], [], []], [], [30, [], [], [90, [], [90, [], [90, [], [], []], []], []]]]
def arbolTrinario(numero):
    return [numero, [], [], []]

def insertaEnArbolTrinario(arbol, numero):
    if numero == arbol[0]:
        if not arbol[2]:  
            arbol[2] = [numero]  
        else:
            arbol[2].append(numero)
    elif numero < arbol[0]:
        if len(arbol[1]) == 0:  
            arbol[1] = arbolTrinario(numero)
        else:
            insertaEnArbolTrinario(arbol[1], numero) 
    else:
        if len(arbol[3]) == 0:  
            arbol[3] = arbolTrinario(numero)
        else:
            insertaEnArbolTrinario(arbol[3], numero)


def estaEnArbolTrinario(arbol, numero):
    if arbol == []:
        return False
    elif numero in arbol[2]:  
        return True
    elif numero == arbol[0]:  
        return True
    elif numero < arbol[0]:
        return estaEnArbolTrinario(arbol[1], numero)  
    else:
        return estaEnArbolTrinario(arbol[3], numero)


datos = input().split()


for i in range(len(datos)):
    if datos[i].isdigit():
        datos[i] = int(datos[i])


arbol = arbolTrinario(datos[0])
for numero in datos[1:]:
    insertaEnArbolTrinario(arbol, numero)


print(arbol)
