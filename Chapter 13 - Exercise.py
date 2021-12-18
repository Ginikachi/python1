#### 1 a: While Loop version:
#### (alternative 1 - much preferred - it checks form the back using positive
#### indexing):
##def linear_search(lst, value):
##    """ (list, object) -> int
##
##    Return the index of the first occurence of value in lst, or return -1
##    if value is not in list.
##
##    >>> linear_search([2, 5, 1, -3], 5)
##    1
##    >>> linear_search([2, 4, 2], 2)
##    0
##    >>> linear_search([2, 5, 1, -3], 4)
##    -1
##    >>> linear_search([], 5)
##    -1
##    """
##
##    i = len(lst) - 1   # The index of the next item in lst to examine.
##
##    # Keep going until we reach the end of lst or until we find value.
##    while i != -1 and lst[i] != value:
##        i = i - 1
##
##    # If we fell off the end of the list, we didn't find value.
##    if i == -1:
##        return -1
##    else:
##        return i



#### 1 a: while loop version (alternative 2 - it checks
#### from the back using negative indexing):
##def linear_search(lst, value):
##    """ (list, object) -> int
##
##    Return the index of the first occurence of value in lst, or return -1
##    if value is not in list.
##
##    >>> linear_search([2, 5, 1, -3], 5)
##    -3
##    >>> linear_search([2, 4, 2], 2)
##    -1
##    >>> linear_search([2, 5, 1, -3], 4)
##    0
##    >>> linear_search([], 5)
##    0
##    """
##
##    i = -1 # The negative index of the next item in lst to examine from the back
##
##    # Keep going until we reach the end of lst or until we find value
##    while i != (-len(lst)) - 1 and lst[i] != value:
##        i = i - 1
##
##    # If we fell off the end of the list moving backwards, we didn't find value.
##    if i == (-len(lst)) - 1:
##        return 0
##    else:
##        return i


#### No 1 b - The for loop version (looping backwards with positive indexing):
##
##def linear_search(lst, value):
##    """ (list, object) -> int
##
##    Return the index of the first occurence of value in lst, or return -1
##    if value is not in list.
##
##    >>> linear_search([2, 5, 1, -3], 5)
##    1
##    >>> linear_search([2, 4, 2], 2)
##    0
##    >>> linear_search([2, 5, 1, -3], 4)
##    -1
##    >>> linear_search([], 5)
##    -1
##    """
##
##    # descending sequence of indices with a step size of -1
##    for i in range(len(lst) - 1, -1, -1):
##        if lst[i] == value:
##            return i
##
##    return -1


#### No 1 c - The sentiniel search version (looping backward with +ve indexing):
##
##def linear_search(lst, value):
##    """ (list, object) -> int
##
##    Return the index of the first occurence of value in lst, or return -1
##    if value is not in list.
##
##    >>> linear_search([2, 5, 1, -3], 5)
##    1
##    >>> linear_search([2, 4, 2], 2)
##    0
##    >>> linear_search([2, 5, 1, -3], 4)
##    -1
##    >>> linear_search([], 5)
##    -1
##    """
##
##    # Add the sentinel.
##    lst.insert(0, value)
##
##    i = len(lst) - 1
##
##    # Keep going until we find value.
##    while lst[i] != value:
##        i = i - 1
##
##    # Remove the sentinel(lst.remove(v) removes the first occurence of v in a
##    # list, you can also use lst.pop(index of the value))
##    
##    lst.remove(value)
##
##    # If we reached the beginning of the list we didn't find value.
##    if i == 0:       # (because the value at index 0 is the sentinel)
##        return -1
##    else:
##        # When we inserted, we shifted everything one to the right. Substract
##        # to account for that.
##        return i - 1


## No 2: The one with the highest index if found.

## No 3: See answer textbook for the answer and its explanation

#### No 4a:
##
##from sorts import find_min
##
##L = [6, 5, 4, 3, 7, 1, 2]
##
##i = 0
##
##while i != len(L):
##    smallest = find_min(L, i)
##    L[i], L[smallest] = L[smallest], L[i]
##    i = i + 1
##    print (L)


#### No 4b:
##
##from sorts import insert
##
##L = [6, 5, 4, 3, 7, 1, 2]
##
##i = 0
##
##while i != len(L):
##    insert(L, i)
##    i = i + 1
##    print (L)

## (see answer textbook for explanation of answers gotten from the code in 4a&b)

## No 5 a:

# until all items are sorted:
#    sweep through the list.
#         for each pair of items in the unsorted part of the list
#         if the first element in the pair is greater than the second element:
#             swap them.

## No 5 b:


# The end of the unsorted section. the largest item will be placed here.
# end = len(L) - 1  

# keep going until there is no more item to consider.
# while end != -1:    

#       sweep through the list.
#       for i in range (0, end):

#            if L[i] > L[i + 1]:
#               [i], L[i + 1] = L[i + 1], L[i]

#       end = end - 1


