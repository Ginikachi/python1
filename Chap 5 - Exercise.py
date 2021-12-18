Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> print("be careful")
be careful
>>> 
>>> ## No 1:
>>> 
>>> True and not False
True
>>> True and not false
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    True and not false
NameError: name 'false' is not defined
>>> 
>>> True or True and False
True
>>> ##(what took place above is short-circuit evaluation)
>>> not True or not False
True
>>> True and not 0
True
>>> 52<52.3
True
>>> 1 + 52 < 52.3
False
>>> 4 != 4.0
False
>>> 
>>> ## No 2:
>>> 
>>> def is_poisitive(x, y):
	"""(number) -> bool

        Return True iff x and y are both positive

        >>> is_positive (2, 3)
        True
        >>> is_positive -4, 4)
        False
        """
	return x > 0 and y > 0

>>> is_positive (2, 3)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    is_positive (2, 3)
NameError: name 'is_positive' is not defined
>>>  def is_positive(x, y):
	 
SyntaxError: unexpected indent
>>> 
>>> def is_positive(x, y):
	"""(number, number) -> bool

        Return True iff x and y are both positive

        >>> is_positive(2, 3)
        True
        >>> is_positive(-4, 4)
        False
        """
	return (x > 0) and (y > 0)

>>> is_positive(2, 3)
True
>>> is_positive(-4, 4)
False
>>> is_positive(5, 0)
False
>>> 
>>> 
>>> ## No 2a: (redo; 2a above still correct but only expressions are asked for)
>>> x = True
>>> y = True
>>> x and y
True
>>> ## No 2b
>>> x = False
>>> y = True
>>> not x
True
>>> ## No 2c:
>>> x = False
>>> y = True
>>> x or y
True
>>> ## No 3:
>>> full = True
>>> empty = False
>>> (full or empty) and not (full and empty)
True
>>> ##(answer below is also correct for no 3 exercise above):
>>> full = True
>>> empty = False
>>> full != empty
True

