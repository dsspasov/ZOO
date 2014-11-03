class Zoo:
    def __init__(self, capacity=0, budget=0):
        self.animals = []
        self.capacity = capacity
        self.budget = budget

    #Should append object from animal class
    def accomodate_animal(self, animal):
        self.animals.append(animal)

    #Adding some random money.
    def win_money(self):
        self.budget += 1000

    #Taking some random money.
    #Shoudl check if budget < 0
    def pay_expanditures(self):
        self.budget -= 1000

    #Needs more funcitonality
    # def check_for_dead_animals(self):
    #     for animal in self.animals:
    #         if animal.age >= animal.life_expectancy:
    #             self.animals.remove(animal)

    #No ideas
    # def check_if_reproduciton(self):