#### No 5 c and D. (using doctest):
##
##def bubble_sort(L):
##    """ (list) -> NoneType
##
##    Reorder the items in L from smallest to largest.
##
##    >>> bubble_sort([3, 4, 7, -1, 2, 5])
##    [-1, 2, 3, 4, 5, 7]
##    >>> bubble_sort([])
##    []
##    >>> bubble_sort([1])
##    [1]
##    >>> bubble_sort([2, 1])
##    [1, 2]
##    >>> bubble_sort([1, 2])
##    [1, 2]
##    >>> bubble_sort([3, 3, 3])
##    [3, 3, 3]
##    >>> bubble_sort([-5, 3, 0, 3, -6, 2, 1, 1])
##    [-6, -5, 0, 1, 1, 2, 3, 3]
##    >>> bubble_sort([7, 6, 5, 4, 3, 2, 1])
##    [1, 2, 3, 4, 5, 6, 7]
##    """
##
##    end = len(L) - 1
##    while end != -1:
##        for i in range(0, end):
##            if L[i] > L[i + 1]:
##                L[i], L[i + 1] = L[i + 1], L[i]
##
##        end = end - 1
##
##    return L


## No 6 a:

# until all items are sorted:
#       sweep through the list from the end to the beginning.
#           for each pair of items in the unsorted part of the list:
#           if the last element in the pair is less than the first element:
#                 swap them.

## No 6 b:

# The beginning of the unsorted section. The smallest item will be placed
# here.
# beginning = 0 

# keep going until there is no more item to consider.
# while beginning < len(L):     

#       sweep through the list.
#       for i in range (len(L) - 1, beginning, -1):

#            if L[i] < L[i - 1]:
#               [i], L[i - 1] = L[i - 1], L[i]

#       beginning = beginning + 1


#### No 6 c and d:
##
##def bubble_sort(L):
##    """ (list) -> NoneType
##
##    Reorder the items in L from smallest to largest.
##
##    >>> bubble_sort([3, 4, 7, -1, 2, 5])
##    [-1, 2, 3, 4, 5, 7]
##    >>> bubble_sort([])
##    []
##    >>> bubble_sort([1])
##    [1]
##    >>> bubble_sort([2, 1])
##    [1, 2]
##    >>> bubble_sort([1, 2])
##    [1, 2]
##    >>> bubble_sort([3, 3, 3])
##    [3, 3, 3]
##    >>> bubble_sort([-5, 3, 0, 3, -6, 2, 1, 1])
##    [-6, -5, 0, 1, 1, 2, 3, 3]
##    >>> bubble_sort([7, 6, 5, 4, 3, 2, 1])
##    [1, 2, 3, 4, 5, 6, 7]
##    """
##
##    beginning = 0
##    while beginning < len(L):
##        for i in range(len(L) - 1, beginning, -1):
##            if L[i] < L[i - 1]:
##                L[i], L[i - 1] = L[i - 1], L[i]
##
##        beginning = beginning + 1
##
##    return L
##
##
## No 7:
##
##import time
##import random
##from sorts import selection_sort
##from sorts import insertion_sort
##from sorts_timing import built_in
##
##
##def print_times(L):
##    """ (list) -> NoneType
##
##    Print the number of milliseconds it takes for selection sort, insertion
##    sort, and list.sort to run.
##    """
##
##    print(len(L), end='\t')
##    for func in (selection_sort, insertion_sort, bubble_sort, built_in):
##        if func in (selection_sort, insertion_sort, built_in) and len(L) > 10000:
##            continue
##
##        L_copy = L[:]
##        t1 = time.perf_counter()
##        func(L_copy)
##        t2 = time.perf_counter()
##        print("{0:7.1f}".format((t2 - t1) * 1000.), end='\t')
##
##    print() # Print a newline.
##
##for list_size in [10, 1000, 2000, 3000, 4000, 5000, 10000]:
##    L = list(range(list_size))
##    random.shuffle(L)
##    print_times(L)
##
### Answer explanation to the result of No 7 code:
### Bubble_sort is the worst of all of them probably because many swaps are
### performed to put one item in place.
##

## No 8:
## Answer the explanation is given in the tectbook. read to understand it:
## (in general more time is likely required since before insertion, there will
## (likely be some shifting of values which are above the value to be inserted).

## (Also see answer in anwer textbook to know if it makes any sense).

## No 9:
## Answer is based on timing and preference. Also see answer textbook for their
## own answer.

## No 10: 

def merge (L1, L2):
    """ (list, list) -> list

    Merge sorted lists L1 and L2 into a new list and return that new list.
    >>> merge([1, 3, 4, 6], [1, 2, 5, 7])
    [1, 1, 2, 3, 4, 5, 6, 7]
    """

    newL = []
    i1 = 0
    i2 = 0

    # For each pair of items L1[i1] and L2[i2], copy the smaller into newL.
    while not (i1 == len(L1) and i2 == len(L2)): #( must not be end of list at
                                                   # the same time)
        if i2 == len(L2) or (i1 != len(L1) and L1[i1] <= L2[i2]):
            newL.append(L1[i1])
            i1 += 1
        else:
            newL.append(L2[i2])
            i2 += 1

    return newL
        

    

