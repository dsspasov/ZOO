class Zoo:
    def __init__(self, capacity=0, budget=0):
        self.animals = []
        self.capacity = capacity
        self.budget = budget

    #Should append object from animal class
    def accomodate_animal(self, animal):
        self.animals.append(animal)

    def check_if_falit(self):
        if self.budget < 0:
            return True
        return False

    #We will work in months - 60$ day ~ 1800$ month
    def win_money(self):
        for animal in self.animals:
            self.budget += 1800

    #Taking some random money.
    #Shoudl check if budget < 0
    def pay_expanditures(self):
        self.budget -= 1000

    def check_for_dead_animals(self):
        for animal in self.animals:
            if animal.age >= animal.life_expectancy:
                self.animals.remove(animal)

    #If you know what I mean ;)
    def make_animals(self, male_animal, female_animal):
        if male_animal.gender == 'male' and female_animal.gender == 'female':
            if female_animal.pregnancy == 0:
                female_animal.pregnant = True
        else:
            print("Sex happened but baby did not :(")
