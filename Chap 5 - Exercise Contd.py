Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ##No 4: see answer for expalnation of question using truth table. See code
>>> ##below too:
>>> def turn_camera_on(L, T):
	if (L < 0.01) or (T > 0.0):
		if not ((L < 0.01) and (T > 0.0)):
			turn_camera_on
			return "turn camera on"
		else:
			return "turn camera off"

		
>>> turn_camera_on(0.02, 1)
'turn camera on'
>>> turn_camera_on(0.001, -1)
'turn camera on'
>>> turn_camera_on(0.001, 1)
'turn camera off'
>>> turn_camera_on(0.02, -1)
>>> 
>>> ##(try another alternative code below):
>>> 
>>> def turn_camera_on(L, T):
	if (L < 0.01) or (T > 0.0):
		if not ((L < 0.01) and (T > 0.0)):
			return "turn camera on"
		else:
			return"turn camera off"

		
>>> turn_camera_on(0.02, 1)
'turn camera on'
>>> turn_camera_on(0.001, -1)
'turn camera on'
>>> turn_camera_on(0.001, 1)
'turn camera off'
>>> turn_camera_on(0.02, -1)
>>> 
>>> 
>>> ## another code also correct for No 4:
>>> 
>>> def turn_camera_on(L, T):
	if (L < 0.01) != (T > 0.0):
		turn_camera_on
		return " turn camera on"
	else:
		return "turn camera off"

	
>>> turn_camera_on(0.02, 1)
' turn camera on'
>>> turn_camera_on(0.001, -1)
' turn camera on'
>>> turn_camera_on(0.001, 1)
'turn camera off'
>>> turn_camera_on(0.02, -1)
'turn camera off'
>>> ##(the above code might be the best option because it displayed the correct
>>> ## answer for the last example 'turn_camera_on(0.02, -1)).
>>> 
>>> ## No 5: 

>>> x = 3
>>> result = (abs(3) == 3)
>>> 
>>> abs(3) == 3
True
>>> result = abs(3) == 3
>>> result = abs(x) == x
>>> result
True
>>> x = -3
>>> result = abs(-3) == -3
>>> result
False
>>> 
>>> 

 
>>> ## No 6:

>>> def (difference):
	
SyntaxError: invalid syntax
>>> def different(a, b):
	if a != b:
		return "true"
	else:
		return "false"

	
>>> different(2, 3)
'true'
>>> different(2,2)
'false'
>>> ##(try another code below for no 6 to see if it works):
>>> def difference(a, b):
	return a != b

>>> difference(2, 3)
True
>>> difference(2, 2)
False
>>> ##(last code is preferred, because already a != b means that a must
>>> ## never be equal to b. so there is no need including the if else
>>> ## condition in the first code of no 6):
>>> 

