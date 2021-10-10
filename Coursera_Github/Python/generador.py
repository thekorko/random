
#Un generador es una función especial que va produciendo una secuencia de valores.
#En apariencia, es como una función normal, pero en lugar de devolver los valores con return, lo hace con la declaración yield

def first_1000():
    "Genera los primeros 1000 numeros"
    for x in range(1000)
        yield x
#el término generador define tanto a la propia función como al resultado que produce.
#La expresión yield regresa un objeto del scope o ámbito local de una función al scope superior de ésta.
#Pero, a diferencia de la declaración return,
#la función no es terminada sino que continúa su ejecución.
#Una característica importante de los generadores es que tanto las variables locales como el punto de inicio de la ejecución,
#se guardan automáticamente entre las llamadas sucesivas que se hagan al generador, es decir, a diferencia de una función normal, una nueva llamada a un generador reinicia la ejecución al principio de la función,
#sino que la continúa inmediatamente después del punto donde se encuentre la última declaración yield, que es donde terminó la función en la última llamada.
#En un generador, la declaración yield puede aparecer en varias líneas, e incluso dentro de un ciclo. El intérprete de Python producirá una excepción de tipo stop iteration, si encuentra el comando return durante la ejecución de un generador
gen_first_1000 = first_1000()

for x in gen_first_1000:
    print(x)

#Cuando ejecuta la primera vez la función, x comienza con, va primero el valor del range que es 0, y devuelve el 0, y entonces se imprime el 0.
#Luego, en la segunda llamada no vuelve a empezar, sino que ahora el range pasa a tener valor 1, y se devuelve el valor 1, que se termina imprimiendo en pantalla.
#Y así con el valor 2, y hasta el 999.



#Veamos otro ejemplo. Por ejemplo, un generador de números primos.

def gen_primos(cantidad=1):
    "Generador de numeros primos"
    contador = 1
    lista_primos[]

    #Comienza un ciclo infinito
    while cantidad > contador:
        es_primo = True
        contador += 1
        if len(lista_primos) > 0:
            for primo in lista_primos:
                if contador % primo == 0:
                    es_primo = false
                    break
        if es_primo:
            lista_primos.append(contador)
            yield contador

#Este generador genera la cantidad de números primos que le pidas.
#Entonces, si ejecutamos en la terminar la definición, y luego creamos un generador que te devuelve los primeros 100 números primos, cuando hacemos for del generador, e imprimimos cada elemento que será un número primo.
first_100_primos = gen_primos(100)

for x in first_100_primos:
    print(x)
