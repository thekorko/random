#JSON
#serializar y descerializar un objeto formato json
#javascript object notation

#es un formato popular en las apps modernas para intercambiar dato

#serializar un objeto significa transformar el mismo en una representación de
#una cadena de caracteres utilizando un formato determinado
#en este caso json

#descerializar es el proceso inverso
#pasa una cadena de caracteres representado en json a un objeto

import json #json estandar de python
import csv #csv estandar de python

#serializar un objeto
json.dumps([1,2,3])

#deserializamos un objeto
json.loads('[1, 2, 3]')

#existen dos funciones similares pero que guardan y leen desde
#un archivo

with open('E:\\json_example.txt', 'x') as a_file:
	json.dump([1, 2, 3, 4, 5], a_file)
#se guardo la lista serializada



with open('E:\\json_example.txt', 'r') as a_file:
	a_list = json.load(a_file)
	#ahora la tenemos en una variable deserializada como lista

#CSV
#csv es el formato mas simple de hojas de calculo
#una desventaja es que soporta multiformato
#pero a la vez es una ventaja
#x ejemplo se puede separar cada columna por comma, punto y comma, y tabulador
#y el entre comillado con comillas simples, dobles o sin
#a veces esto complica la interpretacion
#comma separated values
with open('E:\\datos.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	#nuevo objeto reader = libreria csv->reader(archivo)
	#objeto lector
	for row in reader: #con un for imprimimos las filas
		print(', '.join(row)) #separando las columnas por coma y espacio
		#notar que la fila es una lista

#abrimos el archivo existente con el modo a para poder "editarlo"
with open('E:\\datos.csv', 'a') as csvfile:
	writer = csv.writer(csvfile)
	#nuevo objeto writer = libreria csv->writer(archivo)
	#objeto esscritor
	writer.writerow(['laura', 'grunt', '12132312', 'qweeqww@gmail.com'])
	#escribimos una columna
#recordar que el contexto cierra solo el archivo
