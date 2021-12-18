## No 1a:
## Iterate over each character in the sequence from the beginning to end,
## replacing each A, T, G, and C with its T, A, C, and G, respectively.

## No 1b: Answer = No.

## No 1c: Alternative 1:

##def complement(DNA):
##    """ (string) -> string
##
##    Return the complement of a DNA sequence
##
##    >>> complement('AATTGCCGT')
##    TTAACGGCA
##    """
##
##    complement = ""
##
##    for i in DNA:
##        if i == "A":
##            complement += "T"
##        elif i == "T":
##            complement += "A"
##        elif i == "G":
##            complement += "C"
##        elif i == "C":
##            complement += "G"
##    return complement
##
##print(complement("AATTGCCGT"))

## No 1c: Alternative 2 (using dictionary):

##def complement(sequence):
##    """ (str) -> str
##
##    Return the complement of sequence.
##
##    >>> complement('AATTGCCGT')
##    'TTAACGGCA'
##    """
##
##    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
##    sequence_complement = ''
##
##    for char in sequence:
##        sequence_complement = sequence_complement + complement_dict[char]
##
##    return sequence_complement
##
##print(complement('AATTGCCGT'))

## No 2a: find minimum value and value's index in one pass through the list.

##L = [5, 3, 4, 2, 6, 7]
##index = 0
##smallest = L[0]
##
##for i in range(1, len(L)):
##    if L[i] < smallest:
##        index = i
##        smallest = L[i]
##
##print (smallest, index)

## No 2b:

##def min_index(L):
##    """ (List) -> (object, int)
##
##    Return a tuple containing the smallest item from L and the item's index.
##
##    >>> min_index([5, 3, 4, 2, 6, 7])
##    (2, 3)
##    >>> min_index([4, 4, 5, 1, 7, 0])
##    (0, 5)
##    """
##
##    index = 0
##    smallest = L[0]
##
##    for i in range(1, len(L)):
##        if L[i] < smallest:
##            index = i
##            smallest = L[i]
##
##    return (smallest, index)
##
##print(min_index([5, 3, 4, 2, 6, 7]))
##print(min_index([4, 4, 5, 1, 7, 0]))

## No 2c: (aternative 1)

##def min_or_max_index(L, flag):
##    """ (List, bool) -> (object, int)
##
##    Return the minimum or maximum item and its index from L, depending on
##    whether flag is True or False.
##
##    >>> min_or_max_index([4, 3, 2, 4, 3, 6, 1, 5], True)
##    (1, 6)
##    >>> min_or_max_index([4, 3, 2, 4, 3, 6, 1, 5], False)
##    (6, 5)
##    """
##    if flag == True:
##        index = 0
##        smallest = L[0]
##
##        for i in range(1, len(L)):
##            if L[i] < smallest:
##                index = i
##                smallest = L[i]
##                
##        return (smallest, index)
##
##    else:
##        if flag == False:
##            index = 0
##            largest = L[0]
##
##            for i in range(1, len(L)):
##                if L[i] > largest:
##                    index = i
##                    largest = L[i]
##                    
##            return(largest, index)

## No 2c: (Alternative 2):
##def min_or_max_index(L, flag):
##    """ (List, bool) -> (object, int)
##
##    Return the minimum or maximum item and its index from L, depending on
##    whether flag is True or False.
##
##    >>> min_or_max_index([4, 3, 2, 4, 3, 6, 1, 5], True)
##    (1, 6)
##    >>> min_or_max_index([4, 3, 2, 4, 3, 6, 1, 5], False)
##    (6, 5)
##    """
##    index = 0
##    current_value = L[0]
##
##    if flag:
##        for i in range(1, len(L)):
##            if L[i] < current_value:
##                index = i
##                current_value = L[i]
##    else:
##        for i in range(1, len(L)):
##            if L[i] > current_value:
##                index = i
##                current_value = L[i]
##    return (current_value, index)
##
##print (min_or_max_index([4, 3, 2, 4, 3, 6, 1, 5], True))
##print (min_or_max_index([4, 3, 2, 4, 3, 6, 1, 5], False))

## For No2c: alternative 2, 'True' automatically takes the first part of the code
## while 'False' takes the second part(i.e. after 'else:' up to before 'return..')
## Therefore, if you reverse the symbols, i.e the first part having > and the
## second part having <, the answer will be (6,5) for True and (1, 6) for False.

