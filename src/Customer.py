class Customer:

    class FoodUnacceptableException(Exception):
        pass

    def __init__(self, name, favouriteDish, minimumQuality):
        """
        A customer at our restaurant

        Arguments:
            name (string): The name of the customer
            favouriteDish (string): The customer's favourite dish
            minimumQuality (int): The minimum quality that the customer will accept
        """
        self.name = name
        self.favouriteDish = favouriteDish
        self.minimumQuality = minimumQuality

    def orderDish(self, restaurant, dish):
        """
        Order a dish from a particular restaurant

        Arguments:
            restaurant (Restaurant): The restaurant to order from
            dish (string): The dish to order
        """
        # Place the order
        food = restaurant.placeOrder(dish)
        # Make sure the dish was of acceptable quality
        if food.quality >= minimumQuality:
            return "Yum, that %s was delicious!" % food.name
        else:
            raise FoodUnacceptableException("That %s was not of acceptable quality. I expect the food to be of at quality at least %d" % (food.name, self.minimumQuality))
