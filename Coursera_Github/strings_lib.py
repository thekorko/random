


"{0:f} + {1:f} = {result:f}".format(2, 5, result=7)
#represebtamnos los valors de la streing como float point
#

"{0:.3f} + {1:.3f} = {result:.3f}".format(2, 5, result=7)
#lo mismo perto con un numero lo limitamos a lo que viene despues de la coma, .2, .3, .4 etc

name = Guillermo
"Hola {name:16}".format(name=name)
#como minimo con cierta cantidad de caracteres
#se autocompleta con espacios " "


#alineacion a la izquierda
"Hola {name:<16}".format(name=name)

#alineacion a la derecha
"Hola {name:>16}".format(name=name)

#centrado
"Hola {name:^16}".format(name=name)

#centrado y rellenar con asteriscos en vez de 0
"Hola {name:*^16}".format(name=name)