## No 3a: (algorithm for alternative 1 of No 3b):
##- Read the description line.
##- Keep reading the comment lines until we read the first piece of data.
##- Add the first piece of data to an empty list.
##- Read the remaining lines one at a time, appending the data to the list.
##- sum up the items in the list
##- get the length of the list.
##- get average of items in the list


## No 3b: (alternative 1):

##def hopedale_average(filename):
##    """ (str) -> float
##
##    Return the average number of pelts produced per year for the data in
##    Hopedale file named filename
##    """
##    with open(filename, 'r') as hopedale_file:
##
##        # Read the description line.
##        hopedale_file.readline()
##
##        #keep reading comment lines until we read the first piece of data.
##        data = hopedale_file.readline().strip()
##        while data.startswith('#'):
##            data = hopedale_file.readline().strip()
##
##        # Now we have the first piece of data append it to an empty list.
##        hopedale_list = []
##        hopedale_list.append(int(data))
##
##        # Read the rest of the data.
##        for data in hopedale_file:
##            hopedale_list.append(int(data.strip()))
##
##        total_pelt = sum(hopedale_list)
##        length_pelt = len(hopedale_list)
##
##        Average = (total_pelt / length_pelt)
##
##    return Average
##
##print (hopedale_average('hopedale.txt'))



## No 3b: (alternative 2):

##def hopedale_average(reader):
##    
##    data = reader.readline()
##
##    data = reader.readline().strip()
##    while data.startswith('#'):
##        data = reader.readline().strip()
##
##    total_pelts = int(data)
##    count = 1
##
##    for data in reader:
##        total_pelts = total_pelts + int(data.strip())
##        count = count + 1
##
##    Average = total_pelts / count
##
##    return Average
##
##if __name__ == '__main__':
##    with open('hopedale.txt', 'r') as hopedale_file:
##        average = hopedale_average(hopedale_file)
##        print (average)

## No 4:

##def find_two_smallest(L):
##    """ (List of float) -> tuple of (int, int)
##
##    Return a tuple of the indices of the two smallest values in list L.
##
##    >>> find_two_smallest([809, 834, 477, 478, 307, 122, 96, 102, 324, 476])
##    (6, 7)
##    >>> find_two_smallest([3, 5, 2])
##    (2, 0)
##    >>> find_two_smallest([1, 2])
##    (0, 1)
##    >>> find_two_smallest([3, 2])
##    (1, 0)
##    >>> find_two_smallest([3, 3])
##    (0, 0)
##    >>> find_two_smallest([3, 1, 3])
##    (1, 0)
##    """
##
##    # Get a sorted copy of the list so that the two smallest items are at the
##    # front
##    temp_list = sorted(L)
##    smallest = temp_list[0]
##    next_smallest = temp_list[1]
##
##    # Find the indices in the original list L
##    min1 = L.index(smallest)
##    min2 = L.index(next_smallest)
##
##    # Return the two indices:
##    return (min1, min2)

## No 5:
## Answer: an error message occurs saying that 'list index is out of range'.
## Precondition is required in the docstring to avoid using lists that could
## produce these errors, e.g.: precondition: len(L) > 1 
## (NB: The answer in the textbook is wrong, the code must be modified inorder
## to get the answer in the textbook).

## No 6: (Alternative 1 - simplest)

def dutch_flag(color_list):
    """ (List of strings) -> List of strings

    Return color_list rearranged so that all 'red' strings comes first,
    followed by all 'green' strings, and finally all the 'blue' strings,
    thereby representing the dutch national flag.

    >>> dutch_flag(['green', 'green', 'red', 'blue', 'blue', 'blue', 'red'])
    ['red', 'red', 'green', 'green', 'blue', 'blue', 'blue']
    >>> dutch_flag(['red', 'green', 'green', 'red', 'blue', 'blue', 'blue',
                   'red', 'green'])
    ['red', 'red', 'red', 'green', 'green', 'green', 'blue', 'blue', 'blue']
    """

    flag = sorted (color_list, reverse = True)

    return flag


## No 6: (alternative 2 - very very complicated: see answer textbook)

    









        
                







            

    
    
        
    
