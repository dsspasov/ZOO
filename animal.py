from get_json_data import GetJsonData


class Animal:

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self.animal_settings = GetJsonData("database.json")

    def eat(self):
        pass
        #use food type from json and decrement the same food type in zoo
        # by weight*food_weight()

    def grows(self):
        self.age += 1
        if self.weight < self.animal_settings[self.species].get_weight_age():
            self.weight += 1

    def chance_of_dying(self):
        return (
            self.age / self.animal_settings[self.species].get_life_expectancy()
            )
