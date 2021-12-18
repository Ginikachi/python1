Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>
>>> ## No 1:
>>> def find_dups(List):
	""" (list) -> set()
 
        Takes a list of intergers as its input argument and returns a set
        of those integers that occur two or more times in the list.

        >>> [1, 2, 4, 2, 1, 6, 4, 4]
        {1, 2, 4}
        """
	Duplicates = set()
	for numbers in List:
		if List.count(numbers) > 1:
			Duplicates.add(numbers)

	return Duplicates

>>> find_dups([1, 2, 4, 2, 1, 6, 4, 4])
{1, 2, 4}
>>> find_dups([-7, 8, -7])
{-7}
>>> find_dups([1, 2, 3, 4])
set()
>>> 
>>> ## See 3 alternative solutions for no 1 above without using functon
>>> ## definition in 'Rough-exercise.py'
>>> 
>>> ## 4th alternative for no 1 above, based on the fact that values in sets
>>> ## are unique, i.e can't occur more than once, so length remains the same:
>>> 
>>> def find_dups(L):
	""" (list) -> set

        Return the number of duplicates numbers from L.

        >>> find_dups([1, 1, 2, 3, 4, 2])
        {1, 2}
        >>> find_dups([1, 2, 3, 4])
        set()
        """

	elem_set = set()
	dups_set = set()

	for entry in L:
		len_initial = len(elem_set)
		elem_set.add(entry)
		len_after = len(elem_set)
		if len_initial == len_after:
			dups_set.add(entry)

	return (dups_set)

>>> find_dups([1, 1, 2, 3, 4, 2])
{1, 2}
>>> find_dups([1, 2, 3, 4])
set()
>>> 
>>> ## No 2:
>>> 
>>> def mating_pairs(males, females):
	""" (set, set) -> set of tuple

        Return a set of tuples where each tuple contains a male from males and a
        female from females.

        >>> mating_pairspairs({'Anne', 'Beatrice', 'Cari'},{'Ali', 'Bob', 'Chen'})
        {('Cari', 'Chen'), ('Beatrice', 'Bob'), ('Anne', 'Ali')}
        """

	pairs = set()
	num_gerbils = len(males)

	for i in range(num_gerbils):

		gerbil_male = males.pop()
		gerbil_female = females.pop()
		pairs.add((gerbil_male, gerbil_female),)

	return pairs

>>> mating_pairs({'Anne', 'Beatrice', 'Cari'},{'Ali', 'Bob', 'Chen'})
{('Cari', 'Chen'), ('Anne', 'Bob'), ('Beatrice', 'Ali')}
>>> 

>>> ## (NB: set does not support indexing e.g male[i])
>>> 
>>> ================================ RESTART ================================
>>> 
>>> ## No 3:
>>> 
>>> def get_authors(filenames):
	""" (list of str) --> set of str

	Takes a list of filenames in PDB file format as an input argument and
	returns the set of all author names found in the files.
	"""

	authors_name = set()
	for file in filenames:
		pdb_file = open(file)

		for line in pdb_file:
			line = line.strip()
			if line.lower().startswith('author'):
				for name in line.split()[1:]:
					authors_name.add(name)

	return authors_name

>>> get_authors(['Author1.pdb', 'Author2.pdb'])
{'James', 'Sharon', 'Mary', 'John', 'Peter', 'Cherry'}
>>> 

>>> ##(see alternative answer for no 3 above in answer textbook. The answer in
>>> ## textbook looks more complicated and may need some modification because of
>>> ## the answer it gave)
>>> 
>>> ## No 4:
>>> 
>>> def count_values(dictionary):
	""" (dict) -> int
	Return the number of unique values in dictionary.
	>>> {'red': 1, 'green': 1, 'blue': 2, 'yellow': 3}
	2
	3
	>>> {'red': 1, 'green': 1, 'blue': 2}
	2
	"""
	observation_list = []
	for colour, observation in dictionary.items():
		observation_list.append(observation)
	Result = []
	for unique_value in observation_list:
		if observation_list.count(unique_value) == 1:
			Result.append(unique_value)
	for x in Result:
		print(x)

		
