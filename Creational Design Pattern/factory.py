class Bird:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Chirp"

class Cat:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow"

class Dog:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof"

def get_pet(pet="dog"):
    """ The Factory Method """
    pets = dict( dog=Dog("Hope"), cat=Cat("Peace") )

    return pets[pet]

c = get_pet("cat")
d = get_pet("dog")
print( d.speak() )
print( c.speak() )