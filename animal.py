from get_json_data import GetJsonData


class Animal:

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age * 12
        self.name = name
        self.gender = gender
        self.weight = weight
        self.animal_settings = GetJsonData("database.json")

    def eat(self):
        pass
        #how much food the animal eats in kilos
        #and it can be multiply by the cost of eaten food so we will have the outcomes
        return self.weight * self.animal_settings.get_food_weight(self.species)

    def grows(self):
        self.age += 1
        if (self.weight) < (
                self.animal_settings.get_average_weight(self.species)):
            self.weight += self.animal_settings.get_weight_age(self.species)

    def chance_of_dying(self):
        return (
            (self.age / 12) / self.animal_settings.get_life_expectancy(self.species)
        )
