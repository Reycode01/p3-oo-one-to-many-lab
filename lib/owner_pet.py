PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if not isinstance(name, str):
            raise Exception("Pet name must be a string.")
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        if not isinstance(owner, Owner):
            owner = None
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    def __str__(self):
        return f"Pet(name={self.name}, type={self.pet_type}, owner={self.owner.name if self.owner else 'None'})"

class Owner:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Owner name must be a string.")
        self.name = name
        self.pets = []
        Owner.all.append(self)

    def __str__(self):
        return f"Owner(name={self.name}, pets={self.pets})"

    def pets(self):
        return self.pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet class.")
        self.pets.append(pet)
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets, key=lambda pet: pet.name)