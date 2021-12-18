Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> ## See textbook for elaborate discussion on this chapter beyond the codes
>>> ## below.
>>> 
>>> ## 12.1: Searching for the smallest Values:
>>> ## Index method:
>>> 
>>> counts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
>>> low = min(counts)
>>> low
96
>>> min_index = counts.index(low)
>>> print(min_index)
6
>>> ## (the answer 6 is the index of the minimum, 96, in list count)
>>> 
>>> ## here is a more succint version:
>>> 
>>> counts = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
>>> counts.index(min(counts))
6
>>> 
>>> ## Now, to find the indices of the two smallest values, Lists don't have a
>>> ## method to do this directly, so we'll have to design an algorithm ourselves
>>> ## and then translate it to a Python function.
>>> 
>>> ## Algorithm alternative 1: Find, Remove, Find:
>>> ## the first teo algorithms below mutate the list, either by removing an item
>>> ## or by sorting the list. It is important that our algoritms put things back
>>> ## the way we found them, or the people who call our functions are going to be
>>> ## annoyed with us:
>>> 
>>> ## Which of the algorithms would be the fastest would be checked later on.
>>> 
>>> ## Algorithm alternative 1: Find, Remove, Find:
>>> 
>>> ## (see textbook for detailed explanation on how the algorithms were derived):
>>> 
>>> def find_two_smallest(L):
	""" (list of float) -> tuple of (int, int)

	Return a tuple of the indices of the two smallest values in list L.

	>>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
	(6, 7)
	"""

	# Find the index of the minimum and remove that item
	smallest = min(L)
	min1 = L.index(smallest)
	L.remove(smallest)

	# Find the index of the new minimum
	next_smallest = min(L)
	min2 = L.index(next_smallest)

	# Put smallest back into L
	L.insert(min1, smallest)

	# Fix min2 in case it was affected by the reinsertion:
	# If min1 comes before min2, add 1 to min2
	if min1 <= min2:
		min2 += 1

	return (min1, min2)

>>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
(6, 7)
>>> ## NB: the algorithms are the sentences beginning with # in the code.
>>> 
>>> ## Algorithm alternative 2: Sort, Identify Minimums, Get indices:
>>> 
>>> def find_two_smallest(L):
	""" (list of float) -> tuple of (int, int)

	Return a tuple of the indices of the two smallest values in list L.

	>>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
	(6, 7)
	"""

	# Get a sorted copy of the list so that the two smallest items are at the
	# front
	temp_list = sorted(L)
	smallest = temp_list[0]
	next_smallest = temp_list[1]

	# Find the indices in the original list L
	min1 = L.index(smallest)
	min2 = L.index(next_smallest)

	# Return the two indices:
	return (min1, min2)

>>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
(6, 7)
>>> 
>>> ## NB: for alternative 2, we could have used method list.sort to sort L, but
>>> ## taht breaks a fundamental rule: never mutate the contents of parameters
>>> ## unless the docstring says to. Therefore sorted(L) was used.
>>> 
>>> ## Algorithmn alternative 3: Walk Through the List:
>>> 
>>> def find_two_smallest(L):
	""" (list of float) -> tuple of (int, int)

	Return a tuple of the indices of the two smallest values in list L.

	>>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
	(6, 7)
	"""

	# Set min1 and min2 to the indices of the smallest and next-smallest
	# values at the beginning of L
	if L[0] < L[1]:
		min1, min2 = 0, 1
	else:
		min1, min2 = 1, 0

	# Examine each value in the list in order
	for i in range(2, len(L)):
		# L[i] is smaller than both min1 and min2, in between, or
		# larger than both

		# New smallest?
		if L[i] < L[min1]:
			min2 = min1
			min1 = i

		# New second smallest?
		elif L[i] < L[min2]:
			min2 = i

	return(min1, min2)

>>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
(6, 7)
>>> ## NB: remember to see textbook to see ow initial algorithms were broken
>>> ## down to derive the final algorithms here, that can be translated to python.
>>> 
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
>>> ## 12.2: Timing The Functions:
>>> ================================ RESTART ================================
>>> 
"Find, remove, find" took 0.02ms.
"Sort, get minimums" took 0.02ms.
"Walk through the list" took 0.02ms.
>>> ## The answers above is not consistent with result in textbook (does it have
>>> ## to do with version of python used? Is this version faster than the one
>>> ## the textbook used?)
>>> ##(or is the method used here obsolete for this version, i.e perf_counter?)
