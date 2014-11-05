from get_json_data import GetJsonData


class Animal:

    def __init__(self, species, name, gender, age, weight):
        self.species = species
        self.age = (int)(age) * 12
        self.name = name
        self.gender = gender
        self.weight = weight
        self.pregnant = False
        self.pregnancy = 0
        self.info = GetJsonData("database.json", self.species)

    # how much food the animal eats in kilos
    # and it can be multiply by the cost of eaten food so we will have the
    # outcomes
    def eat(self):
        return self.weight * self.info.food_for_weight()

    def grows(self):
        self.age += 1
        if self.weight < self.info.average_weight():
            self.weight += self.info.gained_weight_for_month()
            if self.weight > self.info.average_weight():
                self.weight = self.info.average_weight()

    # We could add dead before max age reached
    def die(self):
        if self.chance_of_dying >= 1:
            return True
        return False

    def chance_of_dying(self):
        return (
            (self.age / 12) / self.info.life_expectancy()
        )
