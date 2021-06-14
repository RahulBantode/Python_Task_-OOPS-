''' Operations on Sets progrm run it on command line

>>> hello_rahul={'one','two','three','one','two','four','five','one','six'}
>>> type(hello_rahul)
<class 'set'>
>>> print(hello_rahul)
{'four', 'two', 'five', 'one', 'six', 'three'}
>>> 'seven' in hello_rahul
False
>>> 'One' in hello_rahul]
  File "<stdin>", line 1
    'One' in hello_rahul]
                        ^
SyntaxError: invalid syntax
>>> 'One' in hello_rahul
False
>>> 'one' in hello_rahul
True
>>> a=set()
>>> a={'rahu','bantode'}
>>> type(a)
<class 'set'>
>>> set('abcded')
{'a', 'b', 'e', 'c', 'd'}
>>> set1=set('abcdedgsd')
>>> set2=set('rahgfelmn')
>>> a | b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined
>>> set1 | set2
{'f', 'm', 'l', 'n', 'g', 's', 'a', 'e', 'c', 'r', 'd', 'b', 'h'}
>>> set1-set2
{'c', 's', 'd', 'b'}
>>> set2-set1
{'f', 'm', 'n', 'l', 'r', 'h'}
>>> set1 & set2
{'g', 'a', 'e'}
>>>  set1 ^ set2
  File "<stdin>", line 1
    set1 ^ set2
    ^
IndentationError: unexpected indent
>>> set1 ^ set2
{'f', 'm', 'l', 'n', 's', 'b', 'c', 'r', 'h', 'd'}
>>>
'''