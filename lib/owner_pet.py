
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.owner = owner
        self.pet_type = self.check_pet_type(pet_type)
        self.save_pet(self)

    @classmethod
    def check_pet_type(cls, pet_type):
        if pet_type in cls.PET_TYPES:
            return pet_type
        raise Exception
    
    @classmethod
    def save_pet(cls, pet):
        if not isinstance(pet, Pet):
            raise Exception
        cls.all.append(pet)
        

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception
        if pet.pet_type in Pet.PET_TYPES:
            pet.owner = self
    
    def get_sorted_pets(self):
        return sorted(Pet.all, key = lambda pet : pet.name)