


#formas de definir un diccionario
#Los diccionarios son una estructura de datos y un tipo de dato que asocian valores a claves. A diferencia de las listas que indexan sus elementos mediante un rango numérico, los diccionarios indexan sus elementos por claves
#definimos con llaves, de a pares 'clave': valor, osea clave dos puntos y el valor, y cada par con comas.
precios = {'manzana': 3.5, 'banana': 4.5, 'kiwi': 6.0, 'pera': 3.75}
#otra forma es usando la funcion dict() pasando el argumento de tipo keyword donde cada keyword es una clave
#y el valor del argumento es el valor para esa clave
precios = dict(manzana=3.5 ,banana=4.5, kiwi=6.0, pera=3.75)
#tambien se le puede pasar a dict() un iterable con tuplas (clave-valor) dict([(),(),()])
precios = dict([(manzana=3.5), (banana=4.5), (kiwi=6.0), (pera=3.75)])

#acceso a los elementos por claves
precios['manzana'] #3.5
precios['banana'] #4.5
precios['kiwi'] #6.0
precios['pera'] #3.75
precios['melon'] #keyerror

#agregar un elemento (clave-valor)
#indexamos por su nueva clave y definimos un valor
precios['melon'] = 5.75

#actualizar un elemento (clave-valor)
#se indexa con un elemento q ya existe y se actualiza el valor
precios['manzana'] = 3.0

#borrar un elemento
del precios['kiwi']

#pertenencia al diccionario
'banana' in precios
'sandia' not in precios



#Metodos de los diccionarios
precios = {'manzana': 3.5, 'banana': 4.5, 'kiwi': 6.0, 'pera': 3.75}

len(precios)

#obtiene el valor para las claves indicada, se puede indicar un default si no existe
precios.get('manzana') #devuelve el elemento
precios.get('melon') #devuelve null porque no defini un default
precios.get('melon', 0.00) #devuelve 0.00

#El método setdefault, si existe la clave, devuelve el valor; y si no existe la clave, crea el valor con el valor default indicado, y sí nos indica un valor default, la crea con el valor none.
precios.setdefault('banana')
precios.setdefault('sandia', 6.7)

#actualizar diccionarios
#El método update actualiza un diccionario. Se le puede pasar como parámetro de un diccionario, o también un iterable con duplas clave valor.
#Reproduce el video desde :1:58 y sigue la transcripción1:58
#Lo que hará es, si existe la clave, actualiza
#el valor, y si no existe, la crea con el valor indicado.
precios.update({'banana': 4.0, 'durazno': 5.5})
precios.update([('durazno': 5.5),('banana': 4.0,)])

#El método keys me devuelve una vista con las claves del diccionario
precios.keys()

#El método values me devuelve una vista con los valores del diccionario
precios.values()

#Y el método ítems me devuelve una vista con los ítems del diccionario
precios.items()

#El método pop saca del diccionario y devuelve el elemento con la clave indicada. Se puede poner un default si no existe.
precios.pop('manzana')
#se borra manzana
precios.pop('melon', 0.00) #default
precios.pop('melon') #Y en caso de no definir un default, dará un KeyError cuando no exista.


#Después tenemos el método popitem, que saca un elemento pero siguiendo el orden LIFO, Last In First Out.
precios.popitem()

#copia superficial de los diccionarios
copia_precios = precios.copy()

#borra todos los elementos
precios.clear()


#iterar diccionarios
#Las vistas son objetos que proveen una vista dinámica de las entradas del diccionario. Esto quiere decir, que si cambio el diccionario, dicho cambio se ve reflejado en las vistas. Las vistas también son iterables y responden al mensaje "Len" que indican la longitud y el mensaje "In" que indica la pertenencia. Los diccionarios tienen tres vistas: la vista "Keys" o claves, la vista "Values" o valores y la vista "Items" que devuelve los items del diccionario.
precios = {'manzana': 3.5, 'banana': 4.5, 'kiwi': 6.0, 'pera': 3.75}
#vistas de diccionario
claves = precios.keys()

valores = precios.values()

items = precios.items()

precios['melon'] = 5.5
#agrego un item al diccionario
claves
valores
Items
#todas esas vistas se actualizan automaticamente

#iteración de diccionarios
#ntonces, para recorrer haremos un "for" por clave "valor".
for furta, precio in precios.items():
    print("precio de", fruta, ": $", precio)


#claves de diccionarios
#Los diccionarios en Python están implementados internamente como una "Tabla Hash", con lo cual las claves deben ser objetos "hasheables"
#Un objeto es "hasheable" si tiene un valor hash que nunca cambia durante el ciclo de vida del programa,
#necesita tener definido el método mágico __HASH__ y debe poder ser comparado con otros objetos. Esto quiere decir que necesita tener definido el método mágico __EQ__

#Los objetos "hasheables" deben ser iguales cuando su "hash" son iguales.
#Todos los objetos inmutables que provee el "dict in" de Phyton son "hasheables", por ejemplo: los strings, los números, las tuplas son "hasheables", también las fechas son "hasheables".
#Los contenedores mutables como las listas, los conjuntos, los diccionarios no son "hasheables".
#Por último, los objetos que son instancias de clases definidas por el usuario son "hasheables" por defecto. Estos, al compararse, siempre son #distintos a otros objetos salvo a sí mismo y su valor "hash" se deriva desde su ID que es único.
#por defecto. Estos, al compararse, siempre son distintos a otros objetos salvo a sí mismo y su valor "hash" se deriva desde su ID que es único. Hemos visto qué condiciones deben cumplir las claves de los diccionarios.

import datetime
a_dict = dict()

#claves
a_dict['clave'] = 1
a_dict[1] = 1
a_dict[1.5] = 1
a_dict[(1,2)] = 1

a_dict[datetime.date.today()] = 1

#Una lista es un contenedor no inmutable(mutable), no puede ser hasheables
a_dict[[1, 2]] = 1
#lo mismo con los conjuntos
a_dict[{'a'}] = 1
#lo mismo con los diccionarios
a_dict[{'a': 1}] = 1
