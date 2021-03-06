from animal import Animal
from random import *


class Zoo:

    MEAT_PRICE = 4
    GREEN_PRICE = 2
    WON_MONEY_FOR_ANIMAL = 60
    AVERAGE_MONTH_LENGHT = 30
    PREGNANCY_REST = 6  # 6 months till animal can get pregnant again

    def __init__(self, capacity=0, budget=0):
        self.animals = []
        self.capacity = capacity
        self.budget = budget

    # Should append object from animal class
    def accomodate_animal(self, new_animal):
        for animal in self.animals:
            if animal.name == new_animal.name:
                raise ValueError('Name already exists!')
        self.animals.append(new_animal)

    def have_money(self):
        return self.budget > 0

    # method with be used one time a month
    def win_money(self):
        for animal in self.animals:
            self.budget += Zoo.WON_MONEY_FOR_ANIMAL * Zoo.AVERAGE_MONTH_LENGHT

    # Method returns price of one meal of all animals for a day
    def feed_animals(self):
        for animal in self.animals:
            if animal.info.food_type() == "carnivore":
                self.budget -= animal.eat() * Zoo.MEAT_PRICE
            elif animal.info.food_type() == "herbivore":
                self.budget -= animal.eat() * Zoo.GREEN_PRICE

    def check_for_dead_animals(self):
        for animal in self.animals:
            if (animal.age) / 12 >= animal.info.life_expectancy():
                self.animals.remove(animal)
                return True
            else:
                return False

    def female_and_pregnat(self, animal):
        return animal.gender == 'female' and animal.pregnant

    def create_baby(self, mother):
        baby_species = mother.species
        baby_name = mother.name + str(randint(1, 10000000))
        baby_gender = choice(['male', 'female'])
        baby_weight = mother.info.newborn_weight()
        mother.pregnant = False
        mother.pregnancy = 0
        return Animal(baby_species, baby_name, baby_gender, 0, baby_weight)

    def update_pregnancy(self, animal):
        if not animal.pregnant:
            raise ValueError('Animal is not pregnant!')
        elif animal.pregnant:
            if animal.pregnancy < animal.gestation_period:
                animal.pregnancy += 1
            else:
                newborn = create_baby(animal)
                self.accomodate_animal(newborn)
                animal.pregnant = False
                animal.pregnancy = 0
                animal.was_pregnant = True
                animal.after_pregnancy = 1
        elif animal.was_pregnant:
            if animal.after_pregnancy < PREGNANCY_REST:
                animal.after_pregnancy += 1
            else:
                animal.was_pregnant = False
                animal.after_pregnancy = 0

    def make_animals(self, male_animal, female_animal):
        if not female_animal.pregnant and not female_animal.was_pregnant:
            female_animal.pregnant = True

    def meet_animals(self):
        for animal_male in self.animals:
            if animal_male.gender == 'male':
                for animal_female in self.animals:
                    if animal_male.species == animal_female.species and animal_female.gender == 'female':
                        self.make_animals(animal_male, animal_female)
