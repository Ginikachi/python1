Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>  ## No. 1:
>>> kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
>>> kingdoms[0]
'Bacteria'
>>> kingdoms[5]
'Animalia'
>>> kingdoms[0:3]
['Bacteria', 'Protozoa', 'Chromista']
>>> kingdoms[2:5]
['Chromista', 'Plantae', 'Fungi']
>>> kingdoms[4:]
['Fungi', 'Animalia']
>>> kingdoms.clear()
>>> 
>>> ## The above produces the empty list. It can also be produced as below:
>>> kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
>>> kingdoms[1:0]
[]
>>> kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
>>> kingdoms [0:0]
[]
>>> kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
>>> kingdoms[2:0]
[]
>>> ## No. 2: Repeat No 1 using negative indices:
>>> kingdoms[-6]
'Bacteria'
>>> kingdoms[-1]
'Animalia'
>>> kingdoms[-6:-4]
['Bacteria', 'Protozoa']
>>> kingdoms[-4:-6]
[]
>>> kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
>>> kingdoms[-6:-3]
['Bacteria', 'Protozoa', 'Chromista']
>>> kingdoms[-4:-1]
['Chromista', 'Plantae', 'Fungi']
>>> kingdoms[-2:-1]
['Fungi']
>>> kingdoms[-2:0]
[]
>>> kingdoms[-2:]
['Fungi', 'Animalia']
>>> kingdoms[4:6]
['Fungi', 'Animalia']
>>> kingdoms[-1:-2]
[]
>>> kingdoms = ['Bacteria', 'Protozoa', 'Chromista', 'Plantae', 'Fungi', 'Animalia']
>>> kingdoms[3:2]
[]
>>> ## NB: indexing [any number:0] gives an empty list; also indexing [big:small]
>>> ## number gives an empty list.

>>> ## No. 3:
>>> appointments = ['9:00', '10:30', '14:00', '15:00', '15:30']
>>> appointments.append(5, '16:30')
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    appointments.append(5, '16:30')
TypeError: append() takes exactly one argument (2 given)
>>>
>>> appointments.append('16:30')
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30']
>>> 
>>> appointments_more = appointments + ['16:30']
>>> appointments_more
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30', '16:30']
>>> appointments
['9:00', '10:30', '14:00', '15:00', '15:30', '16:30']
>>> ## append modified the list and '+' created a new list;
>>> 
>>> ## No. 4:
>>> ids = [4353, 2314, 2956, 3382, 9362, 3900]
>>> ids.remove(3382)
>>> ids
[4353, 2314, 2956, 9362, 3900]
>>> ids = [4353, 2314, 2956, 3382, 9362, 3900]
>>> ids.index(9362)
4
>>> ids.insert(5, 4499)
>>> ids
[4353, 2314, 2956, 3382, 9362, 4499, 3900]
>>> ids += [5566, 1830]
>>> ids
[4353, 2314, 2956, 3382, 9362, 4499, 3900, 5566, 1830]
>>> ids.reverse()
>>> ids
[1830, 5566, 3900, 4499, 9362, 3382, 2956, 2314, 4353]
>>> ids.sort()
>>> ids
[1830, 2314, 2956, 3382, 3900, 4353, 4499, 5566, 9362]
>>> 
>>> ## No. 5:
>>> alkaline_earth_metals = [4, 12, 20, 38, 56, 88]
>>> alkaline_earth_metals.index(88)
5
>>> alkaline_earth_metals.count()
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    alkaline_earth_metals.count()
TypeError: count() takes exactly one argument (0 given)
>>> len(alkaline_earth_metals)
6
>>> alkaline_earth_metals(5)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    alkaline_earth_metals(5)
TypeError: 'list' object is not callable
>>> alkaline_earth_metals[5]
88
>>> alkaline_earth_metals[-1]
88
>>> len(alkaline_earth_metals)
6
>>> max(alkaline_earth_metals)
88
>>> 
>>> ## No. 6:
>>> temps = [25.2, 16.8, 31.4, 23.9, 28, 22.5, 19.6]
>>> temps.sort()
>>> temps
[16.8, 19.6, 22.5, 23.9, 25.2, 28, 31.4]
>>> temps[5]
28
>>> temps[5:]
[28, 31.4]
>>> temps[6]
31.4
>>> temps[6]
31.4
>>> temps[6:]
[31.4]
>>> temps
[16.8, 19.6, 22.5, 23.9, 25.2, 28, 31.4]
>>> cool_temps = temps[0:2]
>>> cool_temps
[16.8, 19.6]
>>> warm_temps = temps[2:7]
>>> warm_temps
[22.5, 23.9, 25.2, 28, 31.4]
>>> temps_in_celsius = cool_temps + warm_temps
>>> temps_in_celsius
[16.8, 19.6, 22.5, 23.9, 25.2, 28, 31.4]
>>> 
>>> ## No. 7:
>>> def same_first_last(L):
	""" {list) -> bool
        Precondition: len(L) >= 2

        Return True if and only if first item of the list is the same as the
        last.

        >>> same_first_last([3, 4, 2, 8, 3])
        True
        >>> same_first_last(['apple', 'banana', 'pear'])
        False
        >>> same_first_last([4.0, 4.5])
        False

        """
	return L[0] == L[-1]

>>> same_first_last([3, 4, 2, 8, 3])
True
>>> same_first_last(['apple', 'banana', 'pear'])
False
>>> same_first_last([4.0, 4.5])
False
>>> 
>>> ## No 8:
>>> def is_longer(L1, L2):
	""" (list, list) -> bool
        Return True if and only if the length of L1 is longer than the length
        of L2.

        >>> is_longer([1, 2, 3], [4, 5])
        True
        >>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
        False
        >>> is_longer(['a', 'b', 'c'], [1, 2, 3])
        False

        """
	return len(L1) > len(L2)

>>> is_longer([1, 2, 3], [4, 5])
True
>>> is_longer(['abcdef'], ['ab', 'cd', 'ef'])
False
>>> is_longer(['a', 'b', 'c'], [1, 2, 3])
False
>>> 
>>> ##  No 9:
>>> values = [0, 1, 2]
>>> values[1] = values
>>> values
[0, [...], 2]
>>> 
>>> ## (see exercise book for diagram of 'memory model' of No. 9)
>>> 
>>> ## No 10:
>>> units = [['km','miles','league'],['kg','pound','stone']]
>>> units[0]
['km', 'miles', 'league']
>>> units[1]
['kg', 'pound', 'stone']
>>> units[2]
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    units[2]
IndexError: list index out of range
>>> units[0][0]
'km'
>>> units[1][0]
'kg'
>>> units[0][1:]
['miles', 'league']
>>> units[1][0:2]
['kg', 'pound']
>>> 
>>> ## No. 11: Repeat No. 10 using negative indices:
>>> units[-2]
['km', 'miles', 'league']
>>> units[-1]
['kg', 'pound', 'stone']
>>> units[-2][-3]
'km'
>>> units[-1][-3]
'kg'
>>> units[-2][-2:]
['miles', 'league']
>>> units[-1][-3:-1]
['kg', 'pound']
>>> units[-1][-3:-2]
['kg']
>>> units[-1][:-1]
['kg', 'pound']
>>> 
