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

    def have_money(self):
        if self.budget < 0:
            return True
        return False

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
            # make animal age in ages not in months
            if (animal.age) / 12 >= animal.info.life_expectancy():
                self.animals.remove(animal)
                return True
            else:
                return False

    # If you know what I mean ;)
    def make_animals(self, male_animal, female_animal):
        # print(female_animal.pregnancy)
        # print(female_animal)
        if male_animal.gender == 'male' and female_animal.gender == 'female':
            if female_animal.was_pregnant and female_animal.after_pregnancy != 6:
                female_animal.after_pregnancy += 1
            else:
                if female_animal.pregnancy == 0 and not female_animal.pregnant:
                    female_animal.pregnant = True
                    female_animal.was_pregnant = False
                    female_animal.after_pregnancy = 6
        #        print('f')
        else:
            print("Sex happened but baby did not :(")

    def meet_animals(self):
        for animal_male in self.animals:
            if animal_male.gender == 'male':
                for animal_female in self.animals:
                    if ((animal_male.species == animal_female.species) and (animal_female.gender == 'female')):
                        self.make_animals(animal_male, animal_female)
        #                print('x')

    def create_baby(self, mother):
        baby_species = mother.species
        baby_name = mother.name + str(randint(1, 10000000))
        baby_gender = choice(['male', 'female'])
        baby_weight = mother.info.newborn_weight()
        mother.pregnant = False
        mother.pregnancy = 0
        return Animal(baby_species, baby_name, baby_gender, 0, baby_weight)

    def born_animal(self):
        self.meet_animals()
        for animal in self.animals:
            if animal.gender == 'female':
                self.make_animal_more_pregnant(animal)
                if animal.pregnant and animal.pregnancy == animal.info.gestation_period():
                    new_generation = self.create_baby(animal)
                    self.animals.append(new_generation)
    
                    animal.was_pregnant = True
                    animal.after_pregnancy = 0
                    return True
                else:
                    # print(animal.pregnancy)
                    return False

    def check_animal_pregnancy(self):
        pass

    def make_animal_more_pregnant(self, animal):
        if animal.gender == 'female' and animal.pregnant:
            animal.pregnancy += 1
