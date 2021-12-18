Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ## No 1:
>>> celegans_phenotypes = ['Emb', 'Him', 'Unc', 'Dpy', 'Sma']
>>> for phenotypes in celegans_phenotypes:
	print (phenotypes)

	
Emb
Him
Unc
Dpy
Sma
>>> 
>>> ## No 2:
>>> half_lives = [887.7, 24100.0, 6563.0, 14, 373300.0]
>>> for values in half_lives:
	print(values, end=' ')

	
887.7 24100.0 6563.0 14 373300.0 
>>> 
>>> ## No 3:
>>> whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> for more_whales in whales:
	more_whales = more_whales + 1
	print (more_whales)

	
6
5
8
4
3
4
3
7
5
3
2
8
2
4


>>> ## No 3 alternative:
>>> 
>>> whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
>>> more_whales = []
>>> for count in whales:
	more_whales.append(count + 1)

	
>>> more_whales
[6, 5, 8, 4, 3, 4, 3, 7, 5, 3, 2, 8, 2, 4]
>>> ## we want the result to be in list form, without modifying the original
>>> ## list 'whales'. The correct answer format is 'No 3 alternative' above.
>>> 
>>> ## No 4:
>>> alkaline_earth_metals = [[4, 9.012], [12, 24.305], [20, 40.078],
			 [38, 87.62], [56, 137.327], [88, 226]]
>>> for properties in alkaline_earth_metals:
	for atomic_values in properties:
		print(atomic_values, end=' ')
	print()

	
4 9.012 
12 24.305 
20 40.078 
38 87.62 
56 137.327 
88 226 
>>> ## (better still for No 4 b):
>>> for inner_list in alkaline_earth_metals:
	print(inner_list[0])
	print(inner_list[1])

	
4
9.012
12
24.305
20
40.078
38
87.62
56
137.327
88
226
>>> ## (third alternative for ## 4 b):
>>> for inner_list in alkaline_earth_metals:
	for items in inner_list:
		print(items)

		
4
9.012
12
24.305
20
40.078
38
87.62
56
137.327
88
226
>>> ## (this third alternative used nested loop for solution)
>>> ## either of the 2nd and 3rd alternatives are the correct answers since
>>> ## we are required to print the atomic number and atomic weight for each
>>> ## alkaline earth metal on a different line.
>>> 
>>> ## 4 c:
>>> number_and_weight = []
>>> for inner_list in alkaline_earth_metals:
	number_and_weight.append(inner_list[0])
	number_and_weight.append(inner_list[1])

	
>>> number_and_weight
[4, 9.012, 12, 24.305, 20, 40.078, 38, 87.62, 56, 137.327, 88, 226]
>>> 
>>> ## (alternative for 4c using nested 'for'loop):
>>> 
>>> number_and_weight = []
>>> for inner_list in alkaline_earth_metals:
	for items in inner_list:
		number_and_weight.append(items)

		
>>> number_and_weight
[4, 9.012, 12, 24.305, 20, 40.078, 38, 87.62, 56, 137.327, 88, 226]
>>> 
>>> ## No 5:
>>> def mystery_function(values):
	""" (list) -> list
        Return a copy of the list, values,and sublists it contains.
        The top-level sublists have their elements reversed in the returned
        list.

        >>> mystery_function([[1, 2, 3], [4, 5, 6]])
        [[3, 2, 1], [6, 5, 4]]
        """
	
	result = []
	for sublist in values:
		result.append([sublist[0]]) # to the new sublist, append the element
		                        # at index 0 (in front)of the given sublist
		for i in sublist[1:]:
			result[-1].insert(0, i) # at index 0(at the front) of the
			          # new sublist, insert subsequent elements of the
			         # given sublist, beginning with element at index 1
	return result

>>> 
KeyboardInterrupt
>>> mystery_function([[1, 2, 3], [4, 5, 6]])
[[3, 2, 1], [6, 5, 4]]
>>> ##(see answer textbook for probably a simpler 'comment' section for the above)
>>> 
>>> ## No 6:
>>> ================================ RESTART ================================
>>> 
Please enter a chemical formula(or 'quit' to exit): H2O
Water
Please enter a chemical formula(or 'quit' to exit): Quit
Unknown compound
>>> ================================ RESTART ================================
>>> 
Please enter a chemical formula(or 'quit' to exit): NH3
Ammonia
Please enter a chemical formula(or 'quit' to exit): H2O
Water
Please enter a chemical formula(or 'quit' to exit): quit
...exiting program
>>> ================================ RESTART ================================
>>> 
Please enter a chemical formula(or 'quit' to exit): H2O
Water
Please enter a chemical formula(or 'quit' to exit): QUIT
Unknown compound
>>> 
>>> ## (see No 6 code in the file exercise_formular.py).
>>> ================================ RESTART ================================
>>> 
Please enter a chemical formula(or 'quit' to exit): H2O
Water
Please enter a chemical formula(or 'quit' to exit): 2O
Unknown compound
Please enter a chemical formula(or 'quit' to exit): NH3
Ammonia
Please enter a chemical formula(or 'quit' to exit): Quit
Unknown compound
>>> 
>>> ================================ RESTART ================================
>>> 
Please enter a chemical formula(or 'quit' to exit): H2O
Water
Please enter a chemical formula(or 'quit' to exit): 2w
Unknown compound
Please enter a chemical formula(or 'quit' to exit): QUIT
...exiting program
>>> ##(see a better code option for No 6 in file trial.py)
>>> 
>>> ## No 7:
>>> country_populations = [1295, 23, 7, 3, 47, 21]
>>> total = 0
>>> for country in country_populations:
	total = total + country

	
