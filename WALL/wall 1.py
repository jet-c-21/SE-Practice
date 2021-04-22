class TwilightBus:
    """A bus model that makes passengers vanish"""

    def __init__(self, passengers=[]):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)
