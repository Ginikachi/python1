Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> import math
>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
>>> math.floor(-2.8)
-3
>>> abs(round(-4.3))
4
>>> math.sin(34.5)
0.057487478104924564
>>> math.ceil(math.sin(34.5))
1
>>> ## NO. 2
>>> import calendar
>>> help (calendar.isleap)
Help on function isleap in module calendar:

isleap(year)
    Return True for leap years, False for non-leap years.

>>> calendar.isleap(2021)
False
>>> calendar.isleap(2022)
False
>>> calendar.isleap(2023)
False
>>> calendar.isleap(2024)
True
>>> dir(calendar)
['Calendar', 'EPOCH', 'FRIDAY', 'February', 'HTMLCalendar', 'IllegalMonthError', 'IllegalWeekdayError', 'January', 'LocaleHTMLCalendar', 'LocaleTextCalendar', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'TextCalendar', 'WEDNESDAY', '_EPOCH_ORD', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_colwidth', '_locale', '_localized_day', '_localized_month', '_spacing', 'c', 'calendar', 'datetime', 'day_abbr', 'day_name', 'different_locale', 'error', 'firstweekday', 'format', 'formatstring', 'isleap', 'leapdays', 'main', 'mdays', 'month', 'month_abbr', 'month_name', 'monthcalendar', 'monthrange', 'prcal', 'prmonth', 'prweek', 'setfirstweekday', 'sys', 'timegm', 'week', 'weekday', 'weekheader']
>>> help(calendar.leapdays)
Help on function leapdays in module calendar:

leapdays(y1, y2)
    Return number of leap years in range [y1, y2).
    Assume y1 <= y2.

>>> calendar.leapdays(2000, 2050)
13
>>> calendar.weekday(2016, 7, 29)
4
>>> ## NO 3:
>>> ================================ RESTART ================================
>>> 
>>> import doctest
>>> doctest.testmod()
**********************************************************************
File "C:/Python34/Chap 6 - A Modular Approach to Program Organisation/Exercisemodule.py", line 6, in __main__.average
Failed example:
    average(10, 20)
Expected:
    15.0
Got:
    20.0
**********************************************************************
File "C:/Python34/Chap 6 - A Modular Approach to Program Organisation/Exercisemodule.py", line 8, in __main__.average
Failed example:
    average(2.5, 3.0)
Expected:
    2.75
Got:
    4.0
**********************************************************************
1 items had failures:
   2 of   2 in __main__.average
***Test Failed*** 2 failures.
TestResults(failed=2, attempted=2)
>>> ================================ RESTART ================================
>>> 
>>> import doctest
>>> doctest.testmod()
TestResults(failed=0, attempted=2)
>>> 
