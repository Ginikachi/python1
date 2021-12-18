## No 3:

class Member:
    """ A member of a university. """

    def __init__(self, name, address, email):
        """ (Member, str, str, str) -> NoneType

        Create a new member named name, with home address and email address.
        """

        self.name = name
        self.address = address
        self.email = email

    def __str__(self):
        """ (Member) -> str

        Return a string representation of this Member.

        >>> member = Member('Paul', 'Ajax', 'pgries@cs.toronto.edu')
        >>> member.__str__()
        'Paul\\nAjax\\npgries@cs.toronto.edu'
        """

        return '{}\n{}\n{}'.format(self.name, self.address, self.email)

    def __repr__(self):
        """ (Member) -> str

        Return a string representation of this Atom in this format:

            Member("NAME", "ADDRESS", "EMAIL")
        """

        return 'Member("{0}", "{1}", "{2}")'.format(
            self.name, self.address, self.email)

class Student(Member):
    """ A student member at a university. """

    def __init__(self, name, address, email, student_num):
        """ (Member, str, str, str, str) -> NoneType

        Create a new student named name, with home address, email address,
        student number student_num, an empty list of courses taken, and an
        empty list of current courses.
        """

        super().__init__(name, address, email)
        self.student_number = student_num
        self.courses_taken = ['biology', 'geography', 'Mathematics']
        self.courses_taking = ['Physics']

    def __str__(self):
        """ (Member) -> str

        Return a string representation of this Student.

        >>> student = Student('Jen Campbell', 'Toronto',
                        'campbell@cs.toronto.edu', '4321')
        >>> str(student)
        'Jen Campbell\nToronto\ncampbell@cs.toronto.edu\n4321\Coursestaken: \n
                Coursestaking: '
        """

        member_string = super().__str__()

        return '{}\n{}\nCourses taken: {}\nCourses taking: {}'.format(
            member_string,
            self.student_number,
            ', '.join(self.courses_taken),
            ', '.join(self.courses_taking))

    def __repr__(self):
        """ (Member) -> str

        Return a string representation of this Student in this format:

            Student Member("NAME", "ADDRESS", "EMAIL", "STUDENT_NUMBER",
                        COURSES_TAKEN, "COURSES_TAKING")
        """

        member_rep = super().__repr__()

        return 'Student {}, {}, Courses taken: {}, Courses taking: {}'.format(
            member_rep, self.student_number, ', '.join(self.courses_taken),
            ', '.join(self.courses_taking))
    

class Faculty(Member):
    """ A faculty member at a university. """

    def __init__(self, name, address, email, faculty_num):
        """ (Member, str, str, str, str) -> NoneType

        Create a new faculty named name, with home address, email address,
        faculty number faculty_num, and empty list of courses.
        """

        super().__init__(name, address, email)
        self.faculty_number = faculty_num
        self.courses_teaching = []

    def __str__(self):
        """ (Member) -> str

        Return a string representation of this Faculty.

        >>> faculty = Faculty('Paul', 'Ajax', 'pgries@cs.toronto.edu', '1234')
        >>> str(faculty)
        Paul\\nAjax\\npgries@cs.toronto.edu\\n1234\\nCourses: '
        """

        member_string = super().__str__()

        return '{}\n{}\nCourses: {}'.format(
            member_string,
            self.faculty_number,
            ', '.join(self.courses_teaching))

    def __repr__(self):
        """ (Member) -> str

        Return a string representation of this Faculty in this format:

            Student("NAME", "ADDRESS", "EMAIL", "STUDENT_NUMBER",
                        "COURSES_TAKEN: ", "COURSES_TAKING: ")
        """

        member_rep = super().__repr__()

        return 'Faculty {}, {}, Courses teaching: {}'.format(
            member_rep, self.faculty_number, ', '.join(self.courses_teaching))
    
   
