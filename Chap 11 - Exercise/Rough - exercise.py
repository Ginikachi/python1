Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> ## No 1:
>>>
>>> Trial1 = [1, 2, 4, 2, 1, 6, 4, 4]
>>> numbers_to_observation = {}
>>> for figures in Trial1:
	if figures in numbers_to_observation:
		numbers_to_observation[figures] = numbers_to_observation[figures]+1
	else:
		numbers_to_observation[figures] = 1

		
>>> print (numbers_to_observation)
{1: 2, 2: 2, 4: 3, 6: 1}
>>> 
>>> find_dup = set()
>>> for numbers, observation in numbers_to_observation.items():
	if observation > 1:
		find_dup.add(numbers)

		
>>> print (find_dup)
{1, 2, 4}
>>> 
>>> ## (2nd alternative for number 1 above:)
>>> 
>>> from collections import Counter
>>> Trial1 = [1, 2, 4, 2, 1, 6, 4, 4]
>>> occurences = Counter(Trial1)
>>> print (occurences)
Counter({4: 3, 1: 2, 2: 2, 6: 1})
>>> find_dup = set()
>>> for numbers, observation in occurences.items():
	if observation > 1:
		find_dup.add(numbers)

		
>>> print (find_dup)
{1, 2, 4}
>>> 
>>> ## (3rd  alternative for number 1):
>>> 
>>> Trial1 = [1, 2, 4, 2, 1, 6, 4, 4]
>>> find_dup = set()
>>> for numbers in Trial1:
	if Trial1.count(numbers) > 1:
		find_dup.add(numbers)

		
>>> print (find_dup)
{1, 2, 4}
>>> ================================ RESTART ================================
>>> 
>>> find_dups([1, 2, 4, 2, 1, 6, 4, 4])
{1, 2, 4}
>>> 
>>> ## See function definition for above (using alternative 3) in Chap11-exercise.py


>>> ## No. 2:
>>> male = {'a', 'b'}
>>> female = { 'f', 'm'}
>>> mating_pair = set(((male.pop(), female.pop()), (male.pop(), female.pop())))
>>> mating_pair
{('b', 'm'), ('a', 'f')}
>>> 

>>> ## (best alternative for No 2):
>>> males = {'a', 'b'}
>>> females = {'f', 'm'}
>>> pairs = set()
>>> num_gerbils = len(males)
>>> for i in range(num_gerbils)
SyntaxError: invalid syntax
>>> for i in range (num_gerbils):

	gerbil_male = males.pop()
	gerbil_female = females.pop()
	pairs.add((gerbil_male, gerbil_female),)

	
>>> pairs
{('b', 'm'), ('a', 'f')}
>>> 
>>> ## NB: for the above you can also just say 'for i in male:' (i.e no need to
>>> ## use 'range(len(males))')
>>> ## No 4 (alternative 1):
>>> 
>>> colour_to_obs = {'red': 1, 'green': 1, 'blue': 2, 'yellow': 3}
>>> obs_list = []
>>> for colour, obs in colour_to_obs.items():
	obs_list.append(obs)

	
>>> for x in obs_list:
	if obs_list.count(x) == 1:
		print(x)

		
3
2
>>> ## No 4 (alternative 2):
>>> 
>>> colour_to_obs = {'red': 1, 'green': 1, 'blue': 2, 'yellow': 3}
>>> seen = []
>>> for colour, obs in colour_to_obs.items():
	if obs in seen:
		seen.remove(obs)
	else:
		seen.append(obs)

		
>>> print (seen)
[3, 2]
>>> ## (see Chap 11 - Exercise.py for function defintion of alternative 1)
