#Tuplas
#Que es ?
#las tuplas son estructuras de datos que, al igual que las listas, perimiten almacenar una coleccion ordenada de elementos.
#sin embargo, a diferencia de las listas, las tuplas son inmutables, lo que significa que una vez creadas, sus elementos no pueden ser modificados.
#esta caracteristica hace que las tuplas sean utiles para datos que no debes cambiar a lo largo del programa.

###########################################################################

#Caracteristicas:
#inmutabilidad: una vez definida, no se pueden cambiar los elementos de una tupla.
#definicion:se define utilizando parentesis() en lugar de corchetes [].
#Acceso rapido: Al ser inmutables, python puede optimizar el acceso a sus elemento, loque las hace ligerametne mas rapidas que las listas ara algunas operaciones.
#Heterogeneidad: Al igual que las listas, las tuplas pueden contener elementos de diferentes tipos.

###########################################################################

#Sintaxis de las tuplas:

numeros = (10, 20, 30, 40, 50); #craeamos una tupla de numeros.

nombres = ("Alice", "Bob", "Charlie"); #creamos una tupla de cadenas (osea texto).

datos = (25, "Python", 3.14, "charlie") #creamos una tupla heterogenea (osea de diferentes tipo de dato).

###########################################################################

# Acceso por indice: 

#Accediendo al elemento de la tupla
# primer_numero = numeros [0]; # De la tupla numeros buscamos el indice 0 (osea el primer elemento) y nos devuelve 10.
# segundo_nombre = nombres [1]; # De la tupla numeros buscamos el indice 1 (osea el segundo elemento) y nos devuelve "Bob".

# #Accediendo a eleementos de una tupla heterogenea.
# primer_dato = datos[0] # De la tupla datos buscamos el indice 0 (osea el primer elemetno)y nos devuelve 25.
# tercer_dato = datos [3]# De la tupla datos buscamos el indice 3 (osea el cuarto elemento) y nos devuelve "Charlie".

#Slicing (subconjuntos de tuplas)

# numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9); #Definiendo una tupla de numeros 

#Slicing: obteniendo los primeros cinco elementos.

# primeros_cinco = numeros[0:5] # nos crea una nueva tupla con los primeros 5 elementos (0, 1, 2, 3, 4, 5);

#Slicing: obteniendo elemtnos desde el indice 5 hasta el final.
# desde_cinco = numeros[5:] # Nos crea una nueva tupla desde el indice 5 hasta el final de la tupla (5, 6, 7, 8, 9).

#Slicing: Obteniendo un subconjunto de elementos.
# sub_tupla = numeros[2:7] # Nos cre una nueva tupla desde el inice 2 hasta el indice 7 (2, 3, 4, 5, 6)
