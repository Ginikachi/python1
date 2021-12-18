Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> fruit = 'pineapple'
>>> fruit.replace('p', 'd', 2)
'dineadple'
>>> ## No 9:
>>> season = 'summer'
>>> 'I love {0}'.format(season)
'I love summer'
>>> ## No 10:
>>>
>>> side1 = 3
>>> side2 = 4
>>> side3 = 5
>>> 'The sides have lengths {0}, {1}, and {2}.'.format(side1, side2, side3)
'The sides have lengths 3, 4, and 5.'
>>> ## No 11:
>>> 'boolean'.capitalize()
'Boolean'
>>> 'boolean'.upper()
'BOOLEAN'
>>> 'CO2 H2O'.find('2')
2
>>> 'CO2 H2O'.find('2', 'CO2 H2O'.find('2') + 1)
5
>>> 'Boolean'.islower()
False
>>> 'Boolean'[0].islower()
False
>>> 'MoNDaY'.lower().capitalize()
'Monday'
>>> '  Monday'.lstrip()
'Monday'
>>> 
>>> ## No 12:
>>> def total_occurrences(s1, s2, ch):
	""" (str, str, str) -> int

        Precondition: len(ch) == 1

        Return the total number of times that ch occurs in s1 and s2.

        >>> total_occurrences('color', 'yellow', 'l')
        3
        >>> total_occurrences('red', 'blue', 'l')
        1
        >>> total_occurrences('green', 'purple', 'b')
        0
        """
	total = (s1 + s2). count(ch)
	return total

>>> total_occurrences('color', 'yellow', 'l')
3
>>> total_occurrences('red', 'blue', 'l')
1
>>> total_occurrences('green', 'purple', 'b')
0
>>> 
>>> ## ALTERNATIVE METHOD:
>>> def total_occurrences(s1, s2, ch):

	return s1.count(ch) + s2.count(ch)

>>> total_occurrences('color', 'yellow', 'l')
3
>>> total_occurrences('red', 'blue', 'l')
1
>>> total_occurrences('green', 'purple', 'b')
0
>>> 
