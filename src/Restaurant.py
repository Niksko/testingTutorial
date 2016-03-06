from random import choice

class Restaurant:

    def __init__(self, name, waiters, chefs):
        self.name = name
        self.waiters = waiters
        self.chefs = chefs

    def placeOrder(self, dish):
        """
        Place an order for the given dish, using a randomly assigned waiter and passing the list of chefs
        """
        # Get a random waiter
        waiter = choice(self.waiters)
        # Place the order, returning the result
        food = waiter.takeOrder(dish, self.chefs)
        return food