>>> count_values({'red': 1, 'green': 1, 'blue': 2, 'yellow': 3})
3
2
>>> count_values({'red': 1, 'green': 1, 'blue': 2})
2
>>> count_values({'red': 1, 'green': 1})
>>> 
>>> ##(NB: See alternative solution to No 4 in 'Rough - exercise.py').
>>> 
>>> ## NO 5:
>>> 
>>> def least_likely
SyntaxError: invalid syntax
>>> 
>>> def least_likely(particle_to_probability):
	""" (dict) -> str

	Return the particle from particle_to_probability with the lowest
        probability

        >>> {'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07,
            'neutrino': 0.14}
        'meson'
        """
	smallest = 1
	name = ''
	for particle, probability in particle_to_probability.items():
		if probability < smallest:
			smallest = probability
			name = particle
	return name

>>> least_likely({'neutron': 0.55, 'proton': 0.21, 'meson': 0.03, 'muon': 0.07,
        'neutrino': 0.14})
'meson'
>>> 
>>> ## No 6:
>>> 
>>> def count_duplicates(dictionary):
	""" (dict) -> int

	Return the number of values in a dictionary that appears two or more
	times.

	>>> count_duplicates({'k':1, 'v':1, 'c':2, 'd':3, 'e':3, 'f':3})
	2
	>>> count_duplicates({'R': 5, 'G': 2, 'B': 2, 'Y': 1, 'P': 3})
	1
	"""
	duplicate = 0
	original = list(dictionary.values())
	seen = []
	for item in original:
		if not item in seen:
			if original.count(item) > 1:
				duplicate = duplicate + 1
				seen.append(item)
	return duplicate

>>> count_duplicates({'k':1, 'v':1, 'c':2, 'd':3, 'e':3, 'f':3})
2
>>> count_duplicates({'R': 5, 'G': 2, 'B': 2, 'Y': 1, 'P': 3})
1
>>> ## alternative solution to No 6:
>>> 
>>> def count_duplicates(dictionary):

	duplicates = 0
	original = list(dictionary.values())
	
	for item in original:

		# if an item appears at least 2 times, it is a duplicate
		if original.count(item) >= 2:
			duplicates = duplicates + 1
			
			#remove that item from the list
			num_occurrences = original.count(item)
			for i in range(num_occurrences):
				original.remove(item)
	return duplicates

>>> count_duplicates({'k':1, 'v':1, 'c':2, 'd':3, 'e':3, 'f':3})
2
>>> count_duplicates({'R': 5, 'G': 2, 'B': 2, 'Y': 1, 'P': 3})
1
>>> ## what i understand from the second alternative to No 6 is this: once an
>>> ## item is counted, duplicated and removed from the original list, even if
>>> ## a similar item like it is encountered again in the original list, it will
>>> ## not be duplicated a second time.
>>> 
>>> ## No 7:

>>> def is_balanced(colour_to_factor):
	""" (dict of (str:float) -> bool

	Return True if and only if total of values in colour_to_factor is equal
	to 1, showing that dictionary represents a balanced colour.

	>>> is_balanced({'R': 0.5, 'G': 0.4, 'B': 0.7}
	False
	>>> is_balanced({'R': 0.3, 'G': 0.5, 'B': 0.2}
	True
	"""
	values = list(colour_to_factor.values())
	total = sum(values)
	return total == 1.0

>>> is_balanced({'R': 0.5, 'G': 0.4, 'B': 0.7})
False
>>> is_balanced({'R': 0.3, 'G': 0.5, 'B': 0.2})
True
>>> 
>>> ## No 8:
>>> 
>>> def dict_intersect(dict1, dict2):
	""" (dict, dict) -> dict

	Return a new dictionary that contains only the key/value pairs that
	occur in both dict1 and dict2.
	
	>>> dict_intersect({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
	{'e': 5, 'c': 3}
	"""
	intersection = {}
	for key, value in dict1.items():
		if key in dict2 and value == dict2[key]:
			intersection[key] = value
			
	return intersection

