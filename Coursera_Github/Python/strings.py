# -*- coding: utf-8 -*-

#Ser consistente con el codigo
#Mantener una convencion o estilo de codigo
#
# /n es el caracter que representa salto de linea


s1 = "String comilla doble" #el uso dependera de la convencion adoptada en el codigo para que quede mas prolijo

s2 = 'String comilla simple' #imprime una linea

s3 = """String 3 comillas
dobles""" #imprime /n para el salto de linea

#python 3 utiliza unicode para los strings
#python 2 usaba ascii que puede representar 256 caracteres


s4 = '''string saltos de linea
String
string'''
#las cadenas necesitan ser codificadas por que en codigo maquina son 0 y 1
#utf 88 puede representar mas de 100000 caracter
#si se quiere cambiar la codificacion usamos la funcion encode

s5 = "áéíóú"

type(s5) #type de s5 es string (unicode)

s6 = s5.encode('utf-8')

s6

type(s6) #su type ahora es bytes

s7 = s5.encode('ascii') #error porque ascii no soporta acentos
