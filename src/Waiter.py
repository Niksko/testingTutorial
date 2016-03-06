class Waiter:

    # This is raised when none of the available chefs know the dish
    class DishUnavailableException(Exception):
        pass

    def __init__(self, name):
        """
        A waiter at our restaurant

        Arguments:
            name (string): The name of the waiter
        """
        self.name = name

    def takeOrder(self, dishName, chefs):
        """
        Try to take an order for a given dish, given some list of chefs. Return the dish to the customer

        Arguments:
            dishName (String): The name of the dish that has been ordered
            chefs (list of Chef): The chefs available to take the order
        """
        order = None
        # See if any of the chefs know the dish
        for chef in chefs:
            if dishName in chef.dishes:
                order = chef.cookDish
                break
        if order is None:
            # None of the chefs knew the dish
            raise DishUnavailableException("Unfortunately none of the chefs know how to make %s" % dishName)
        else:
            return order
