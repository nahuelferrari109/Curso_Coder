#CONJUNTOS Y DICCIONARIOS.
#que son?
#los conjuntos y diccionarios son otro tipo de colecciones que, al igual que las tuplas y listas, permiten almacenar multiples elementos en una sola variable.
# Aunque ambos se utilizan para agrupar datos, tienen caracteristicas y usos distintos que los diferencian de otro tipos de colecciones como las listas y las tuplas.

#diferencias y similuted
# estructura
#conjuntos: son colecciones no ordenadas de elemetnos unicos. No permiten duplicados y no mantienen el orden de los elemetnos.
#Diccionarios: son colecciones de pares clave-valor. cada vlase es unica y se utiliza para almacenar y acceder a los valores correspondientes.

#mutabilidad
#Conjuntos: Son mutables, es decir, se pueden agregar o eliminar elemetnos despues de su creacio.
#Diccionarios: Tambien son mutables, permitiendo la modificacion de par clave-valor existentes, asi como la adicion y eliminacion de nuevos pares.

#acceso a elemetnos
#conjuntos:No permiten el acceso a elementos mediante indice ya que no mantiene un orden.
#Diccionario: Permiten el acceso rapido a los valores mediante sus claves unicas.

#usos comunes.
#conjuntos: se utilizan para alamacenar elementos unicos y realizar operaciones matematicas como uncion, interseccion y diferencia.
#Diccionarios: Se utiliza para almacenar datos en pares clave-valor, permitendo busqueda rapidas y efecientes.

#que son los conjuntos ?
#Los conjuntos son colleciones no ordenadas de elementos unicos.
# Esto segnifica que no pueden contener elementos duplicados y que el orden de los elemetnos no esta garantizados.

#Sixtansis Basica 
#para definir un conjuntos, se utilizan llaves {} o la funcion set(). Ejemplo.

# numeros = {1, 2, 3, 4, 5} #Definiendo un conjuntos de numeros.

# letras = set(["a", "b", "c", "d"]) #Usando la funcion set().

# conjuntos_vacio = set(); #Definimos un conjunto vacio.

#Caracteristicas de los conjuntos

#elementos unicos: Los conjuntos no permiten elementos dulicados. si se intenta agregar un duplicado sera ignorado. 
#numeros = {1,2,2,3} print(numeros)// resultado = {1,2,3}. osea se ignora el dos porque esta duplicado.

#No ordenado: Los elementos en un conjuntos no tienen un orden especificos. No se puede acceder por Indice.

#Operaciones de conjuntos: Python proporciona varias operaciones para trabajar con conjuntos, como la union, inteseccion y diferencia.

# Ejemplo de operaciones con conjuntos.

#Union combina todos los elemetnos de dos conjuntos, eliminando duplicados.
# conjunto1 = {1,2,3} #definimos conjunto 1 
# conjunto2 = {3,4,5} #definimos conjunto 2
# union = conjunto1 | conjunto2 # hace la operacion union y elimina los duplcados 
# print(union); #Resultado {1 , 2, 3, 4, 5}

#Interseccion: Devuleve los elemntos que estan persentes en ambos conjuntos.
# conjunto1 = {1,2,3} #definimos conjunto 1 
# conjunto2 = {3,4,5} #definimos conjunto 2
# interseccion = conjunto1 & conjunto2 #Hace la operacion Interccesion.
# print(interseccion); #Devuelve la interccesion de los dos conjuntos (osea los que estan dentro de los dos conjuntos.) resultado:{3}.

#Diferencfia: Devuelve los elemetnos que estan presentes en ambos conjuntos.
# conjunto1 = {1,2,3} #definimos conjunto 1 
# conjunto2 = {3,4,5} #definimos conjunto 2
# diferencia = conjunto1 - conjunto2; #Hace la diferencia entre los dos conjuntoos osea devuelve elos elemetos del primero que no estan en el segundo.
# print(diferencia)#resultado{1, 2}.

#uso de metodos en conjunrtos.

