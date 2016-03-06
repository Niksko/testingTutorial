from Dish import Dish
from random import gauss

# Define the standard deviation of the normal distribution used to determine quality
QUALITY_SIGMA = 2

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

        if (skill < 0 or skill > 10):
            raise ValueError("Skill must be between 0 and 10 inclusive")
        else:
            self.skill = skill

        if not isinstance(dishes, list):
            raise TypeError("Dishes must be of type list")
        else:
            self.dishes = dishes

    def cookDish(dish):
        """
        Returns a dish object of the required type if known, otherwise raises an error.
        The quality of the dish depends on the skill of the chef. We use a normal distribution centered around the
        skill of the chef with standard deviation 2
        """
        if dish in self.dishes:
            quality = gauss(self.skill, QUALITY_SIGMA)
            return Dish(name=dish, quality=quality)
        else:
            raise UnkownDishException("This dish is not known by chef %s" % self.name)
