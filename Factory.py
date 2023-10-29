
class FoodFactory:
    def create_food(self, food_type):
        pass

class Restaurant:
    def __init__(self, food_factory):
        self.food_factory = food_factory

    def order_food(self, food_type):
        food = self.food_factory.create_food(food_type)
        return food

class Pizza:
    def __str__(self):
        return "Pizza"

class Burger:
    def __str__(self):
        return "Burger"

class FoodFactoryImpl(FoodFactory):
    def create_food(self, food_type):
        if food_type == "Pizza":
            return Pizza()
        elif food_type == "Burger":
            return Burger()
        else:
            return None
