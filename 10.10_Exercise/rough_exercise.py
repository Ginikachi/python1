Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
Enter file to copy: alkaline_metals
Traceback (most recent call last):
  File "C:/Python34/Chap 10 - Reading and Writing Files/10.10_Exercise/rough_read_No1.py", line 2, in <module>
    with open (file, 'r') as alkaline_metals:
FileNotFoundError: [Errno 2] No such file or directory: 'alkaline_metals'
>>> ================================ RESTART ================================
>>> 
Enter file to copy: alkaline_metals.txt
Traceback (most recent call last):
  File "C:/Python34/Chap 10 - Reading and Writing Files/10.10_Exercise/rough_read_No1.py", line 2, in <module>
    with open (file, 'r') as alkaline_metals:
FileNotFoundError: [Errno 2] No such file or directory: 'alkaline_metals.txt'
>>> ================================ RESTART ================================
>>> 
Enter file to copy: alkaline_metals.txt
>>> with open (file, 'r') as alkaline_metals:
	contents = alkaline_metals.read()

	
>>> contents
'beryllium 4 9.012\nmagnesium 12 24.305\ncalcium 20 20.078\nstrontium 38 87.62\nbarium 56 137.327\nradium 88 226\n'
>>> print(contents)
beryllium 4 9.012
magnesium 12 24.305
calcium 20 20.078
strontium 38 87.62
barium 56 137.327
radium 88 226

>>> with open ('alkaline_metals_backup.bak', as backup_file:
	   
SyntaxError: invalid syntax
>>> with open ('alkaline_metals_backup.bak', 'w') as backup_file:
	backup_file.write(contents)

	
107
>>> ================================ RESTART ================================
>>> 
beryllium 4 9.012
magnesium 12 24.305
calcium 20 20.078
strontium 38 87.62
barium 56 137.327
radium 88 226

>>> ## alternative to no 1 above:
>>> filename = input('Which file would you like to back-up? ')
Which file would you like to back-up? alkaline_metals.txt
>>> new_filename= filename + '.bak'
>>> backup = open(new_filename, 'w')
>>> for line in open(filename):
	backup.write(line)

	
18
20
18
19
18
14
>>> backup.close()
>>> with open ('alkaline_metals.txt.bak', 'r') as backup:
	content = backup.read()
	print  (content)

	
beryllium 4 9.012
magnesium 12 24.305
calcium 20 20.078
strontium 38 87.62
barium 56 137.327
radium 88 226

>>> ## No 2:
>>> result = []
>>> with open('alkaline_metals.txt', 'r') as metals:
	fields = line.split
	result.append([fileds])

	
Traceback (most recent call last):
  File "<pyshell#26>", line 3, in <module>
    result.append([fileds])
NameError: name 'fileds' is not defined
>>> alkaline_metals = []
>>> with open('alkaline_metals.txt', 'r') as metals:
	fields = line.split
	alkaline_metals.append([fields])

	
>>> alkaline_metals
[[<built-in method split of str object at 0x02B4B9D0>]]
>>> result = []
>>> with open('alkaline_metals.txt', 'r') as metals:
	a, b, c = line.split
	result.append([a, b, c])

	
Traceback (most recent call last):
  File "<pyshell#37>", line 2, in <module>
    a, b, c = line.split
TypeError: 'builtin_function_or_method' object is not iterable
>>> result = []
>>> with open ('alkaline_metals.txt', 'r') as metals):
	
SyntaxError: invalid syntax
>>> results = []
>>> with open ('alkaline_metals.txt', 'r') as metals:
	fields = line.split()
	result.append([fields])

	
>>> result = []
>>> with open ('alkaline_metals.txt', 'r') as metals:
	fileds = line.split()
	result.append([fields])

	
>>> result
[[['radium', '88', '226']]]
>>> result = []
>>> with open ('alkaline_metals.txt', 'r') as metals:
	for line in metals:
		fields = line.split()
		result.append(fields)

		
>>> result
[['beryllium', '4', '9.012'], ['magnesium', '12', '24.305'], ['calcium', '20', '20.078'], ['strontium', '38', '87.62'], ['barium', '56', '137.327'], ['radium', '88', '226']]
>>> 
>>> alkaline_metals = []
>>> with open ('alkaline_metals.txt', 'r') as metals:
	line = line.strip
	for line in metals:
		fields = line.split()
		result.append(fields)

		
>>> result
[['beryllium', '4', '9.012'], ['magnesium', '12', '24.305'], ['calcium', '20', '20.078'], ['strontium', '38', '87.62'], ['barium', '56', '137.327'], ['radium', '88', '226'], ['beryllium', '4', '9.012'], ['magnesium', '12', '24.305'], ['calcium', '20', '20.078'], ['strontium', '38', '87.62'], ['barium', '56', '137.327'], ['radium', '88', '226']]
>>> 
>>> alkaline_metals = []
>>> with open ('alkaline_metals.txt', 'r') as metals:
	line = line.strip()
	for line in metals:
		fields = line.split()
		alkaline_metals.append(fields)

		
>>> alkaline_metals
[['beryllium', '4', '9.012'], ['magnesium', '12', '24.305'], ['calcium', '20', '20.078'], ['strontium', '38', '87.62'], ['barium', '56', '137.327'], ['radium', '88', '226']]
>>> 
>>> ## No 3. (reading backwards):
>>> 
>>> alkaline_metals = []
>>> with open ('alkaline_metals.txt', 'r') as metals:
	for line in reversed(metals):
		fields = line.split()
		alkaline_metals.append(fields)

		
