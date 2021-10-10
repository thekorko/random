file = open("E:\\archivo456","r")
print(file.readlines())
#la funcion se llama con dos parametros
#la ruta del archivo
#y el modo de apertura
#visual studio te permite ver la documentacion de python y ejecutar
#la consola
#los modos son
#r en lectura que es el (default)
#w en escritura truncando el archivo primero
#x para abrir un nuevo archivo en modo escritura
#a para agregar contenido al final o mantener lo que tenia previamente
#b para modo binario
#t para texto (default)
#+ para actualizaciones
#u ya no se usa

file.read()
file.close()
#si no cerramos el archivo estamos posiblemente bloqueando a otros programas
#y quedara un file descriptor en el sistema operativo
#cerrar siempre los archivos


#devuelve un objeto de tipo archivo
#si ocurre algun problema como que el user no tenga permiso para abrir el archivo
#o que el archivo no exista
#se levanta una excepcion de ioerror

#vamos a guardar un string en el archivo
with open("E:\\archivo456","w") as a_file:
	a_file.write('hola mundo')
	a_file.writelines(['linea 1:\n', 'linea 2:\n', 'linea 2:\n'])


with open("E:\\archivo456","a") as a_file:
	a_file.write('hola mundo')


#tambien podemos usar un context manager
#que nos permite definir acciones al entrar en contexto
#o al salir del contexto
#por ejemplo con los archivos al abrirlos
#despues se cierran automaticamente
with open("E:\\archivo456","r") as file:
	file.read()
	print(file.read()) #leemos e imprimomos todo el archivo
	#la funcion read lee todo el contenido del archivo
	print(file.readline())
	print(file.readlines())

with open("E:\\archivo4356","r") as a_file:
	print(a_file.readline()) 
	file = ['saddasasd\n', 'ewqewqeqweqw\n', 'ewewqeqweqw\n']
	#la funcion readline, lee la linea actual del archivo
	print(a_file.readlines())
	#la funcion readlines las lineas del archivo y las guarda en una lista
	print(list(a_file))
	#genera una lista  con las lineas del archivo
	#es lo mismo que readlines
	for line in a_file:
		print(line)


