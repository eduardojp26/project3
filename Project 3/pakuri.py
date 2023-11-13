# first class pakuri from instructions 
class Pakuri:
    #define all the mandatory methods and behaviors 
    def __init__(self, species): 
        self.species = species
        self.attack = (len(species) * 7) + 9
        self.defense = (len(species) * 5) + 17
        self.speed = (len(species) * 6) + 13

 # getter: retrive the attribute value
    def get_species(self):
        return self.species

    def get_attack(self):
        return self.attack

    def get_defense(self):
        return self.defense

    def get_speed(self):
        return self.speed

 #setter: update the attribute's value
    def set_attack(self, new_attack):
        self.attack = new_attack
 #Update self.attack, self.defense, and self.speed
 # a) double the attack; b) quadruple the defense; and c) triple the speed 
    def evolve(self):
        self.attack *= 2
        self.defense *= 4
        self.speed *= 3