#Problema 2  / 9 ptos x4 pruebas / 36 puntos
#Concatenación de listas o tuplas
#---------------------------------------------------------------------------------
#Confeccione un programa que lea varios elementos y los entregue de manera inversa
#---------------------------------------------------------------------------------
#Ejemplo de entrada:
#         20 90 hola jiji 77
#La salida debe ser
#         (77, 'jiji', 'hola', 90, 20)
t           = input().split()
tInvertido  = reversed(t)
largoT      = len(t)


for i in range(largoT):
    if (t[i].isdigit()):
        t[i] = int(t[i])

tInvertido = tuple(tInvertido)
print(tInvertido)