>>> total
1396
>>> 
>>> ## No 8:
>>> rat1 = [2, 4, 6, 8, 10]
>>> rat2 = [1, 6, 8, 7, 9]
>>> for i in range(len(rat1)):
	if i == 0:
		if rat1[i] > rat2[i]:
			print("Rat 1 weighed more than rat 2 on day 1.")
		else:
			print("Rat 1 weighed less tahn rat 2 on day 2.")

			
Rat 1 weighed more than rat 2 on day 1.
>>>  ##(alternative method: without using nested if):
>>> if rat1[0] > rat2[0]:
	print("Rat 1 weighed more than rat 2 on day 1.")
else:
	print("Rat 1 weighed less than rat 2 on day 1.")

	
Rat 1 weighed more than rat 2 on day 1.
>>> 
>>> if rat1[2] > rat2[2]:
	print("Rat 1 weighed more than rat 2 on day 3.")
else:
	print("Rat 1 weighed less than rat 2 on day 3.")

	
Rat 1 weighed less than rat 2 on day 3.
>>> 
>>> ## No 8b:
>>> if rat1[0] > rat2[0]:
	if rat1[4] > rat2[4]:
		print("Rat 1 remained heavier than Rat 2.")
	else:
		print("Rat 2 became heavier than Rat 1.")

		
Rat 1 remained heavier than Rat 2.
>>> 
>>> rat1 = [2, 4, 6, 8, 9]
>>> rat2 = [1, 6, 8, 7, 10]
>>> if rat1[0] > rat2[0]:
	if rat1[4] > rat2[4]:
		print("Rat 1 remained heavier than Rat 2.")
	else:
		print("Rat 2 became heavier than Rat 1.")

		
Rat 2 became heavier than Rat 1.

>>> ## (a better method using nested if):
>>> if rat1[0] > rat2[0]:
	if rat1[-1] > rat2[-1]:
		print("Rat 1 remained heavier than Rat 2.")
	else:
		print("Rat 2 became heavier than Rat 1.")
else:
	print("Rat 2 became heavier than Rat 1.")

	
Rat 2 became heavier than Rat 1.
>>> rat1 = [1, 4, 6, 8, 9]
>>> rat2 = [2, 6, 8, 7, 6]
>>> if rat1[0] > rat2[0]:
	if rat1[-1] > rat2[-1]:
		print("Rat 1 remained heavier than Rat 2.")
	else:
		print("Rat 2 became heavier than Rat 1.")
else:
	print("Rat 2 became heavier than Rat 1.")

	
Rat 2 became heavier than Rat 1.
>>> rat1 = [1, 4, 6, 8, 9]
>>> rat2 = [2, 6, 8, 7, 10]
>>> if rat1[0] > rat2[0]:
	if rat1[-1] > rat2[-1]:
		print("Rat 1 remained heavier than Rat 2.")
	else:
		print("Rat 2 became heavier than Rat 1.")
else:
	print("Rat 2 became heavier than Rat 1.")

	
Rat 2 became heavier than Rat 1.
>>> ##(NB: This last code that is said to be better may need some modification at
>>> ## the last print statement since it did not give the correct answer for the
>>> ## immediate last answer above)
>>> 
>>> ##(alternative to 8b without nested if):
>>> 
>>> rat1 = [2, 4, 6, 8, 10]
>>> rat2 = [1, 6, 8, 7, 9]

>>> if rat1[0] > rat2[0] and rat1[-1] > rat2[-1]:
	print("Rat 1 remained heavier than Rat 2.")
else:
	print("Rat 2 became heavier than Rat 1.")

	
Rat 1 remained heavier than Rat 2.
>>> 
>>> ## No 9:
>>> for numbers in range(33, 50):
	print (numbers)

	
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
>>> ## No 10:
>>> for numbers in range(10):
	print (10 - numbers, end = ' ')

	
10 9 8 7 6 5 4 3 2 1 
>>> 
>>> ## No 11:
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
12.0
>>> 
>>> ## No 12:
>>> def remove_neg(num_list):
	index = 0
	while index < len(num_list):
		if num_list[index] < 0:
			del num_list[index]
		else:
			index = index + 1

			
>>> remove_neg([1, 2, 3, -3, 6, -1, -3, 1])
>>> remove_neg
<function remove_neg at 0x02E3C8E8>

>>> def remove_neg(num_list):
	index = 0
	while index < len(num_list):
		if num_list[index] < 0:
			del num_list[index]
		else:
			index = index + 1
	return num_list

>>> remove_neg([1, 2, 3, -3, 6, -1, -3, 1])
[1, 2, 3, 6, 1]
>>> 
>>> ## No 13:
>>> for width in range (1, 8):
	print(width * 'T')

	
T
TT
TTT
TTTT
TTTTT
TTTTTT
TTTTTTT
>>> 
>>> ## No 14:
>>> for width in range (1, 8):
	print(' ' * (7-width), 'T' * width)

	
       T
      TT
     TTT
    TTTT
   TTTTT
  TTTTTT
 TTTTTTT
>>> 
>>> ## No 15:
>>> ## (Using 'while' loop for nos 13 and 14):
>>> width = 0
>>> number = range(1, 8)
>>> while width < len(number):
	print('T' * number[width])
	width = width + 1

	
T
TT
TTT
TTTT
TTTTT
TTTTTT
TTTTTTT
>>> ## (alternative to above):
>>> width = 1
>>> while width < 8:
	print('T' * width)
	width = width + 1

	
T
TT
TTT
TTTT
TTTTT
TTTTTT
TTTTTTT
>>> 
>>> ## 15B:
>>> width = 1
>>> while width < 8:
	print(' ' * (7 - width), 'T' * width, sep=' ')
	width = width + 1

	
       T
      TT
     TTT
    TTTT
   TTTTT
  TTTTTT
 TTTTTTT
>>> 
