Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.

>>> ================================ RESTART ================================
>>> 
Enter file to copy: alkaline_metals.txt
>>> with open(file, 'r') as alkaline_metals:
	contents = alkaline_metals.read()

	
>>> with open ('alkaline_metals_backup.bak', 'w') as backup_file:
	backup_file.write(contents)

	
107
>>> 
>>> ## alternative code to no.1 above:
>>> filename = input('which file would you like to back-up? ')
which file would you like to back-up? alkaline_metals.txt
>>> new_filename = filename + '.bak'
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
>>> 
>>> ## No 2:
>>> alkaline_metals = []
>>> with open ('alkaline_metals.txt', 'r') as metals:
	line = line.strip()
	for line in metals:
		fields = line.split()
		alkaline_metals.append(fields)

		
>>> alkaline_metals
[['beryllium', '4', '9.012'], ['magnesium', '12', '24.305'], ['calcium', '20', '20.078'], ['strontium', '38', '87.62'], ['barium', '56', '137.327'], ['radium', '88', '226']]
>>> 
>>> ## alternative code to No 2 above:
>>> alkaline_metals = []
>>> for line in open ('alkaline_metals.txt'):
	alkaline_metals.append(line.strip().split(' '))

	
>>> alkaline_metals
[['beryllium', '4', '9.012'], ['magnesium', '12', '24.305'], ['calcium', '20', '20.078'], ['strontium', '38', '87.62'], ['barium', '56', '137.327'], ['radium', '88', '226']]
>>> 
>>> ## no 3:
>>> ## Answer: 'We could read the file contents into a data structure, such as
>>> ## a 'list', and then iterate over the 'list' from end(last line) to
>>> ## beginning (first line):
>>> 
>>> with open ('alkaline_metals.txt', 'r') as metals:
	alkaline_metals = metals.readlines()

	
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    with open ('alkaline_metals.txt', 'r') as metals:
FileNotFoundError: [Errno 2] No such file or directory: 'alkaline_metals.txt'
>>> ================================ RESTART ================================
>>> 
['beryllium 4 9.012\n', 'magnesium 12 24.305\n', 'calcium 20 20.078\n', 'strontium 38 87.62\n', 'barium 56 137.327\n', 'radium 88 226\n']
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
>>> ## No 4: see code in read_Lynx.py
>>> ================================ RESTART ================================
>>> 
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

>>> ## No 4: See code in read_smallest_skip.py
>>> ## see data in hebron_modified.txt
>>> ## No 5. See code in read_smallest_skip.py
>>> ## see data in hebron_modified.txt
>>> ================================ RESTART ================================
>>> 
None
>>> 
>>> ## No 6. See code in read_smallest_continue.py
>>> ## see data in hebron.txt

>>> ================================ RESTART ================================
>>> 
55
>>> ##(NB: for No. 5 above, The None is dispalyed because there is no data
>>> ## immediately after the header. Data is seen as from the second line
>>> ## after the header).
>>> 
>>> ## (also with respect to no. 6, try to produce code using 'continue' for
>>> ## when there is NO data immediately after header, but the smallest is still 
>>> ## needed from the rest of data: keep trying this with
>>> ## rough_read_smallest.py and rough_read_multimol.py).

>>> ## See No. 7 code in read_multimol.py in exercise folder.

>>> ## See No. 8 code in read_multimol_serial.py
