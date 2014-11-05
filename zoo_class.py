from animal import Animal
from random import *


class Zoo:

    MEAT_PRICE = 4
    GREEN_PRICE = 2
    WON_MONEY_FOR_ANIMAL = 60
    AVERAGE_MONTH_LENGHT = 30

    def __init__(self, capacity=0, budget=0):
        self.animals = []
        self.capacity = capacity
        self.budget = budget

    # Should append object from animal class
    def accomodate_animal(self, animal):
        # check if name exists
        self.animals.append(animal)

    def not_enought_money(self):
        if self.budget < 0:
            return True
        return False

    # method with be used one time a month
    def win_money(self):
        for animal in self.animals:
            self.budget += Zoo.WON_MONEY_FOR_ANIMAL * Zoo.AVERAGE_MONTH_LENGHT

    # Method returns price of one meal of all animals for a day
    def pay_expanditures(self):
        for animal in self.animals:
            if animal.info.food_type() == "carnivore":
                self.budget -= animal.eat() * Zoo.MEAT_PRICE
            elif animal.info.food_type() == "herbivore":
                self.budget -= animal.eat() * Zoo.GREEN_PRICE

    def check_for_dead_animals(self):
        for animal in self.animals:
            if animal.age >= animal.info.life_expectancy():
                self.animals.remove(animal)
                return True
            else:
                return False

    # If you know what I mean ;)
    def make_animals(self, male_animal, female_animal):
        if male_animal.gender == 'male' and female_animal.gender == 'female':
            if female_animal.pregnancy == 0:
                female_animal.pregnant = True
        else:
            print("Sex happened but baby did not :(")

    def born_animal(self):
        for animal in self.animals:
            if animal.pregnant and animal.pregnancy == animal.info.gestation_period():
                new_generation = create_baby(animal)
                self.animals.append(new_generation)
                return True
            else:
                return False

    def create_baby(self, mother):
        b_species = mother.species
        b_name = animal.name + str(randint(1, 10000000))
        b_gender = choice(['male', 'female'])
        b_weight = mother.info.newborn_weight()
        return Animal(b_species, b_name, b_gender, 0, b_weight)
