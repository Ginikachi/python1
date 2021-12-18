## No 4:

class Nematode:
    """ A microscopic worm """

    def __init__(self, name, length, gender, age):
        """ (Nematode, str, float, str, int) -> NoneType

        Create a new Nematode with body length (in millimeters; they are
        1 mm in length), gender (either hermaphrodite or male), and age (in
        days).

        >>> worm = Nematode('C.elegans', 0.9, 'hermaphrodite', 5)
        >>> worm.name
        C.elegans
        >>> worm.length
        0.9
        >>> worm.gender
        hermaphrodite
        >>> worm.age
        5
        """

        self.name = name
        self.length = length
        self.gender = gender
        self.age = age

    def __str__(self):
        """ (Nematode) -> str

        Return a string representation of this member.

        >>> worm = Nematode('C.elegans', 0.9, 'hermaphrodite', 5)
        >>> str(worm)
        C.elegans\n0.9\nhermaphrodite\n5
        """
        
        return 'Nematode name: {}\nlength: {} mm\ngender: {}\nage: {} days'.format(
            self.name, self.length, self.gender, self.age)
                        
    
    def __repr__(self):
        """ (Nematode) -> str

        Return a string representation of this member in this format:

            Nematode("NAME", Length, "GENDER", Age)
        """

        return 'Nematode("{0}", {1}, "{2}", {3})'.format(
            self.name, self.length, self.gender, self.age)
    

            
                                