>>> ## No. 7:
>>> Population = int(input('Enter the population: "))
		       
SyntaxError: EOL while scanning string literal
>>> Population = int (input('Enter the populstion: '))
Enter the populstion: 9000
>>> if Population < 10000000:
	print(Population)

	
9000
>>> 
>>> ## No 7b:
>>> population = int(input('Enter the population: '))
Enter the population: 9000
>>> if population > 10000000 and population < 35000000:
	print(population)

	
>>> 
>>> population = int(input('Enter the population: '))
Enter the population: 11000000
>>> if population > 10000000 and population < 35000000:
	print(population)

	
11000000
>>> 
>>> ## No 7c:
>>> number of people = int(input('Enter number of people: '))
SyntaxError: invalid syntax
>>> number_of_people = int(input('Enter number of people: '))
Enter number of people: 900
>>> area_occupied = float(input('Enter area occupied: '))
Enter area occupied: 20
>>> if (number_of_people/area_occupied) > 100:
	print("Densely populated.")

	
>>> number_of_people = int(input('Enter the number of people: '))
Enter the number of people: 9000
>>> area_occupied = float(input('Enter area occupied: '))
Enter area occupied: 20
>>> if (number_of_people/area_occupied) > 100:
	print("Densely populated.")

	
Densely populated.
>>> 
>>> ## 7d:
>>> population = 900
>>> land_area = 20
>>> if (population/land_area) > 100:
	print ("Densely populated.")
else:
	print("Sparsely populated.")

	
Sparsely populated.
>>> 
>>> ## No 8:

>>> def convert_temperature(t, source, target):
	""" (number, str, str) -> number

        Convert t from source temperature scale to target temperature scale
        and return the result.

        >>> convert_temperature(0, 'Celsius', 'Kelvin')
        273.15
        >>> convert_temperature(100, 'Celsius', 'Fahrenheit')
        212.0
        """
	if source == 'Kelvin':
		celsius = t - 273.15
	elif source == 'Celsius':
		celsius = t
	elif source == 'Fahrenheit':
		celsius = (t - 32) * 5 / 9
	elif source == 'Rankine':
		celsius = (t - 491.67) * 5 / 9
	elif source == 'Delisle':
		celsius = 100 - t * 2 / 3
	elif source == 'Newton':
		celsius = t * 100 / 33
	elif source == 'Reamur':
		celsius = t * 5 / 4
	elif source == 'Romer':
		celsius = (t - 7.5) * 40 / 21
	if target == 'Kelvin':
		return celsius + 273.15
	elif target == 'Celsius':
		return celsius
	elif target == 'Fahrenheit':
		return celsius * 9 / 5 + 32
	elif target == 'Rankine':
		return (celsius + 273.15) * 9 / 5
	elif target == 'Delisle':
		return (100 - celsius) * 3 / 2
	elif target == 'Newton':
		return celsius * 33 / 100
	elif target == 'Reamur':
		return celsius * 4 / 5
	elif target == 'Romer':
		return celsius * 21 / 40 + 7.5

	
>>> convert_temperature (0, 'Celsius', 'Kelvin')
273.15
>>> convert_temperature (100, 'Celsius', 'Fahrenheit')
212.0
>>> convert_temperature (150, 'Rankine', 'Celsius')
-189.8166666666667
>>> convert_temperature (200, 'Celsius', 'Celsius')
200
>>> 
## No. 9
>>> ph = 2
>>> if ph >= 3.0 and ph < 7.0:
	print(ph, "is acidic.")
elif ph < 3.0:
	print(ph, "is VERY acidic! Be careful.")

	
2 is VERY acidic! Be careful.
>>>
>>> ph = 3
>>> if ph >= 3.0 and ph < 7.0:
	print(ph, "is acidic.")
elif ph < 3.0:
	print(ph, "is VERY acidic! Be careful.")

	
3 is acidic.
>>> 
## No. 10:
>>> ph = float(input("Enter the ph level: "))
Enter the ph level: 6.4
>>> if ph < 7.0:
	print("It's acidic!")
elif ph < 4.0:
	print("It's a strong acid!")

	
It's acidic!
>>> ph = float(input("Enter the ph level: "))
Enter the ph level: 3.6
>>> if ph < 7.0:
	print("It's acidic!")
elif ph < 4.0:
	print("It's a strong acid!")

	
It's acidic!
>>> ph = float(input("Enter the ph level: "))
Enter the ph level: 3.6
>>> if ph >= 4.0 and ph < 7.0:
	print("It's acidic!")
elif ph < 4.0:
	print("It's a strong acid!")

It's a strong acid!
>>> ## No 10 c redo:
>>> ## No 10c redo: (NB; The questions wants both messages to be displayed
>>> ## if a value less 4 is entered: in this case, elif is not needed.
>>> 
>>> ph = float(input("Enter the ph level: "))
Enter the ph level: 3.6
>>> if ph < 7.0:
	print("It's acidic!")
	if ph < 4.0:
		print("It's a strong acid!")

		
It's acidic!
It's a strong acid!
>>> 
##  No. 11:
>>> ## No 11a: The reason why the code checks whether someone is light is
>>> ## because that is a better mental match with the table: the first cell
>>> ## is for young, light people, and so it is natural to have a Boolean
>>> ## variable to match that.
>>> ## No. 11b:
>>> age = 40
>>> bmi = 24
>>> young = age < 45
>>> heavy = bmi>= 22.0
>>> if young and not heavy:
	risk = 'low'
elif young and heavy:
	risk = 'medium'
elif not young and not heavy:
	risk = 'medium'
elif not young and heavy:
	risk = 'high'

	
>>> risk
'medium'
