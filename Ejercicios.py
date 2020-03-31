#Ejercicio
# Pasar a escala de grises el color codificado en los elementos de la lista `pixel`
print("Ejercicio #1")
pixel= [0.6,0.3,0.4] # intensidades de cada canal. 
#El elemento 0 es el R, el 1 el G y el 2 el B

# la intensidad en escala de grises es el promedio de la intensidad de cada canal R, G y B
intensidad=(pixel[0]+pixel[1]+pixel[2])/3

print("La intensidad es:")
print(intensidad)

#Ejercicio 2
# Pasar a blanco y negro el valor de intensidad codificado en la variable intensidad

print("Ejercicio #2")
# podemos considerar que un pixel se convierte en blanco si su intensidad en escala de grises es mayor a 0.5
# y negro de lo contrario
if intensidad > 0.5:
    bw = "blanco"
else:
    bw = "negro"
print("En blanco y negro el pixel sería: (0 -> negro, 1 -> blanco)")
print(bw)
print("Ejercicio #3")
#Ejercicio 3: Escribir un for para buscar el máximo de la lista e imprimirlo
lista=[44,11,15,29,53,12,30]
for i in lista:
    for num in lista:
        if num > i:
            maximo = num


# debe imprimir 53
print("- El maximo es:")
print(maximo)

print("Ejercicio #4")
#Ejercicio 4: Escribir un for para buscar el máximo de la lista e imprimir su _posición_
lista=[44,11,15,29,53,12,30]
for i in range(len(lista)):
    for num in lista:
        if num > lista[i]:
            posicion= lista.index(num)

#debe imprimir 4
print("- La posición del máximo es:")
print(posicion)

#Ejercicio 5
print("Ejercicio #5")
# Escribir una función que reciba una lista y un valor, 
#y devuelva la cantidad de veces que aparece ese valor en la lista

def ocurrencias(lista,valor):
    contador =0
    for num in lista:
        if valor == num:
            contador = contador + 1
    return contador


l=[1,4,2,3,5,1,4,2,3,6,1,7,1,3,5,1,1,5,3,2]
v=2

print("La cantidad de ocurrencias es:")
print(ocurrencias(l,v))
#debe imprimir 3, la cantidad de veces que aparece el 2 en la lista