>>> dict_intersect({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5},
	       {'a': 4, 'c': 3, 'e': 5, 'f': 6})
{'e': 5, 'c': 3}
>>> 
>>> ## No 9:
>>> 
>>> def db_headings(dict_of_dict):
	""" (dict of dict) -> set

	Return a set of the keys in the inner dictionaries in dict_of_dict.
	
	>>> db_headings({'j': {'a':'b', 'w':'i'}, 'f': {'a':'d', 'm':'l'}})
	{'a', 'w', 'm'}
	>>> db_headings({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}})
	{1, 2, 3}
	"""
	
	inner_keys = set()
	for key, inner_dict in dict_of_dict.items():
		for inner_key in inner_dict:
			inner_keys.add(inner_key)
			
	return inner_keys

>>> db_headings({'j': {'a':'b', 'w':'i'}, 'f': {'a':'d', 'm':'l'}})
{'a', 'm', 'w'}
>>> db_headings({'A': {1: 'a', 2: 'b'}, 'B': {2: 'c', 3: 'd'}})
{1, 2, 3}
>>> 
>>> ## No 10:
>>> 
>>> Alternative 1:
	
SyntaxError: invalid syntax
>>> ## Alternative 1:
>>> 
>>> db_consistent(dict_of_dict):
	
SyntaxError: invalid syntax
>>> 
>>> ## No 10:
>>> ##Alternative 1:
>>> 
>>> def db_consistent(dict_of_dict):
	""" (dict of dict) -> bool

	Return True if all inner dictionaries in dict_of_dict contain the same
	keys.
	
	>>> db_consistent({'H': {1:'b', 2:'i'}, 'F': {2:'d', 1:'h'}})
	True
	>>> db_consistent({'H': {1:'b', 2:'i'}, 'F': {2:'d', 3:'g'}})
	False
	>>> db_consistent({'H': {1:'b', 2:'i'}, 'F': {1:'d', 2:'d', 3:'u'},
	            'W': {1:'s', 2:'j'}})
	False
	"""
	
	inner_keys_list = []
	for key, inner_dict in dict_of_dict.items():
		inner_keys = list(inner_dict.keys())
		inner_keys.sort()
		inner_keys_list.append(inner_keys)
		
	for i in range(1, len(inner_keys_list)):
		
		#If the number of keys is different.
		if len(inner_keys_list[0]) != len(inner_keys_list[i]):
			return False
		
		# If the keys don't match.
		for j in range(len(inner_keys_list[0])):
			if inner_keys_list[0][j] != inner_keys_list[i][j]:
				return False
			
	return True

>>> dict_of_dict = {'H': {1:'b', 2:'i'}, 'F': {2:'d', 1:'h'}}
>>> db_consistent(dict_of_dict)
True
>>> db_consistent({'H': {1:'b', 2:'i'}, 'F': {2:'d', 3:'g'}})
False
>>> db_consistent({'H': {1:'b', 2:'i'}, 'F': {1:'d', 2:'d', 3:'u'},
	            'W': {1:'s', 2:'j'}})
False
>>> ## NB: inner_dict.keys() returns a set.
>>> ##inner_keys.sort() allows for inner_keys_list[0][j] != inner_keys_list[i][j]
>>> ## to be used because it aligns elements e.g [a, b], [a, b].
>>> 
>>> ## Alternative 2:
>>> 
>>> def db_consistent(dict_of_dict):
	inner_keys_list = []
	
	for key, inner_dict in dict_of_dict.items():
		inner_keys = list(inner_dict.keys())
		inner_keys.sort()
		inner_keys_list.append(inner_keys)
		
	for item in inner_keys_list:
		if item != inner_keys_list[0]:
			return False
		
	return True

>>> db_consistent({'H': {1:'b', 2:'i'}, 'F': {2:'d', 1:'h'}})
True
>>> db_consistent({'H': {1:'b', 2:'i'}, 'F': {2:'d', 3:'g'}})
False
>>> db_consistent({'H': {1:'b', 2:'i'}, 'F': {1:'d', 2:'d', 3:'u'},
	            'W': {1:'s', 2:'j'}})
