def read_molecule(reader):
    """ (file open for reading) -> list or NoneType

    Read a single molecule from reader and return it, or return None to signal
    end of file. The first item in the result is the name of the compound;
    each list contains an atom type and the X, Y, and Z coordinates of that
    atom.
    """

    # If there isn't another line, we're at the end of the file.
    line = reader.readline()
    if not line:
        return None

    # Name of the molecule: "Compound   name"
    key, name = line.split()

    # Other lines are either "END" or "ATOM num_type x y z"
    molecule = [name]
    number = 0
    line = reader.readline()
    

    # Parse all the atoms in the molecule.
    while not line.startswith('END'):
        key, num, atom_type, x, y, z = line.split()
        molecule.append([atom_type, x, y, z])
        if  not int(num) == number + 1:
            print ('Expected serial number {0}, but got {1}'. format(
                number + 1, num))
        number = number + 1
        line = reader.readline()

    return molecule


####simpler alternative: the section:
##if  not int(num) == number + 1:
##            print ('Expected serial number {0}, but got {1}'. format(
##                number + 1, num))
##
##can be replaced with:  (in this case, number is first assigned 1 not 0
##
##if int(num) != number:
##    print print ('Expected serial number {0}, but got {1}'. format(
##                number, num))


    
def read_all_molecules(reader):
    """ (file open for reading) -> list
    Read zero or more molecules from reader, returning a list of the molecule
    information.
    """

    # The list of molecule information.
    result = []

    reading = True
    while reading:
        molecule = read_molecule(reader)
        if molecule: # None is treated as False in an if statement
            result.append(molecule)
        else:
            reading = False
    return result

if __name__ == '__main__':
    molecule_file = open('multimol.txt', 'r')
    molecules = read_all_molecules(molecule_file)
    print(molecules)

##
##def read_molecule(reader):
##    """ (file open for reading) -> list or NoneType
##    Read a single molecule from reader and return it, or return None to signal
##    end of file. The first item in the result is the name of the compound;
##    each list contains an atom type and the X, Y, and Z coordinates of that
##    atom.
##    """
##    # If there isn't another line, we're at the end of the file.
##    line = reader.readline()
##    if not line:
##        return None
##
##    # Name of the molecule: "COMPND name"
##    key, name = line.split()
##
##    # Other lines are either "END" or "ATOM num atom_type x y z"
##    molecule = [name]
##    reading = True
##
##    while reading:
##        line = reader.readline()
##        if line.startswith('END'):
##            reading = False
##        else:
##            key, num, atom_type, x, y, z = line.split()
##            molecule.append([atom_type, x, y, z])
##
##    return molecule


## Note that the commented 'def read_molecule(reader) code is same as the first
## def read_molecule(reader) code up above. It is just an alternative.    
