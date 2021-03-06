def read_molecule(reader):
    """ (file open for reading) -> list or NoneType

    Read a single molecule from reader and return it, or return None to signal
    end of file. The first item in the result is the name of the compound;
    each list contains an atom type and the X, Y, and Z coordinates of that
    atom.
    """

    # If there isn't another line, we're at the end of the file.
    reading = True
    while reading:
        line = reader.readline()
        if (line.startswith('CMNT') or line.isspace()):
            continue
        elif not (line.startswith('CMNT') or line.isspace()):
            # Name of the molecule: "Compound   name"
            key, name = line.split()
            molecule = [name]
            reading = False
    
        
    
##        line = reader.readline()
##        key, name = line.split()
##        molecule = [name]
        
##        else:
##            reading = False
##            # Other lines are either "END" or "ATOM num_type x y z"
##            molecule = [name]
##    else:
##        molecule = None

    reading = True
    while reading:
        line = reader.readline()
        if line.startswith('END'):
            reading = False
        elif not (line.startswith('CMNT') or line.isspace()):
            key, num, atom_type, x, y, z = line.split()
            if molecule == None:
                molecule = []
            molecule.append([atom_type, x, y, z])

    return molecule

if __name__ == '__main__':
    molecule_file = open('multimol.txt', 'r')
    molecules = read_molecule(molecule_file)
    print(molecules)


    
##def read_all_molecules(reader):
##    """ (file open for reading) -> list
##    Read zero or more molecules from reader, returning a list of the molecule
##    information.
##    """
##
##    # The list of molecule information.
##    result = []
##
##    reading = True
##    while reading:
##        molecule = read_molecule(reader)
##        if molecule: # None is treated as False in an if statement
##            result.append(molecule)
##        else:
##            reading = False
##    return result
##
##if __name__ == '__main__':
##    molecule_file = open('multimol.txt', 'r')
##    molecules = read_all_molecules(molecule_file)
##    print(molecules)
##
