Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> ## No 1:
>>> 
>>> 'hello'.upper()
'HELLO'
>>>
>>> 'Happy Birthday!'.lower()
'happy birthday!'
>>>
>>> 'WeeeEEEEeeeEEEEeee'.swapcase()
'wEEEeeeeEEEeeeeEEE'
>>>
>>> 'ABC123'.isupper()
True
>>>
>>> 'aeiouAEIOU'.count('a')
1
>>>
>>> 'hello'.endswith('o')
True
>>>
>>> 'hello'.startswith('H')
False
>>>
>>> 'Hello {0}'.format('Python')
'Hello Python'
>>>
>>> 'Hello {0}! Hello{1}!'.format('Python','World')
'Hello Python! HelloWorld!'
>>> 
>>> ## No 2:
>>> 'tomato'.count('o')
2
>>> ## No 3:
>>> 'tomato'.find('o')
1
>>> ## No 4:
>>> 'tomato'.find('o', 3, 6)
5
>>> 'tomato'.find('o', 'tomato'.find('o') +1)
5
>>> 'tomato'.find('o', 1, 6)
1
>>> 'tomato'.find('o', 3)
5
>>> 'tomato'.find('o', 2)
5
>>> 'tomato'.find('o', 1)
1
>>> ## No 5
>>> 'avocado'.find('o', 'avocado'.find('o') + 1)
6
>>> 'avocado'.find('o')
2
>>> 

>>> 'avocadocado'.find('o', 'avocadocado'.find('o') + 2)
6
>>> 'avocadocado'.find('o', 7)
10
>>> 'avocadocado'.find('o', 'avocadocado'.find('o') + 3)
6
>>>
>>> 'avocadocado'.find('o', 'avocadocado'.find('o') + 1, 'avocadocado'.find ('o') + 2)
-1
>>> 'avocadocado'.find('o', 'avocadocado'.find('o') + 1, 'avocadocado'.find ('o') + 1)
-1
>>> ## No 6:
>>> 'runner'.replace('n', 'b')
'rubber'
>>> ## No 7:
>>> s = 'yes'
>>> s = '  yes  '
>>> s.strip()
'yes'
>>> ## No 8:
>>> fruit = 'pineapple'
>>> fruit.find('p', fruit.count('p'))
5
>>> ## fruit.count('p') was first executed, then fruit.find('p', 3), where 3
>>> ## is the result from fruit.count('p')
>>> 
>>> fruit.count(fruit.upper().swapcase())
1
>>> fruit.upper()
'PINEAPPLE'
>>> fruit.upper().swapcase()
'pineapple'
>>> fruit.count(fruit.upper().swapcase())
1
>>> ## order of execution: fruit.upper() then 'PINEAPPLE',swapcase() then
>>> ## fruit.count('pineapple')
>>> 
>>> fruit.count('pineapple')
1
>>> fruit.replace(fruit.swapcase(), fruit.lower())
'pineapple'
>>> ## fruit.swapcase() then fruit.lower() then fruit.replace('PINEAPPLE',
>>> ## 'pineapple')
>>> 
