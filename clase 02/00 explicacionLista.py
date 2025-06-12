#LISTAS
###########################################################################
#Que es una lista?
#En Python, las listas son estructuras de datos muy versatiles que permiten almacenar una coleccion ordenada de elementos.
#A diferencia de otros leguajes de progrmacion, las listas en Python pueden contener elementos de diferentes tipos, incluyendo numeros, cadenas de tecto e incluso otras listas.
#Las listas son mutables eso significa que podes modificar su interior osea eliminar agregar borrar datos que contiene esa lista.

#Sintaxis basica para definier una lista en Python se utilizan [] y los elementos se separan por comas. Ejemplos.

# #Lista de numeros enteros 
# numeros = [1, 2, 3, 4, 5];

# #Lista de cadenas de texto.
# frutas = ["manzana", "Banana", "cereza"];

# #Lista heterogenea (contiene diferentes tipos de datos).
# mi_lista = [1, "hola", 3.14, True];

# #Lista vacia
# listaVacia = [];

###########################################################################

# #ACCESO POR INDICE: los elementos de una lista se pueden acceder utilizndo su indice. Comienza desde 0 para el primer elemetno. Ejemplo.

# primer_numero = numeros[0] #Accedimos al primer elemeto de la lista que hicimos arriba llamada numeros. devuelve el 1.
# segunda_fruta = frutas[1] #Accedunis al segundo elemetno de la lista frutas que hicimos arriba. devuelve banana.

# primer_elemento = mi_lista[0]; #Accedimos al primer elemento de la lista heterogenea que hicimos arriba. devuelve 1.
# segundo_elemetno = mi_lista[1]; #Accedimos al segudo elemento de la lista heterogenea que hicimos arriba. devuelve "hola". 

###########################################################################

# SLICING (Subconjunto de listas).

# Python permite extraer subconjuntos de una lista utilziando la tecnica de slicing. esto se hace utilizando el operaor: dentro de los corchetes

# numeros = [0,1,2,3,4,5,6,7,8,9]; #Definimos una lsita de numeros.

# primeros_cinco = numeros[0:5]; #Nos devuelve los primeros 5 elementos de la lista. [0,1,2,3,4].

# desde_cinco = numeros [5:]; #Nos devuelve desde la pocicion 5 hasta la ultima posicion.[5,6,7,8,9]

# sub_lista = numeros [2:7]; # Nos devuelve desde la posicion 2 hasta la posicion 7. [2,3,4,5,6]

# pares = numeros [0:10:2] #Nos devuelve desde la posicion 0 hasta la 10 pero con el paso de 2 en 2. [0,2,4,6,8]

###########################################################################

#OPERACIONES BASICAS.

# mi_lista = [1,2,3];

# mi_lista.append(4) #con .append() agregamos el elementos al final de la lista. [1,2,3,4] 

# mi_lista += [5,6] # con el += se puede agregar como el append pero mas canttidad de elementos.

# mi_lista.insert(1,1.5) # Con .insert(posicion , elemetno a agregar) Nos agrega el elemento donde nostros queramos agregarlo. [1,1.5,2,3,4]

# mi_lista.remove(1.5)# Con .remove(elemento) Nos elimina el elemento que nostros le pasemos como parametro. [1,2,3,4] en este caso se elimino el 1.5

# del mi_lista[3] # con del eliminamos por el indice.

# mi_lista.pop() #elimina el ultimo elemento de la lista y tambien por indice.

# mi_lista[0] = 5 #modificamos un elemento existente [5,2,3,4] cambiamos el elemento de la posicion 0 (osea el 1 ) por el elemento 5.

# cuenta = mi_lista.count(2) #Nos muestra la cantidad de elementos que aparece ese elemento en la lista en este caso seria 1 sola vez.

# longitud = len(mi_lista) #Me devuelve la longitud de la lista. Osea cuantos elementos tiene la lista.

# elemento = mi_lista.index(4); # Con .index(elemetno que queremos buscar) busca la posiscion del ese elemento osae el indice.

# masNumeros = [7, 8 , 9];
# mi_lista.extend(masNumeros);# se agrega al final la nueva lista que nosotros le dimos.

# mi_lista.clear()# Elimina todos los elemetnos de una lista. 
