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
