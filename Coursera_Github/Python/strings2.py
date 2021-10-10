#strings dinamicas
#le paso un valor a un string para formar una string compuesta por diferentes tipos de variables
#se componen de cadenas de caracteres fijas y variables
#el operador es el % y nos permite pasarle uno o mas datos a mi strings
name = "Guillermo" #defino la varable name
"Hola %s" %name #le paso la variable previa a esta string
#Estro muestra en consola la string y mi nombre
"el numero es %d" % 6 #le paso un entero
"el numero es %02d" %7 #quiero pasarle un entero minimamente de dos digitos y si no los tiene completar con 0
"el decimal es %f" %8.2 #le paso un decimal
"el decimal es %.2f" %8.2 #le paso un decimal y limito a dos digitos
"hola %(name)s" % {'name': name} #le paso un diccionario donde la clave tiene que coincidir con el nombre que le pongo en el operador
#le pasamos un parametro con nombre
"hola %(name)s" % {'name': "test2"}
#el diccionario lo podemos llenar ahi mismo o llenarlo con una varable
"hola %(clave)s" % {'clave': name}
#la "clave" es el identificador


"hola {}".format(name) #llamo al metodo format() y le paso la variable name
"hola {}".format("dsadsaads") #No esta tan mal es divertido esto

"la suma de 1 + 2 es {0}".format(1+2) #remplazamos la posicion 0 por el output del metodo format
#mas adelante veremos con mas detalle

#concatenacion con el metodo join() usando una lista de valores
' '.join(["Hola", name]) #concatenamos usando un espacio vacio

', '.join(["1", "2", "3", "4"]) #los elementos de esta lista tienen que ser strings no puedo usar numeros porque estamos hablando de concatenacion

test = ', '.join(["1", "2", "3", "4"]) # es valido
