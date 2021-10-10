Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(‘\’Hola \n Mundo!\’’)
SyntaxError: invalid character in identifier
>>> print(’\’Hola \n Mundo!\’’)
SyntaxError: invalid character in identifier
>>> print("\"Hola \n Mundo!\"")
"Hola 
 Mundo!"
>>> string = "PYTHON"
>>> string.startswith("py")
False
>>> 
>>> 
>>> 
>>> string.startswith("Py")
False
>>> string.startswith("PY")
True
>>> string = "destin ON"
>>> string.endswith(‘on’.swapcase())
SyntaxError: invalid character in identifier
>>> string.endswith("on".swapcase())
True
>>> string = "pyTHON"
>>> string.endswith("on".swapcase())
True
>>> string = "python"
>>> string.endswith("on".swapcase())
False
>>> string.find("y")
1
>>> string.find("z")
-1
>>> 
KeyboardInterrupt
>>> string.find("p")
0
>>> string = "\\n"
>>> string.isspace()
False
>>> string = " "
>>> string.isspace()
True
>>> string = "
SyntaxError: EOL while scanning string literal
>>> string = ''
>>> string.isspace()
False
>>> string = "\r"
>>> string.isspace()
True
>>> string = "\t"
>>> string.isspace()
True
>>> string = "7 Cajas"
>>> string.istitle()
True
>>> string = "Un Titulo Dos"
>>> string = istitle()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    string = istitle()
NameError: name 'istitle' is not defined
>>> string
'Un Titulo Dos'
>>> string.istitle()
True
>>> string.strip()
'Un Titulo Dos'
>>> string = "  python es gen  "
>>> string.strip()
'python es gen'
>>> string.split(", ")
['  python es gen  ']
>>> string = "1, 2, 3, 4"
>>> string.split(", ")
['1', '2', '3', '4']
>>> string = "WHATEVER"
>>> string.isupper()
True
>>> string = "WHATEVER3"
>>> string.isupper()
True