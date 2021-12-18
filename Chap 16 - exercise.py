#### No 1 (alternative a)
##import tkinter
##
##window = tkinter.Tk()
##
### The controller
##def click():
##    window.destroy()
##
### The views
##frame = tkinter.Frame(window)
##frame.pack()
##
##button = tkinter.Button(frame, text = "Goodbye", command=click)
##button.pack()
##
##window.mainloop()


#### No 1 (alternative b - preferred option: lambda used)
##
##import tkinter
##
##window = tkinter.Tk()
##frame = tkinter.Frame(window)
##frame.pack()
##
##button = tkinter.Button(frame, text='Goodbye', command=lambda: window.destroy())
##button.pack()
##
##window.mainloop()


## No 2: Write a GUI application with a single button. Initially the button
## is labeled 0, but each time it is clicked, the value on the button increases
## by 1.

##import tkinter
##
##window = tkinter.Tk()
##
### The model.
##counter = tkinter.IntVar()
##counter.set(0)
##
### General controller.
##def click(var):
##    """ Increasement the number var by 1 each time the button is clicked and
##        update var with the result."""
##    
##    var.set(var.get() + 1)
##
### The view.
##frame = tkinter.Frame(window)
##frame.pack()
##
##button = tkinter.Button(frame, textvariable=counter,
##                        command=lambda: click(counter))
##button.pack()
##
##window.mainloop()

#### No 2 (alternative b): see answer textbook

## No 3: What is a more readable way to write the following? x = lambda: y

##def x():
##    return y


#### No 4:
##import tkinter
##from collections import Counter
##
##def count(data, widget):
##    """ Update widget with the total number of As, Ts, Cs, and Gs found in
##    text. """
##    
##    out_data = (data.get('0.0', tkinter.END)).strip()
##    occurences = Counter(out_data)
##
##    total_dna = ''
##    for key, value in occurences.items():
##        final =("Num {0}s: {1} ".format(key, value))
##        total_dna = total_dna + final
##    widget.config(text=total_dna)
##    
##window = tkinter.Tk()
##frame = tkinter.Frame(window)
##frame.pack()
##
##dna = tkinter.Text(frame, height=10, width=40, borderwidth=4,
##                   relief=tkinter.GROOVE)
##dna.pack()
##
##button = tkinter.Button(frame, text='Count',
##                        command=lambda: count(dna, label))
##button.pack()
##
##label = tkinter.Label(frame)
##label.pack()
##
##window.mainloop()

## In the above No 4 code, .strip is used to prevent dictionary from counting
## trailing spaces. See alternative function definiton below:

##Aternative B:
##def count(data, widget):
##    all_data = (data.get('0.0', tkinter.END)).strip()
##    count_data ={}
##    for char in all_data:
##        count_data[char] = all_data.count(char)
##
##    total_dna = ''
##    for key, value in count_data.items():
##        final =("Num {0}s: {1} ".format(key, value))
##        total_dna = total_dna + final
##    widget.config(text=total_dna)

## Alternative C:
## see it in answer textbook. there stringVar is used therefore
## config(used in the two alternative above) is not needed.
## Also note that the specific charaters (ATGC) is used for iteration,
## .strip is not needed. The disadvantge of this method is that if you have a
## large number of distinct characters to count (e.g the 26 alphabets) - it
## will be very cumbersome or practically impossible to list out all the
## alphabets. Therefore the .strip method is still preferred.


#### No 5:
##import tkinter
##window = tkinter.Tk()
##
##def convert_to_celsius(temp1, temp2):
##    """ Convert temperature temp1 degrees fahrenheit to temperature temp2
##        degrees celsius and display the result. """
##    temp2.set((temp1.get() - 32) * (5/9))
##
##def quit(root):
##    root.destroy()
##
##frame = tkinter.Frame(window)
##frame.pack()
##
##label1 = tkinter.Label(frame, text='Temperature in Fahrenheit:')
##label1.pack()
##
##fahrenheit = tkinter.DoubleVar()
##fahrenheit.set('')
##entry = tkinter.Entry(frame, textvariable=fahrenheit)
##entry.pack()
##
##celsius = tkinter.DoubleVar()
##celsius.set('')
##label2 = tkinter.Label(frame, textvariable=celsius)
##label2.pack()
##
##button1 = tkinter.Button(frame, text='Convert',
##                         command=lambda: convert_to_celsius(fahrenheit, celsius))
##button1.pack()
##
##button2 = tkinter.Button(frame, text='Quit', command=lambda: quit(window))
##button2.pack()
##
##window.mainloop()


#### No. 6
##import tkinter
##import tkinter.filedialog as dialog
##window = tkinter.Tk()
##
##class TextEditor:
##    """A simple text editor."""
##    def __init__(self, master):
##
##        self.master = master
##        self.text = tkinter.Text(master)
##        self.text.pack()
##
##        self.menubar = tkinter.Menu(master)
##        self.filemenu = tkinter.Menu(self.menubar)
##        self.filemenu.add_command(label='Save',
##                                  command=lambda: self.save(self.master,
##                                                             self.text))
##        self.filemenu.add_command(label='Quit',
##                                  command=lambda: self.quit(self.master))
##
##        self.menubar.add_cascade(label = 'File', menu=self.filemenu)
##        self.master.config(menu=self.menubar)
##
##    def save(self, root, text):
##        data = text.get('0.0', tkinter.END)
##        filename = dialog.asksaveasfilename(
##            parent=root,
##            filetypes=[('Text', '*.txt')],
##            title='Save as...')
##        writer = open(filename, 'w')
##        writer.write(data)
##        writer.close()
##
##    def quit(self, root):
##        root.destroy()
##
##myapp = TextEditor(window)
##
##window.mainloop()


