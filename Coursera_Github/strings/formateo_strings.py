# _*_ coding: utf-8 _*_
import string

#var name contenido mi nombre
name = 'Korko'
#heredar de la clase formatter
#redefinir el metodo format con el comportamiento
#que necesites

#creo una instancia de la clase Formatter
formatter = string.Formatter()

#llamo al metodo format de la clase Formatter
#con el string que quiero formatear
formatter.format('Hola {}', name)
#output Hola Guillermo

#es lo mismo que lo que hicimos antes
'Hola {}'.format(name)

#Ejemplos:
#cada llave representa uno de los caracteres
"{} + {} = {}".format(2, 5, 7)
#esto no es una operacion es un string

#otra posibilidad es especificar el index del elemento
"{1} + {2} ={0}".format(7, 5, 2)

#otra opcion es pasar argumentos con nombre
#en este caso la variable name se reemplazara por el argumento name
"Hola {name}".format(name=name)
      #var name      #arg name <- variable name

#se pueden mezclar args con nombre y sin nombre
#primero se pasa los que no tienen nomnbre
"{0} + {1} = {result}".format(2, 5, result=7)

"{1:f} + {1:f} = {result:f}".format(2, 5, result = 7)