#add(): agrega un elementos 
# numeros = {1,2,3,4,5} #Definimos el conjunto numeros
# numeros.add(6) #Aplicamos el metodo add(elemento que queres agregar) que es para agregar un elemeto
# print(numeros) #resultado {1,2,3,4,5,6}

#remove(): Elimina un elemento al conjunto.
# numeros = {1,2,3,4,5,6} #Definimos el conjunto numeros
# numeros.remove(6)#Aplicamos el metodo remove(elemento que queres eliminar) que es para eliminar un elemento.
# print(numeros) #resultado {1,2,3,4,5,6}

#discard(): Elimina un elemento del conjunto si esta presente. No genera error si el elemento no existe.
# numeros = {1,2,3,4,5} #Definimos el conjunto numeros
# numeros.discard(6) #Aplicamos el metodo discard(elemento que queres eliminar si esta presente) sirve para eliminar un elemetno si esta presente y si no esta no da error.
# print(numeros) #el elemeto no estaba entonces el resultado es el mismo. {1,2,3,4,5} tampoco dio error.

#clearr() elimina todos los elementos del conjunto.
# numeros = {1,2,3,4,5} #Definimos el conjunto numeros
# numeros.clear() #elimina todo el conjunto numeros ahora el mismo esta vacio 
# print(numeros) #resultado {}

#list() es par trasforma el conjunto en una lista. y ahi si poder ver el elemeto por indice.


#Que son los Diccionarios?
#los diccionarios son estructura de datos que permiten almacenar colecciones de pares clave-valor. A diferencia de las listas y tuplas, que son secuencias de elemetnos.
#Los diccionarios son colecciones no odenadas, lo que significa que no mantiene el orden de insercion de los elementos.
#cada clave en un diccionario es unica y se utiliza para acceder a su valor correspondiente de manera rapida y eficiente.

#Sintaxis basica..
#Para definir un diccionario, se utiliza llavaes{} y los pares clave-valor se separan por comas, con la clave y el valor separador por dos puntos :.
#por ejemplo.

# persona = {#creamos un diccionario llamado persona.
#     "nombre":"juan",# creamos una clave con el nombre "nombre" y su valor "Juan"
#     "edad" : 30, # creamos una clave con el nombre "edad" y su valor 30
#     "ciudad" : "madrid"# creamos una clave con el nombre "ciudad" y su valor "Madrid"
# }

#Caracteristicas de los Diccionarios 
#Colecciones No Ordenadas: Los diccionarios no mantienen el orden de los elementos.
#pares Clave-valor: Cada elemetno en un diccionario esta formado por partes: una clave y uin valor. las calves deben ser unicas e inmutables
#(pueden ser cadenas, numeros o tuplas), mientras que los valores pueden ser de cualquier tipo.

#Acceso rapido a Valores: se puede acceder a los valores en un diccionario de manera eficiente utilizando sus claves.

#Ejemplo practicos.

#Definicion y Acceso:

# alumno = { #creamos un diccionario llamado alumno.
#     "nombre" : "Ana",# creamos una clave con el nombre "nombre" y su valor "Ana"
#     "edad" : 22# creamos una clave con el nombre "curso" y su valor "Matematicas"
# }
# nombreAlumno = alumno ["nombre"] #Buscamos en el diccionario alumno su nombre 
# print (nombreAlumno)# Resultado : Ana
# edadAlumno = alumno["edad"]#Buscamos en el diccionario alumno su edad.
# print(edadAlumno)# Resultado : 22

#Modificacion de valores : Los diccionarios son mutables, por lo que se pueden modificar los valores existentes,
#Agregar nuevos pares clave-valor y eliminar elementos.

# alumno = { #creamos un diccionario llamado alumno.
#     "nombre" : "Ana", # creamos una clave con el nombre "nombre" y su valor "Ana"
#     "edad" : 22,# creamos una clave con el nombre "edad" y su valor 22
#     "curso" : "Matematicas"# creamos una clave con el nombre "curso" y su valor "Matematicas"
# }

# alumno["ciudad"] = "Barcelona" # se le agrega la clave ciudad con el valor Barcelona
# del alumno["curso"] # se elimina la clave curso con su valor

