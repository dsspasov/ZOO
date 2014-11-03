class Animal:

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight

    def eat(self):
        pass

    def grows(self):
        self.age += 1
        self.weight += 1

    def die(self):
        if (self.age/50) > 0.8:
            pass
            #die