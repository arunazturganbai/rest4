class Observer:
    def update(self, message):
        pass

class Subject:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, message):
        for observer in self._observers:
            observer.update(message)

class Kitchen(Subject):
    def prepare_order(self, order):
        print(f"Preparing order: {order}")
        self.notify_observers(f"Order {order} is ready!")

class Waiter(Observer):
    def update(self, message):
        print(f"Received notification: {message}")