# print(alumno) # Resultado : 'nombre': 'Ana', 'edad': 22, 'ciudad': 'Barcelona'.

#Metodos utiles para Diccionarios 

#Key() Devuelve una vista de las claves del diccionario.

# alumno = { #creamos un diccionario llamado alumno.
#    "nombre" : "Ana", # creamos una clave con el nombre "nombre" y su valor "Ana"
#    "edad" : 22,# creamos una clave con el nombre "edad" y su valor 22
#    "curso" : "Matematicas"# creamos una clave con el nombre "curso" y su valor "Matematicas"
# }
# claves = alumno.keys() #Aplicamos el metodo key para que nos muestre las claves del diccionario.
# print(claves) #Respuesta: dict_keys(['nombre', 'edad', 'curso'])

#values() Devuelve una vista de los valores del diccionario.

# alumno = { #creamos un diccionario llamado alumno.
#    "nombre" : "Ana", # creamos una clave con el nombre "nombre" y su valor "Ana"
#    "edad" : 22,# creamos una clave con el nombre "edad" y su valor 22
#    "curso" : "Matematicas"# creamos una clave con el nombre "curso" y su valor "Matematicas"
# }
# valores = alumno.values()#Aplicamos el metodo values() para que nos muestre los valores de cada clve del diccionario.
# print(valores)# Resultado: dict_values(['Ana', 22, 'Matematicas'])

#Items() Devuelve una vista de los pares clave-valor del diccionario.

# alumno = { #creamos un diccionario llamado alumno.
#    "nombre" : "Ana", # creamos una clave con el nombre "nombre" y su valor "Ana"
#    "edad" : 22,# creamos una clave con el nombre "edad" y su valor 22
#    "curso" : "Matematicas"# creamos una clave con el nombre "curso" y su valor "Matematicas"
# }
# items = alumno.items() #Aplicamos el metodo items que nos da la calve-valor del diccionario alumno.
# print(items)#resultado: dict_items([('nombre', 'Ana'), ('edad', 22), ('curso', 'Matematicas')])

#get(): devuelve el valro para una calve dada, o "none" si la clave no existe.

# alumno = { #creamos un diccionario llamado alumno.
#    "nombre" : "Ana", # creamos una clave con el nombre "nombre" y su valor "Ana"
#    "edad" : 22,# creamos una clave con el nombre "edad" y su valor 22
#    "curso" : "Matematicas"# creamos una clave con el nombre "curso" y su valor "Matematicas"
# }
# curso = alumno.get("curso") # Aplicamos el metodo get() que nos da el valor de la clave dada o None en el caso que no exista la clave.
# ciudad = alumno.get("ciudad")# Aplicamos el metodo get() que nos da el valor de la clave dada o None en el caso que no exista la clave.
# print(curso) #resultado :  "Matematicas"
# print(ciudad) #resultado : None

#update() Actualiza el diccionario con los pares clave-valor de otro diccionario o con pares calve-valor proporcionados como argumentos.

# alumno = { #creamos un diccionario llamado alumno.
#    "nombre" : "Ana", # creamos una clave con el nombre "nombre" y su valor "Ana"
#    "edad" : 22,# creamos una clave con el nombre "edad" y su valor 22
#    "curso" : "Matematicas"# creamos una clave con el nombre "curso" y su valor "Matematicas"
# }
# print(alumno) #resultado: {'nombre': 'Ana', 'edad': 22, 'curso': 'Matematicas'}
# alumno.update({"edad" : 24, "curso" : "fisica", "ciudad": "Buenos Aires"})# Aplicamos el metodo update() y actualiza el diccionario alumno con los clave-valor que nosotros lo dimos o otro diccionario.
# print (alumno) #resultado: {'nombre': 'Ana', 'edad': 24, 'curso': 'fisica', 'ciudad': 'Buenos Aires'}

#len() #tambien sirve con diccionarios y te da cada par de clave-valor que hay en el dccionario en el calo de alumnos hay 3

#pop() sirve tambien para borrar una clave seleccionada.

# clear() sirve para eliminar todo el contenido de un diccionario.

