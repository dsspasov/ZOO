from animal import Animal

from zoo_class import Zoo


class SimultaZoo:

    def __init__(self):
        self.zoo = Zoo()

    def see_animals(self):
        animal_list = self.zoo.animals
        printed_string = ""
        for animal in animal_list:
            printed_string += "{} : {}, {}, {}".format(
                animal.name, animal.species, animal.age, animal.weight) + "\n"
        # return printed_string
        print(printed_string)

    def acomodate(self, species, name, gender, age, weight):
        animal_x = Animal(species, name, gender, age, weight)
        self.zoo.accomodate_animal(animal_x)

    def move_to_habitat(self, species, name):
        animal_list = self.zoo.animals
        for animal in animal_list:
            if species == animal.species and name == animal.name:
                self.zoo.animals.remove(animal)

    def simulate(self, interval_of_time, period):
        # more things have to be done
        while period != 0:

            for animal in self.zoo.animals:
                animal.grows()
                if (animal.chance_of_dying > 0.9):
                    print("An animal is going to die")
            self.see_animals()
            if self.zoo.check_for_dead_animals():
                print ("An animal has died")
            else:
                print ("No animals have died")

            if self.zoo.born_animal():
                print("An animal has been born")
            else:
                print("No animals hava been born")

            if self.zoo.not_enought_money():
                print ("Not enought money")

            period -= 1

    def main(self):
        while True:
            command = input("Enter command >")
            option = command.split(" ")
            if option[0] == "see_animals":
                self.see_animals()

            if option[0] == "acomodate":
                            #   species,     name       gender,     age   , weight
                self.acomodate(
                    option[1], option[2], option[3], option[4], option[5])

            if option[0] == "move_to_habitat":
                                    # species ,   name
                self.move_to_habitat(option[1], option[2])

            if option[0] == "simulate":
                self.simulate(option[1], option[2])

            if option[0] == "finish":
                print("FINISH")
                break


def main():
    a = SimultaZoo()
    a.main()

if __name__ == '__main__':
    main()
