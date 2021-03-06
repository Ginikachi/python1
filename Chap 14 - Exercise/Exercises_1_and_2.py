## No 1a - 1e:

class Country:
    """ Information about a country including its name, it's population, and
    it's area.
    """

    def __init__(self, name, population, area):
        """ (Country, str, int, number) -> NoneType

        Create a new country with name name, and a population of population,
        havind a an area of area.

        >>> canada = Country( \
                'Canada', \
                34482779, \
                9984670)
        >>> canada.name
        'Canada'
        >>> canada.population
        34482779
        >>> canada.area
        9984670
        """

        self.name = name
        self.population = population
        self.area = area

    def is_larger(self, other):
        """ (Country, Country) -> Bool

        Return True iff the area of this Country has a larger than the
        area of other.

        >>> canada = Country('Canada', 34482779, 9984670)
        >>> usa = Country('United States of America', 313914040, 9826675)
        >>> canada.is_larger(usa)
        True
        >>> usa.is_larger(canada)
        False
        """

        return self.area > other.area

    def population_density(self):
        """ (Country) -> number

        Return the population density of this Country.

        >>> canada = Country('Canada', 34482779, 9984670)
        >>> canada.population_density()
        3.4535722262227995
        """

        population_density = self.population / self.area

        return population_density

    def __str__(self):
        """ (Country) -> str

        Return a human-readable string representation of this Country.

        >>> usa = Country('United States of America', 313914040, 9826675)
        >>> print(usa)
        United States of America has a population of 313914040 and is
        9826675 square km.
        """
        return '{} has a population of {} and is {} square km.'.format(
                self.name, self.population, self.area)

    def __repr__(self):
        """ (Country) -> str

        Return concise string representations of this Country.

        >>> canada = Country('Canada', 34482779, 9984670)
        >>> canada
        Country('Canada', 34482779, 9984670)
        >>> [canada]
        [Country('Canada', 34482779, 9984670)]
        """

        return "Country('{0}', {1}, {2})".format(
            self.name, self.population, self.area)


## No 2:

class Continent:
    """ A continent with name name and list of countries it
    contains.
    """

    def __init__(self, name, countries):
        """ (Continent, str, list of str) -> NoneType

        A continent with name name, made up of countries.

        >>> canada = Country('Canada', 34482779, 9984670)
        >>> usa = Country('United States of America', 313914040, 9826675)
        >>> mexico = country.Country('Mexico', 112336538, 1943950)
        >>> countries = [canada, usa, mexico]
        >>> north_america = Continent('North America', countries)
        >>> north_america.name
        'North America'
        >>> for country in north_america.countries:
        ...     print(country)
        Canada has a population of 34482779 and is 9984670 square km.
        United States of America has a population of 313914040 and is 9826675
    square km.
        Mexico has a population of 112336538 and is 1943950 square km.
        """

        self.name = name
        self.countries = countries

    def total_population(self):
        """ (Continent) -> int

        Return the sum of the populations of the countries on this
        continent.

        >>> canada = Country('Canada', 34482779, 9984670)
        >>> usa = Country('United States of America', 313914040, 9826675)
        >>> mexico = Country('Mexico', 112336538, 1943950)
        >>> countries = [canada, usa, mexico]
        >>> north_america = Continent('North America', countries)
        >>> north_america.total_population()
        460733357
        """

        population = []

        for country in self.countries:
            population.append(country.population)

        return sum(population)

    ## Also see answer textbook for alternative answer for 'total_population'.

    def __str__(self):
        """ (Continent) -> str

        Return a human-readable string representation of this Continent.
        >>> canada = Country('Canada', 34482779, 9984670)
        >>> usa = Country('United States of America', 313914040, 9826675)
        >>> mexico = Country('Mexico', 112336538, 1943950)
        >>> countries = [canada, usa, mexico]
        >>> north_america = Continent('North America', countries)
        >>> print(north_america)
        North America
        Canada has a population of 34482779 and is 9984670 square km.
        United States of America has a population of 313914040 and is 9826675
    square km.
        Mexico has a population of 112336538 and is 1943950 square km
        
        """

        res = self.name
        for country in self.countries:
            res = res + '\n' + str(country)

        return res
    

canada = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 313914040, 9826675)
mexico = Country('Mexico', 112336538, 1943950)
mexico = Country('Mexico', 112336538, 1943950)
countries = [canada, usa, mexico]
north_america = Continent('North America', countries)
                                 
    
