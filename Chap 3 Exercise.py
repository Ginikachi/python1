Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> ## No 1:
>>> min(2,3,4)
2
>>> max(2,-3,4,7,-5)
7
>>> max(2,-3,min(4,7),-5)
4
>>> 
>>> ## No 3:
>>> 

>>> def tripple(n):
	""" (number) -> number

        Return n trippled.

        >>> tripple(2)
        6
        >>> tripple(0.5)
        1.5
        """
	return 3 * n

>>> tripple(2)
6
>>> tripple(0.5)
1.5
>>> 

>>> ## No 4:
>>> def abs_difference(x, y):
	""" (number, number) -> number

        Return the absolute value of the difference between x and y.

        >>> abs_difference(5, 3)
        2
        >>> abs_difference(3, 5)
        2
        >>>abs_difference(2.5, 1)
        1.5
        """
	return abs(x - y)

>>> abs_difference(5, 3)
2
>>> abs_difference(3, 5)
2
>>> abs_difference(1, 2.5)
1.5
>>> 

>>> ## No 5:
>>> def convert_to_miles(km)
SyntaxError: invalid syntax
>>> 
>>> def convert_to_miles(km):
	""" (number) -> float

        Return the distance km in miles.

        >>> convert_to_miles(8)
        5.0
        """
	return km / 1.6

>>> convert_to_miles (8)
5.0
>>> convert_t0_miles(10)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    convert_t0_miles(10)
NameError: name 'convert_t0_miles' is not defined
>>> convert_to_miles(10)
6.25
>>> 
>>> 

>>> ## No 6:
>>> def average_grade(grade1, grade2, grade3):
	""" (number, number, number) -> number

        Return the average grade of grade1, grade2, and grade3, where each
        grade range from 0 to 100, inclusive.

        >>> average_grade(90, 80, 75)
        81.6666666667
        """
	return (grade1 + grade2 + grade3) / 3

>>> average_grade(90, 80, 70)
80.0
>>> average_grade(90, 80, 75)
81.66666666666667
>>> 

>>> ## No 7:
>>> best_three_avg(grade1, grade2, grade3, grade4):
	
SyntaxError: invalid syntax
>>> def best_three_avg(grade1, grade2, grade3, grade4):
	""" (number, number, number, number) -> number

        Return the average of the best three grades of grade1, grade2,
        grade3, grade4.

        >>> best_three_avg (80, 60, 70, 50)
        70
        """
	total = grade1 + grade2 + grade3 + grade4
	best_three_total = total - min(grade1, grade2, grade3, grade4)
	return best_three_total / 3

>>> best_three_avg(80, 60, 70, 50)
70.0
>>> ## to solve no 7 using the function from No 6:
>>> def best_three_avg(grade1, grade2, grade3, grade4):
	return max(average_grade(grade1, grade2, grade3),
		   average_grade(grade1, grade2, grade4),
		   average_grade(grade1, grade3, grade4),
		   average_grade(grade2, grade3, grade4))

>>> best_three_avg(80, 60, 70, 50)
70.0
>>> 

>>> ## No 8:
>>> def weeks_elapsed(day1, day2):
	""" (int, int) -> int

        day1 and day2 are days in the same year. Return the number of full
        weeks that have elapsed  between the two days.

        >>> weeks_elapsed(3, 20)
        2
        >>> weeks_elapsed(20, 3)
        2
        >>> weeks_elapsed(8, 5)
        0
        >>> weeks_elapsed(40, 61)
        3
        """
	return (abs(day1 - day2)) // 7

>>> weeks_elapsed(3, 20)
2
>>> weeks_elapsed(20, 3)
2
>>> weeks_elapsed(8, 5)
0
>>> weeks_elapsed(40, 61)
3
>>> 

>>> ##No 9:
>>> ##No 10:
>>> def square(num):
	""" (number) -> number

        Return the square of num.

        >>> square(3)
        9
        """

	
>>> def square(num):
	""" (number) -> number

        Return the square of num.

        >>> square(3)
        9
        """
	return num ** 2

>>> square(3)
9
>>> square(2.5)
6.25
>>> square(-2)
4
>>> 
