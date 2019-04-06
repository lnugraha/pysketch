class Dog:
    def speak(self):
        return "Woof!"

    def __str__(self):
        return "Dog"


class DogFactory:
    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog Food"

class PetStore:
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print( "Our pet is {}".format(pet) )
        print( "Our pet speaks {}".format(pet.speak()) )
        print( "Our pet eats {}".format(pet_food) )

# Creates a concrete factory
factory = DogFactory()

# Create a pet store housing our absract factory
shop = PetStore(factory)

# Invoke the utilit method
shop.show_pet()

