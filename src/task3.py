class Animal:
    """
        A parent class which will be inherited by child classes (Dog & Cat)
    """

    legs = 4

    def __init__(self, name):
        self.name = name

    def identity(self):
        return self.name
    
    def has_legs(self):
        return f"{self.name} has {4} legs"

    def can_reproduce(self):
        return "yes"


class Dog(Animal):

    def __init__(self, name):
        self.name = name

    def makes_sound(self):
        return "whoof..."

    def pack_member(self):
        return "yes"


class Cat(Animal):

    def __init__(self, name):
        self.name = name
    
    def makes_sound(self):
        return "meow..."

    def solitaty_member(self):
        return "yes"
