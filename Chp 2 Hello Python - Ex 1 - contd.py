Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ## chapter 2 exercise continued. No 2:
>>> x = -17
>>> x
-17
>>> + x
-17
>>> + -17
-17
>>> ## No 3:
>>> temp = 24
>>> temp
24
>>> ## convert te value in temp from celsius to farenheit by multiplying by 1.8
>>> ## and adding 32: make temp refer to the resulting value:
>>> temp =(temp x 1.8) + 32
SyntaxError: invalid syntax
>>> temp = (temp * 1.8) + 32
>>> temp
75.2
>>> # No 5:
>>> x = 10.5
>>> y = 4
>>> x = x + y
>>> x
14.5
>>> y
4
>>> x
14.5
>>> x = 3
>>> x + = x - x
SyntaxError: invalid syntax
>>> x = 3
>>> x
3
>>> x + = x - x
SyntaxError: invalid syntax
>>> x += x - x
>>> x
3
>>> ## No 6: Write a bullet list description of what happens when python
>>> ## evaluates the statement x += x - x when x has the value of 3
>>> ## Answer : (a): (x - x) is evaluated, yielding 0. (b): 0 is added
>>> ## to the value at x, which is 3, yielding 3.
>>> 
>>> w
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    w
NameError: name 'w' is not defined
>>> ## example of NameError above: When a value is used before it has
>>> ## been assigned a value, a NameError occurs. More examples:
>>> s = t + 6
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    s = t + 6
NameError: name 't' is not defined
>>> 
>>> ## No 8: Which of the following expressions results in SyntaxErrors?
>>> 6 * ...........8
SyntaxError: invalid syntax
>>> 6 * ...8
SyntaxError: invalid syntax
>>> 6 * .8
4.800000000000001
>>> 6 * ..8
SyntaxError: invalid syntax
>>> 8 = people
SyntaxError: can't assign to literal
>>> ((((4**3))))
64
>>> (.(.(.(.5))))
SyntaxError: invalid syntax
>>> (*(*(*(*5))))
SyntaxError: can use starred expression only as assignment target
>>> 4 += 7/2
SyntaxError: can't assign to literal
>>> 4+= 7/2
SyntaxError: can't assign to literal
>>> 
