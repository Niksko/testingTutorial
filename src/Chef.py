from Dish import Dish, MAX_QUALITY, MIN_QUALITY
from random import gauss

# Define the standard deviation of the normal distribution used to determine quality
QUALITY_SIGMA = 2
# Define the max and minimum possible skills
MAX_SKILL = 10
MIN_SKILL = 0

class Chef:

    # An exception for when the chef doesn't know the dish asked
    class UnkownDishException(Exception):
        pass

    def __init__(self, name, skill = 0, dishes):
        """
        Initializes the chef with a name and a set of dishes that the chef knows how to make

        Arguments:
            name (string): The name of the chef
            skill (int): The skill of the chef, from 0 to 10
            dishes (list of strings): The names of dishes that the chef can make
        """
        self.name = name

        if (skill < MIN_SKILL or skill > MAX_SKILL):
            raise ValueError("Skill must be between %d and %d inclusive, got value %d" % (MIN_SKILL, MAX_SKILL, skill))
        else:
            self.skill = skill

        if not isinstance(dishes, list):
            raise TypeError("Dishes must be of type list, got value of type %s" % str(type(dishes)))
        else:
            self.dishes = dishes

    def cookDish(dish):
        """
        Returns a dish object of the required type if known, otherwise raises an error.
        The quality of the dish depends on the skill of the chef. We use a normal distribution centered around the
        skill of the chef with standard deviation 2
        """
        if dish in self.dishes:
            # We want quality to be an integer, minimum of MIN_QUALITY, max of MAX_QUALITY
            quality = gauss(self.skill, QUALITY_SIGMA)
            if quality < MIN_QUALITY:
                quality = MIN_QUALITY
            else if quality > MAX_QUALITY:
                quality = MAX_QUALITY
            return Dish(name=dish, quality=quality)
        else:
            raise UnkownDishException("This dish is not known by chef %s. Known dishes are: %s" % (self.name, str(self.dishes))
