from animal import Animal


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
    # We will work in months - 60$ day ~ 1800$ month
    def win_money(self):
        for animal in self.animals:
            self.budget += Zoo.WON_MONEY_FOR_ANIMAL * Zoo.AVERAGE_MONTH_LENGHT

    # Method returns price of one meal of all animals for a day
    # assuming they eat twise
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
                new_animal = Animal(animal.species, "alabala", "gender", 0, animal.info.newborn_weight())
                self.animals.append(new_animal)
                return True
            else:
                return False
