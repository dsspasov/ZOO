import json


class GetJsonData:

    def __init__(self, file_name):
        self.file_name = file_name
        self.result = self._file_open(file_name)

    def _file_open(self, file_name):
        file_data = open(file_name, 'r')
        text = file_data.read()
        file_data.close()
        return json.loads(text)["species"]

    def get_species_type(self):
        list_of_keys = []
        for key in self.result.keys():
            list_of_keys.append(key)
        return list_of_keys

    #returns years
    def get_life_expectancy(self, type_of_animal):
        return self.result[type_of_animal]["life_expectancy"]

    #returns carnivore or herbivore
    def get_food_type(self, type_of_animal):
        return self.result[type_of_animal]["food_type"]

    #returns months
    def get_gestation_period(self, type_of_animal):
        return self.result[type_of_animal]["gestation_period"]

    #returns weight in kilos
    def get_newborn_weight(self, type_of_animal):
        return self.result[type_of_animal]["newborn_weight"]

    #returns gained weight for one month in kilo
    def get_weight_age(self, type_of_animal):
        return self.result[type_of_animal]["weight_age"]

    #returns ration of eaten food to current weight
    def get_food_weight(self, type_of_animal):
        return self.result[type_of_animal]["food_weight"]

    #get average max weight
    def get_average_weight(self, type_of_animal):
        return self.result[type_of_animal]["average_weight"]
