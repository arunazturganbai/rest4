from Observer import Kitchen, Waiter
from Factory import FoodFactoryImpl, Restaurant

def main():
    food_factory = FoodFactoryImpl()
    restaurant = Restaurant(food_factory)

    kitchen = Kitchen()
    waiter1 = Waiter()
    waiter2 = Waiter()

    kitchen.add_observer(waiter1)
    kitchen.add_observer(waiter2)

    orders = ["Pizza", "Burger", "Pasta"]

    for order in orders:
        food = restaurant.order_food(order)
        kitchen.prepare_order(food)
