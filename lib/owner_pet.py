class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name, self.pet_type, self.owner = name, pet_type, owner
        if self.pet_type not in Pet.PET_TYPES:
            raise Exception("Pet is not in the list")
        Pet.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return list(filter(lambda pet: pet.owner.name == self.name, Pet.all))

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise TypeError("The value must be an instance of the pet class")

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)
