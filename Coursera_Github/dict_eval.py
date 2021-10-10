Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> d = {'a': 1, 'b':2, 'c':3}
>>> d.update({'a':5, 'd':4})
>>> del d['b']
>>> d.keys()
dict_keys(['a', 'c', 'd'])
>>> precios = {'manzana': 3.5, 'banana': 4.5, 'kiwi': 6.0, 'pera': 3.75, ‘ciruela’: 2.45, ‘durazno’: 4.55, ‘melon’: 7.35, ‘sandia’: 9.70, ‘anana’: 11.25}
SyntaxError: invalid character in identifier
>>> precios = {'manzana': 3.5, 'banana': 4.5, 'kiwi': 6.0, 'pera': 3.75, 'ciruela': 2.45, 'durazno': 4.55, 'melon': 7.35, 'sandia': 9.70, 'anana': 11.25}
>>> (2*3.5)+(2.5*4.5)+6.0+(3*3.75)+2.45+(2*4.55)+(5*7.35)+(10*9.70)+(3*11.25)
214.55
>>> d={'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5}
>>> d.setdefault('z',5) == 5
True
>>> d.get('z') == none
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    d.get('z') == none
NameError: name 'none' is not defined
>>> d.get('z') == None
False
>>> d={'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5}
>>> d.get('z') == None
True
>>> d.get('z', 7) == 7
True
>>> d['z']
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d['z']
KeyError: 'z'
>>> d{}
SyntaxError: invalid syntax
>>> d.setdefault('a',5) == 5
False
>>> d.get('a', 7) == 7
False
>>> d['a'] == 1
True
>>> d={‘a’: 1, ‘b’: 2, ‘c’: 3, ‘d’:4, ‘e’:5}
SyntaxError: invalid character in identifier
>>> d={'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5}
>>> d.pop('f', 2) == 2
True
>>> d.popitem() == ('e', 5)
True
>>> d={'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5}
>>> d.popitem() == (5)
False
>>> d.pop('a', 2) == 2
False
>>> d.pop() == 5
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    d.pop() == 5
TypeError: pop expected at least 1 argument, got 0
>>> d.pop('c') == 3
True
>>> d.keys()
dict_keys(['b', 'd'])
>>> import datetime
>>> datetime.date(2019,2,21)
datetime.date(2019, 2, 21)
>>> d.items()
dict_items([('b', 2), ('d', 4)])
>>> [x for x in d]
['b', 'd']
>>> [x for x in enumerate(d)]
[(0, 'b'), (1, 'd')]
>>> e = {}
>>> type(e)
<class 'dict'>
>>> g = {1,2,3}
>>> type(g)
<class 'set'>
>>> x = {'a' = 1, 'b' = 2}
SyntaxError: invalid syntax
>>> d
{'b': 2, 'd': 4}
>>> d={'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5}
>>> d['a'] == 1
True
>>> d.update((('a', 2)))
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    d.update((('a', 2)))
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> d.update((('a', 2),('b',3)))
>>> d
{'a': 2, 'b': 3, 'c': 3, 'd': 4, 'e': 5}
>>> d={'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5}d={'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5}
SyntaxError: invalid syntax
>>> d={'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5}
>>> d.pop('a',2) ==2
False
>>> d={'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5}
>>> d.popitem() == 5
False
>>> d={'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5}
>>> d.pop() == 5
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    d.pop() == 5
TypeError: pop expected at least 1 argument, got 0
>>> z = {1,2,3}
>>> type(z)
<class 'set'>
>>> z = ['a']
>>> type(z)
<class 'list'>
>>> z = {datetime.date(2019,2,21)}
>>> type(z)
<class 'set'>
>>> [x for x in d]
['a', 'b', 'c', 'd', 'e']
>>>  [x for x in enumerate(d)]
 
SyntaxError: unexpected indent
>>> [x for x in enumerate(d)]
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
>>> 