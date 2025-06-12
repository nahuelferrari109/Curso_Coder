# OPERADORES ARITMETICOS.
###########################################################################

# Suma (+): Adición de dos números.

# Resta (-): Sustracción de un número de otro.

# Multiplicación (*): Producto de dos números.

# División (/): Cociente de dos números.

# División entera (//): Cociente entero de la división de dos números.

# Módulo (%): Resto de la división de dos números.

# Potenciación (): Un número elevado a la potencia de otro.

#//////////////////////////////////////////////////////////////////////////

# METODOS DE CADENA
###########################################################################

#len(): te da el numero de cuantos caracteres tiene el string

# texto ="Hola mundo"; #cadena
# cantidadDeCaracteres= len(texto); #cuenta la cantdad de caracteres de la cadena con el nombre texto.
# print(cantidadDeCaracteres); # resultado devuelve la cantidad de caracteres y muestra pantalla devuelve 10.

###########################################################################

#lower():Convierte todos los caracteres de la cadena en minusculas.
#upper(): Conviente todos los caracteres de la cadena a mayusculas.
#replace(old, new): remplaza todas las apariciones de old con new.
#split(delimitar): Divide la cadena en una lista de subCadenas, utilizando el delimitador especificado.
#strip(): Elimina los espacion en blanco al principioy al final de la cadena.
#Ejemplo.

# cadena = "Python es Increible";
# print(cadena.lower()); # Resultado: "python es increible" osea todo en minusculas.
# print(cadena.upper()); # Resultado: "PYTHON ES INCREIBLE" osea todo en mayusculas.
# print(cadena.replace("Increible","genial")) # Resultado : "Python es genial" osea cambio incrible por genial.
# print(cadena.split()) #Resultado: ["Python", "es", "Increible"]. osea delimito con comas.
# print (cadena.strip()) # resultado: Python es Increible. osea elimino lo que se le habia colocado arrible de las comas.

###########################################################################

# Indexacion = podes indicar el caracter por medio del indice. por ejemplo

# cadena = "python"; # cadena
# print (cadena[0]) # Indica que de la cadena "python" scamos la letra "p"

###########################################################################

# Slincing : permite extraer una parte especifica utilizando [Inicio:Fin:Paso] por ejemplo.
# cadena =  "Python";
# print (cadena[0:2])# Indica que el Inicio en el primer caracter, termina en el segundo caracter y el paso en 1 en 1. Devuelve PY.
# print(cadena[2:5])# Indica que el Inicio en el segundo caracter, termina en el quinto caracter y el paso en 1 en 1. Devuelve tho.
# print(cadena[-3:])#Indica que el inicio es 3 pero desde el ultimo caracter hasta el primero y termina el el ultimo caracter y el paso es 1 en 1. devuelve hon.
# print (cadena[::2])# Indica que el incio es el la primera letra , hasta el ultimo caracter, pero con el pase de 2 en 2. deuelve pto.

###########################################################################

# CONCATENACION DE CADENAS Se puede hacer tanto con + o como con el metodo join();

#Ejemplo con el +
# cadena1= "Python" #cadena 1
# cadena2="es genial" # cadena 2
# resultado = cadena1 + " " + cadena2; #concatenamos la primer cadena con el espacio y eso con la cadena2.
# print(resultado); #Resultado: "Python es genial"

#Ejemplo con el join()
# partes = ["Python", "es", "genial"]
# resultado = " ".join(partes);
# print(resultado);

###########################################################################
# Repeticion de cadena se hace con el *

# cadena = "hola, " #cadena 
# multiplicarCadena = cadena * 5; #Multiplica 5 veces la cadena.
# print(multiplicarCadena); # Imprime las 5 cadenas multiplicadas.

###########################################################################