Traceback (most recent call last):
  File "<pyshell#87>", line 2, in <module>
    for line in reversed(metals):
TypeError: argument to reversed() must be a sequence
>>> alkaline_metals []
SyntaxError: invalid syntax
>>> 
>>> alkaline_metals = []
>>> for line in open ('alkaline_metals.txt'):
	alkaline_metals.append(line.strip().split(' '))

	
>>> alkaline_metals
[['beryllium', '4', '9.012'], ['magnesium', '12', '24.305'], ['calcium', '20', '20.078'], ['strontium', '38', '87.62'], ['barium', '56', '137.327'], ['radium', '88', '226']]
>>> for alkaline in reversed(alkaline_metals):
	print (alkaline)

	
['radium', '88', '226']
['barium', '56', '137.327']
['strontium', '38', '87.62']
['calcium', '20', '20.078']
['magnesium', '12', '24.305']
['beryllium', '4', '9.012']
>>> print(alkaline.strip())
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    print(alkaline.strip())
AttributeError: 'list' object has no attribute 'strip'
>>> print (alkaline_metals)
[['beryllium', '4', '9.012'], ['magnesium', '12', '24.305'], ['calcium', '20', '20.078'], ['strontium', '38', '87.62'], ['barium', '56', '137.327'], ['radium', '88', '226']]
>>> for alkaline in reversed(alkaline_metals):
	print(alkaline.strip())

	
Traceback (most recent call last):
  File "<pyshell#102>", line 2, in <module>
    print(alkaline.strip())
AttributeError: 'list' object has no attribute 'strip'
>>> 
>>> with open ('alkaline_metals.txt', 'r') as metals:
	alkaline_metals = metals.read()

	
>>> alkaline_metals
'beryllium 4 9.012\nmagnesium 12 24.305\ncalcium 20 20.078\nstrontium 38 87.62\nbarium 56 137.327\nradium 88 226\n'
>>> print (alkaline_metals)
beryllium 4 9.012
magnesium 12 24.305
calcium 20 20.078
strontium 38 87.62
barium 56 137.327
radium 88 226

>>> for alklaine in reversed alkaline_metals:
	
SyntaxError: invalid syntax
>>> 
>>> for alkaline in reversed (alkaline_metals):
	print(alkaline)

	


6
2
2
 
8
8
 
m
u
i
d
a
r


7
2
3
.
7
3
1
 
6
5
 
m
u
i
r
a
b


2
6
.
7
8
 
8
3
 
m
u
i
t
n
o
r
t
s


8
7
0
.
0
2
 
0
2
 
m
u
i
c
l
a
c


5
0
3
.
4
2
 
2
1
 
m
u
i
s
e
n
g
a
m


2
1
0
.
9
 
4
 
m
u
i
l
l
y
r
e
b
>>> with open ('alkaline_metals.txt, 'r') as metals:
	   
SyntaxError: EOL while scanning string literal
>>> with open ('alkaline_metals.txt', 'r') as metals:
	alkaline_metals = metals.readlines()

	
>>> alkaline_metals
['beryllium 4 9.012\n', 'magnesium 12 24.305\n', 'calcium 20 20.078\n', 'strontium 38 87.62\n', 'barium 56 137.327\n', 'radium 88 226\n']
>>> for alkaline in reversed(alkaline_metals):
	print(alkaline)

	
radium 88 226

barium 56 137.327

strontium 38 87.62

calcium 20 20.078

magnesium 12 24.305

beryllium 4 9.012

>>> for alkaline in reversed(alkaline_metals):
	print(alkaline.strip())

	
radium 88 226
barium 56 137.327
strontium 38 87.62
calcium 20 20.078
magnesium 12 24.305
beryllium 4 9.012
>>> 
>>> with open ('lynx.txt', 'r') as file:
	Lynx = file.read()

	
>>> print(Lynx)
Annual Number of Lynx Trapped, MacKenzie River, 1821-1934
#Original Source: Elton, C. and Nicholson, M. (1942)
#"The ten year cycle in numbers of Canadian lynx",
#J. Animal Ecology, Vol. 11, 215--244.
#This is the famous data set which has been listed before in
#various publications:
#Cambell, M.J. and Walker, A.M. (1977) "A survey of statistical work on
#the MacKenzie River series of annual Canadian lynx trappings for the years
#1821-1934 with a new analysis", J.Roy.Statistical Soc. A 140, 432--436.
  269. 321. 585. 871. 1475. 2821. 3928. 5943. 4950. 2577. 523. 98.
  184. 279. 409. 2285. 2685. 3409. 1824. 409. 151. 45. 68. 213.
  546. 1033. 2129. 2536. 957. 361. 377. 225. 360. 731. 1638. 2725.
 2871. 2119. 684. 299. 236. 245. 552. 1623. 3311. 6721. 4245. 687.
  255. 473. 358. 784. 1594. 1676. 2251. 1426. 756. 299. 201. 229.
  469. 736. 2042. 2811. 4431. 2511. 389. 73. 39. 49. 59. 188.
  377. 1292. 4031. 3495. 587. 105. 153. 387. 758. 1307. 3465. 6991.
 6313. 3794. 1836. 345. 382. 808. 1388. 2713. 3800. 3091. 2985. 3790.
  674. 81. 80. 108. 229. 399. 1132. 2432. 3574. 2935. 1537. 529.
  485. 662. 1000. 1590. 2657. 3396.

>>>

