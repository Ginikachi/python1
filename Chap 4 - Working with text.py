Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> 'Aristotle'
'Aristotle'
>>> "Isaac Newton"
'Isaac Newton'
>>> ''
''
>>> len(' Albert Einstein')
16
>>> len('Albert Einstein')
15
>>> ## len returns the number of chatacters between the opening and closing quotes:
>>> len('')
0
>>> 'Albert' + 'Eistein' ## addition of two strings
'AlbertEistein'
>>> 'Albert' + ' Eistein'
'Albert Eistein'
>>> ## + is called the concatenation operator. If you want to join a string with a number, function str can be applied to the number to get a string representation of it, and then the concatenation can be done:
>>> 
>>> 'Four score and ' str(7) + ' years ago'
SyntaxError: invalid syntax
>>> 'Four score and ' + str(7) + ' years ago'
'Four score and 7 years ago'
>>> int('0')
0
>>> int("11")
11
>>> float('-324')
-324.0
>>> float("56.34")
56.34
>>> 
>>> 'AT' * 5
'ATATATATAT'
>>> 4 * '-'
'----'
>>> ## If the integer is less than or equal to zero, the operator yields the empty string (a string containing no characters):
>>> 
>>> 'GC' * 0
''
>>> 'TATATATA' * -3
''
>>> ## strings are values, so you can assign a string to a variable. Also, operations on strings xan be applied to those variables:
>>> 
>>> sequence = 'ATTGTCCCCC'
>>> len(sequence)
10
>>> new_sequence =  sequence + 'GGCCTCCTGC'
>>> new_sequence
'ATTGTCCCCCGGCCTCCTGC'
>>> new_sequence * 2
'ATTGTCCCCCGGCCTCCTGCATTGTCCCCCGGCCTCCTGC'
>>> 
>>> ## 4.2 USING SPECIAL CHARACTERS IN STRINGS

>>> 'that's not going to work'
SyntaxError: invalid syntax
>>> 
>>> "that's better"
"that's better"
>>> ## above shows that if you want a quote in a string then one simple way is to use double quote around the string. you can also put single quotes around a string conatining a double quote"
>>> 
>>> 'she said, "That is better."'
'she said, "That is better."'
>>> 
>>> ## If you want to put both kinds of quote in one string, you could do this:
>>> 'She said, "That' + "'" + 's hard to read."'
'She said, "That\'s hard to read."'
>>> ## the result is a valid python string. the  backslash above in the result is called an escape character
>>> 'She said, "That\'s hard to read."'
'She said, "That\'s hard to read."'
>>> 'She said,' + '"That' + "'" + 's hard to read."'
'She said,"That\'s hard to read."'
>>> ## The combination of the backslash and the single quote \' is called the escape sequence. The length of an escape sequence is one:
>>> len('\'')
1
>>> len('it\'s')
4
>>> 

>>> ## 4.3 CREATING A MULTILINE STRING
>>> '''one
two
three'''
'one\ntwo\nthree'
>>> '''one
...two
...three'''
'one\n...two\n...three'
>>> ## \n sequence appears wherever our input starts a new line. during printing \n does not show, i.e escape sequences do not show. they see a tab or a quote rather than \t or \'.
>>> 
>>> ## PRINTING INFORMATION
>>> print(1+1)
2
>>> meaning = "The Latin 'Oryctolagus cuniculus' means 'domestic rabbit'."
>>> print meaning
SyntaxError: Missing parentheses in call to 'print'
>>> print (meaning)
The Latin 'Oryctolagus cuniculus' means 'domestic rabbit'.
>>> meaning
"The Latin 'Oryctolagus cuniculus' means 'domestic rabbit'."
>>> print (meaning)
The Latin 'Oryctolagus cuniculus' means 'domestic rabbit'.
>>> 
>>> print('one\ttwo\nthree\tfour')
one	two
three	four
>>> print('''one
two
three''')
one
two
three
>>> print('one\ntwo\nthree')
one
two
three
>>> print('one\ttwo\tthree')
one	two	three
>>> ## Function print takes a comma-separated list of values to print and prints the values with a single space between them and anewline after the last values:
>>> print(1, 2, 3)
1 2 3
>>> ## when called with no arguments, print ends the current line, advancing to the next one:
>>> print()

>>> print(1, 'two', 'three', 4.0)
1 two three 4.0
>>> 
>>> radius = 5
>>> print("The diameter of the circle is", radius * 2, "cm.")
The diameter of the circle is 10 cm.
>>> 
