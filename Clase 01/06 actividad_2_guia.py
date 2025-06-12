cadena = input ("Ingrese la palabra: "); # Pedimos al Cliente que ingrese una palabra .

cadenaNvaPrimeros = cadena[0:3]; # Indicamos que la cadena me de los primeros 3 caracteres.
cadenaNvaUltimos = cadena[-3:];# Indicamos que la cadena nos de los ultimos 3 caracteres.


print(cadenaNvaPrimeros , cadenaNvaUltimos, cadenaNvaPrimeros + cadenaNvaUltimos); # Mostramos en pantalla los primeros y los ultimos 3 caracteres y despues los dos concatenados.