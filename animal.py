from get_json_data import GetJsonData


class Animal:

    def __init__(self, species, name, gender, age, weight):
        self.species = species
        self.age = age * 12
        self.name = name
        self.gender = gender
        self.weight = weight
        self.animal_settings = GetJsonData("database.json")

    #how much food the animal eats in kilos
    #and it can be multiply by the cost of eaten food so we will have the outcomes
    def eat(self):
        return self.weight * self.animal_settings.get_food_weight(self.species)

    def grows(self):
        self.age += 1
        if self.weight < self.animal_settings.get_average_weight(self.species):
            self.weight += self.animal_settings.get_weight_age(self.species)
            if self.weight > self.animal_settings.get_average_weight(self.species):
                self.weight = self.animal_settings.get_average_weight(self.species)

    #We could add dead before max age reached
    def die(self):
        if self.chance_of_dying >= 1:
            return True
        return False

    def chance_of_dying(self):
        return (
            (self.age / 12) / self.animal_settings.get_life_expectancy(self.species)
        )
