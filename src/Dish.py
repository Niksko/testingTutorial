# Define the max and min possible qualities of a dish
MIN_QUALITY = 0
MAX_QUALITY = 10

class Dish:
    def __init__(self, name, quality):
        """
        This sets up the dish with a name and a quality

        Arguments:
            name (string): The name of the dish
            quality (int): The quality of the dish

        Raises:
            TypeError: If the quality is not an integer
            ValueError: If the quality is not within bounds as defined in the constants above
        """
        self.name = name
        if not isinstance(quality, int):
            raise TypeError("Quality must be an integer value, got type %s instead" % str(type(quality)))
        else if quality < MIN_QUALITY or MAX_QUALITY > MAX_QUALITY:
            raise ValueError("Quality must be between %d and %d, got value of %d" % (MIN_QUALITY, MAX_QUALITY, quality))
        else:
            self.quality = quality
