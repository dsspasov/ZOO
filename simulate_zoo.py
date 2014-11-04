from animal import Animal

from zoo_class import Zoo


class SimultaZoo:

    def __init__(self):
        self.zoo = Zoo()

    def see_animals(self):
        animal_list = self.zoo.animals
        printed_string = ""
        for animal in animal_list:
            printed_string += "{} : {}, {}, {}".format(animal.name, animal.species, animal.age, animal.weight) +"\n"
        #return printed_string
        print(printed_string)

    def acomodate(self, species, age, name, gender, weight):
        animal_x = ANimal(species, age, name, gender, weight)
        self.zoo.acomodate(animal_x)

    def move_to_habitat(self, species, name):
        animal_list = self.zoo.animals
        for animal in animal_list:
            if species == animal.species and name == animal.name:
                self.zoo.remove(animal)
                #i = animal_list.index(animal)
                #self.zoo.pop(i)
    def simulate(self, interval_of_time, period):
        #more things have to be done
        while period != 0:

            for animal in self.zoo.animals:
                animal.grows()

            self.see_animals()
            if self.zoo.is_animal_dead():
                print ("An animal has died")
            else:
                print ("No animals have died")

            if self.zoo.is_animal_born():
                print("An animal has been born")
            else:
                print("No animals hava been born")

            if self.zoo.not_enought_money():
                print ("Not enought money")

            period -= 1

    def main(self):
        command = input ("Enter command >")
        option = command.split(" ") 

        if option[0] == "see_animals":
            self.see_animals()

        if option[0] == "acomodate":
                        #   species,     age       name,     gender   , weight
            self.acomodate(option[1], option[2], option[3], option[4], option[5])

        if option[0] == "move_to_habitat":
                                # species ,   name
            self.move_to_habitat(option[1], option[2])

        if option[0] == "simulate":
            self.simulate(option[1], option[2])