False
>>> 
>>> ## Alternative 3:
>>>
>>> def db_consistent(dict_of_dict):

	inner_keys_list = []
	
	for key, inner_dict in dict_of_dict.items():
		inner_keys = list(inner_dict.keys())
		inner_keys.sort()
		inner_keys_list.append(inner_keys)
		
	return inner_keys_list[1:] == inner_keys_list[:-1]

>>> db_consistent({'H': {1:'b', 2:'i'}, 'F': {2:'d', 1:'h'}})
True
>>> db_consistent({'H': {1:'b', 2:'i'}, 'F': {1:'d', 2:'d', 3:'u'},
	            'W': {1:'s', 2:'j'}})
False
>>> db_consistent({'H': {1:'b', 2:'i'}, 'F': {2:'d', 3:'g'}})
False
>>> 
>>> ## NB: inner_keys.sort() code is important in all alternatives because
>>> ## [a, b] != [b, a], even though they contain the same elements. Therefore
>>> ## to get the accurate answer for No 10, two lists with same elements a and
>>> ## b for example, must be sorted, so that 1st list = [a, b] and the 2nd
>>> ## list = [a, b], so that '1st list == 2nd list', which properly shows that
>>> ## they contain the same elements.
>>>
>>>
>>> ## No 11A: (Alternative 1):
>>> 
>>> def sparse_add(vector1, vector2):
	""" (dict of {int: int}, dict of {int: int}) -> dict of {int: int}

	Return the sum of sparse vectors vector1 and vector2.
	>>> sparse_add({1: 3, 3: 4}, {2: 4, 3: 5, 5: 6})
	{1: 3, 2: 4, 3: 9, 5: 6}
	>>> sparse_add({0: 1, 6: 3}, {1: 2, 4: 5, 6: 9})
	{0: 1, 1: 2, 4: 5, 6: 12}
	"""
	
	sum_vector = vector1.copy()
	
	for key in vector2:
		if key in sum_vector:
			sum_vector[key] = sum_vector[key] + vector2[key]
		else:
			sum_vector[key] = vector2[key]
			
	return sum_vector

>>> sparse_add({1: 3, 3: 4}, {2: 4, 3: 5, 5: 6})
{1: 3, 2: 4, 3: 9, 5: 6}
>>> sparse_add({0: 1, 6: 3}, {1: 2, 4: 5, 6: 9})
{0: 1, 1: 2, 4: 5, 6: 12}
>>> 
>>> ## NB: see other alternatives in No11_function_definitions.py. Also see
>>> ## there, solutions for other questions derived from No 11.
>>> 
>>> ## No 11B: (alternative1. see alternative 2 in No11_function_definitions.py)
>>> 
>>> def sparse_dot(vector1, vector2):
	""" (dict of {int: int}, dict of {int: int} -> dict of {int: int})

	Return the dot product of sparse vectors vector1 and vector2.
	>>> sparse_dot({1: 3, 3: 4}, {2: 4, 3: 5, 5: 6})
	20
	>>> sparse_dot({0: 1, 1: 2, 2: 3}, {0: 4, 1: 5, 2: 6})
	32
	>>> sparse_dot({0: 1, 6: 3}, {1: 2, 4: 5, 6: 9})
	27
	"""
	
	dot = 0
	
	for key1 in vector1:
		if key1 in vector2:
			dot = dot + vector1[key1] * vector2[key1]
			
	return dot

>>> sparse_dot({1: 3, 3: 4}, {2: 4, 3: 5, 5: 6})
20
>>> sparse_dot({0: 1, 1: 2, 2: 3}, {0: 4, 1: 5, 2: 6})
32
>>> sparse_add({0: 1, 6: 3}, {1: 2, 4: 5, 6: 9})
{0: 1, 1: 2, 4: 5, 6: 12}
>>> sparse_dot({0: 1, 6: 3}, {1: 2, 4: 5, 6: 9})
27
>>> 
