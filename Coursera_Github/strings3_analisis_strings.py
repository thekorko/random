s1 = "Prueba"


#devuelve el numero de ocurrencias de la cadena que le pasamos en toda s1
s1.count("a")

#indica en boolean si la cadena empieza con el caracter
s1.startswith("a")

#indica en boolean si termina con el caracter
#s1.endswith("a")


#busca la subcadena que le pasamos y nos tira el index donde empieza esa cadena en la palabra (la primera) si no lo encuentra devuelve -1
s1.find("ue")

#busca pero si no la encuentra tira una exception valueerror
#s1.index("a")

#igual que find solo que en vez pasar la primera coincidencia devuelve la ultima
s1.rfind("ue")

#son carac decimales
s1.isdecimal()

#son digitos?
s1.isdigit()

#son todos lowercase
s1.islower()

#son todos mayus?
s1.isupper()

#es un titulo?
s1.istitle()

#son todos caracteres " " espacio?
s1.isspace()

#son alfabeticos?
s1.isalpha()

#indica si esta compuesta por caracteres alfanum
s1.issalnum()