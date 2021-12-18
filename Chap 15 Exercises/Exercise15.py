## See unittest code in No1TestPreceding.py

## No. 1 (given code):

##def double_preceding(values):
##    """ (list of number) -> NoneType
##
##    Replace each item in the list with twice the value of the
##    preceding item, and replace the first item with 0.
##
##    >>> L = [1, 2, 3]
##    >>> double_preceding(L)
##    >>> L
##    [0, 2, 4]
##    """
##
##    if values != []:
##        temp = values[0]
##        values[0] = 0
##        for i in range(1, len(values)):
##            values[i] = 2 * temp
##            temp = values[i]
    

#### No. 1 (corrected code) (alternative 1):
##
##def double_preceding(values):
##    """ (list of number) -> NoneType
##
##    Replace each item in the list with twice the value of the
##    preceding item, and replace the first item with 0.
##
##    >>> L = [1, 2, 3]
##    >>> double_preceding(L)
##    >>> L
##    [0, 2, 4]
##    """
##
##    if values != []:
##        values_main = values[:]
##        temp = values_main[0]
##        values[0] = 0
##        for i in range(1, len(values)):
##            values[i] = 2 * temp
##            temp = values_main[i]



#### No. 1 (corrected code) (alternative 2 - more straight forward):
##
##def double_preceding(values):
##
##
##    if values != []:
##        temp = values[0]
##        values[0] = 0
##        for i in range(1, len(values)):
##            double = 2 * temp
##            temp = values[i]
##            values[i] = double
##
#### The bug in the first code of Exercise 1 (i.e code before correction), is
#### inside the for loop. Instead of doubling the value of the item to be
####  overwritten (i.e the original item), it doubles the computed value. The
#### for loop needs to store the next vlaue to read before overwriting it (see
#### alternative 2 correction)


## No. 2:
## SEE ANSWER TEXTBOOK FOR ANSWER AND DETAILED EXPLANATION


#### No. 3:
##
##def all_prefixes(item):
##    """ (str) -> NoneType
##
##    Returns the set of all nonempty substrings that start with the
##    first letter of string item.
##
##    >>> item = "lead"
##    >>> all_prefixes(item)
##    {"l", "le", "lea", "lead"}
##    >>> item = 'x'
##    >>> all_prefixes(item)
##    {'x'}
##    >>> item = ''
##    all_prefixes(item)
##    set()
##    """
##
##    count = 0
##    if item != '':
##        substring = [item[0]]
##
##        if len(item) > 1:
##            for i in range(1, len(item)):
##                substring.append(substring[count] + item[i])
##                count = count + 1
##                set_substring = set(substring)
##        else:
##            set_substring = set(substring)
##    else:
##        set_substring = set()
##        
##
##    return set_substring

#### No. 4:
##
##def is_sorted(L):
##    """ (List of int) -> NoneType
##
##    Return True if List of integers L is sorted in nondecreasing order
##    and returns False otherwise.
##
##    >>> L = [1, 2, 3]
##    True
##    >>> L = [1, 2, 2, 3]
##    True
##    >>> L = [1, 3, 1]
##    False
##    """
##    
##    for i in range(len(L)-1):
##        if not L[i+1] >= L[i]:
##            return False
##    return True
        
#### No. 5 (given code):
##
##def find_min_max(values):
##    """ (list) -> NoneType
##
##    Print the minimum and maximum value from values.
##    """
##
##    min = None
##    max = None
##    for value in values:
##        if value > max:
##            max = value
##        if value < min:
##            min = value
##
##    print('The minimum value is {0}'.format(min))
##    print('The maximum value is {0}'.format(max))


#### No 5 (corrected code):
##
##def find_min_max(values):
##    """ (list) -> NoneType
##
##    Print the minimum and maximum value from values.
##    """
##
##    min = None
##    max = None
##    for value in values:
##        if max is None or value > max:
##            max = value
##        if min is None or value < min:
##            min = value
##
##    print('The minimum value is {0}'.format(min))
##    print('The maximum value is {0}'.format(max))
        

## Correction explained: The first time the if-blocks in the for-loop are
## executed (see 'given code'), the value is compared with None. Since such
## comparisons are not allowed in Python, the code throws an Error. To fix it,
## you will need to change the for-loop (see corrected code).
## NB: == can also be used in place of 'is' e.g in line 161, the if sentence
## can be written as:    if max == None or value > max:


## No 6 (Given code):

def average(values):
    """ (list of number) -> number

    Return the average of the numbers in values. Some items in values are
    None, and they are not counted toward the average.

    >>> average([20, 30])
    25.0
    >>> average([None, 20, 30])
    25.0
    """

    count = 0 # The number of values seen so far.
    total = 0 # The sum of the values seen so far.
    for value in values:
        if value is not None:
            total += value

        count += 1

    return total / count

## No 6 (Corrected code):

def average(values):
    """ (list of number) -> number

    Return the average of the numbers in values. Some items in values are
    None, and they are not counted toward the average.

    >>> average([20, 30])
    25.0
    >>> average([None, 20, 30])
    25.0
    """

    count = 0 # The number of values seen so far.
    total = 0 # The sum of the values seen so far.
    for value in values:
        if value is not None:
            total += value
            count += 1

    if count == 0:
        return None

    return total / count
