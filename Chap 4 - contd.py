Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> print('a','b','c') # the separator is a space by default
a b c
>>> print('a','b','c', sep=',')
a,b,c
>>> 
KeyboardInterrupt
>>> print('a','b','c', sep=', ')
a, b, c
>>> print('a', 'b', 'c', sep=', ', end='') #prints without starting a new line
a, b, c
>>> print('a', 'b', 'c', sep=', ', end=' ')
a, b, c 
>>> 
>>> ## Typically, end='' is used only in programs, not in the shell.

SyntaxError: invalid syntax
>>> 
>>> #4.5: GETTING INFORMATION FROM THE KEYBOARD
>>> # using the built-in function 'input'
>>> 
>>> species = input()
Homo sapiens
>>> species
'Homo sapiens'
>>> population = input()
123461
>>> population
'123461'
>>> type(population)
<class 'str'>
>>> # the input() returns whatever the user enters as string, even if it looks
>>> #like a string. Use int or float to enter number
>>> 
>>> population = input()
2341
>>> population
'2341'
>>> population = int(population)
>>> population
2341
>>> population = population + 1
>>> population
2342
>>> ## in a shorter form:
>>> 
>>> population = int(input())

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    population = int(input())
ValueError: invalid literal for int() with base 10: ''
>>> 
>>> population = int(input())
2341
>>> population = population + 1
>>> population
2342
>>> 
>>> ## input can be given a string argument, which is used to prompt the user
>>> ## for input
>>> 
>>> species = input("Please enter a species: ")
Please enter a species: Python curtus
>>> species
'Python curtus'
>>> print(species)
Python curtus
>>> 

>>> ##4.7. EXERCISES
>>> ## No 1:
>>> 'Computer' + 'Science'
'ComputerScience'
>>> 'Darwin\'s'
"Darwin's"
>>> 'H20'*3
'H20H20H20'
>>> 'C02' * 0
''
>>> 
>>> ## NO 2:
>>> "They'll hibernate during the winter."
"They'll hibernate during the winter."
>>> '"Absolutely not," he said,'
'"Absolutely not," he said,'
>>> '"He said, 'Absolutely not,'" recalled Mel.'
SyntaxError: invalid syntax
>>> 
>>> '"He said, 'absolutely not,'" recalled Mel.'
SyntaxError: invalid syntax
>>> 
>>> '"He said, \'Absolutely not,\'" recalled Mel.'
'"He said, \'Absolutely not,\'" recalled Mel.'
>>> print ('"He said, \'Absolutely not,\'" recalled Mel.')
"He said, 'Absolutely not,'" recalled Mel.
>>> 
>>>  'hydrogen sulphide'
 
SyntaxError: unexpected indent
>>> 'hydrogen sulphide'
'hydrogen sulphide'
>>> 'left\right'
'left\right'
>>> 
>>> ## No 3:
>>> 'A\nB\nC'
'A\nB\nC'
>>> "A\nB\nC"
'A\nB\nC'
>>> 
>>> ##No 4:
>>> len()
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    len()
TypeError: len() takes exactly one argument (0 given)
>>> 
>>> len('')
0
>>> ## No 5:
>>> 'The rabbit is' + str(3) + '.'
'The rabbit is3.'
>>> print ('The rabbit is ' + str(3) + '.')
The rabbit is 3.
>>> print ('The rabbit is ' + str(3) + ' years old.')
The rabbit is 3 years old.
>>> 
>>> print ('The rabbit is ', str(3), '.')
The rabbit is  3 .
>>> print ('The rabbit is', str(3) '.')
SyntaxError: invalid syntax
>>> print ('The rabbit is', str(3), '.')
The rabbit is 3 .
>>> 
>>> x = 3
>>> y = 12.5
>>> print('The rabbit is', x.')
      
SyntaxError: EOL while scanning string literal
>>> print('The rabbit is', x, '.')
The rabbit is 3 .
>>> print('The rabbit is', x, + '.')
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    print('The rabbit is', x, + '.')
TypeError: bad operand type for unary +: 'str'
>>> print('The rabbit is', x + '.')
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    print('The rabbit is', x + '.')
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
>>> print('The rabbit is ' + x + '.')
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    print('The rabbit is ' + x + '.')
TypeError: Can't convert 'int' object to str implicitly
>>> 
>>> print('The rabbit is', x  '.')
SyntaxError: invalid syntax
>>> 
>>> print ('The rabbit is ' + str(x) + '.')
The rabbit is 3.
>>> ### NOTE FOR THE ABOVE ERRORS: comma gives space in print.
>>> ###'comma' and '+' may not go together in print. 
>>> ### If you do not want the space that comma gives, use + but remember to
>>> # add str to the variable e.g str(x), to get the number assigned to x.
>>> 
>>> print('The rabbit is ' + str(x) + ' years old.')
The rabbit is 3 years old.
>>> 
>>> print(y, 'is average.')
12.5 is average.
>>> print('The rabbit is', x, 'years old.')
The rabbit is 3 years old.
>>> 
>>> print(y, '*', x)
12.5 * 3
>>> 
>>> print(str(y) + ' * ' + str(3) + ' is 37.5.')
12.5 * 3 is 37.5.
>>> 
>>> ## No 6:
>>> first = 'John'
>>> last= 'Doe'
>>> print(last + ', ' + first)
Doe, John
>>> 
>>> ##No 7:
>>> num = float(input())
24
>>> print (num)
24.0
>>> 
>>> ## No 8:
>>> 
>>> def repeat(s, n):
	""" (str, int) -> str

        Return s repeated n times; if n is negative, return the empty string.

        >>> repeat('yes', 4)
        'yesyesyesyes'
        >>> repeat('no', 0)
        ''
        >>> repeat('no', -2)
        ''
        >>>repeat('yesnomaybe', 3)
        yesnomaybeyesnomaybeyesnomaybe

        """

	
>>> def repeat(s, n):
	""" (str, int) -> str

        Return s repeated n times; if n is negative, return the empty string.

        >>> repeat('yes', 4)
        'yesyesyesyes'
        >>> repeat('no', 0)
        ''
        >>> repeat('no', -2)
        ''
        >>>repeat('yesnomaybe', 3)
        yesnomaybeyesnomaybeyesnomaybe

        """
	return s * n

>>> repeat('yes', 4)
'yesyesyesyes'
>>> repeat('no', 0)
''
>>> repeat('no', -2)
''
>>> repeat('yesnomaybe', 3)
'yesnomaybeyesnomaybeyesnomaybe'
>>> 
>>> ## No 9:
>>> 
>>> def total_length(s1, s2):
	"""(str, str) -> int

        Return the sum of the lengths of s1 and s2.

        >>> total_length('yes', 'no')
        5
        >>> total_length('yes', '')
        3
        >>>total_length('YES!!!!', 'Noooooo')
        14
        """
	return len(s1) + len(s2)

>>> total_length('yes', 'no')
5
>>> total_length('yes', '')
3
>>> total_length('YES!!!!', 'Noooooo')
14
>>> 

>>> ##revisiting some of No2:
>>> print('left\right')
leftight
>>> print('left\\right')
left\right
>>> '''"He said, 'Absolutely not,'" recalled Mel.'''
'"He said, \'Absolutely not,\'" recalled Mel.'
>>> 
