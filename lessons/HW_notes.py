"""note 1"""
#python cannot distinguish the difference between:
#a == b and a = b
# undetected bugs may occur due to this reason

"""note 2"""
#yellow_exist: bool=False
#write "yellow_exist is not True" or "not yellow_exist"
#do not write "yellow_exist != True"

"""note 3"""
#how to access REPL
#Open the command palette, look for “Start REPL”

"""note 4"""
#当用首行缩进的时候，想要进入缩进的function还需要一个空格

"""note 5"""
#funcntion 和 function 之间需要空两行

"""note 6"""
#def name(name: list[int]) the parameter of list has to
#define a type such as [int]

"""note 7"""
#if x:
#this means if x != 0:

"""note 8"""
#if x in list/dict:
#可以用在dict，也可以用在list

"""note 9"""
#unit tests
#in order to test the function with the same name
#from module import function...
#do not from file import module
#if so, each function should be module.function instead of its name only

"""note 10"""
#format to write a class
"""
from __future__ import annotations

class <class name>:
    """"""
    <attribute name> = <variable type>

    def __init__(self, ,):
    
    def ->
"""

"""note 11"""
#string object cannot use reassignment operator
"""
a = 'abc'
a[0] = 'e'
print(a)

not working
"""

#list object can use reassignment operator
"""
a = ['a','b','c']
a[0] = 'e'
print(a)
"""

#dict object cannot use append
"""
a = {'a': 1,'b': 2,'c': 3}
a.append('e')
print(a)

not working
"""

#instead use
"""
a['a'] = 2
a['e'] = 4
a.pop('a')
"""

"""note 12"""
#class name, the name of the class is by convention capitalized.