from pakuri import Pakuri

class DuplicateSpeciesError(Exception):
    pass
# custom exception to be raised when a pakuri with the same species already exists 
class NoneExistantPakuriError(Exception):
    pass
# custom exception when there is no pakuri with specified species input

evolveList = []

class Pakudex:

    def __init__(self, capacity=20):
        self.pakuris = []
        self.capacity = capacity
        self.size = 0
    
    def get_size(self):
        self.size = len(self.pakuris)
        return self.size

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        #If the list is empty returns none
        if not self.pakuris:
            return None
        return self.pakuris

    def get_stats(self, species):
        for pakuri in self.pakuris:
            if pakuri == species:
                pakuriObject = Pakuri(species)
                #Checks to see if the Pakuri is the evolveList. If it is, it will evolve it and then print out the stats
                if species in evolveList:
                    pakuriObject.evolve()
                return [pakuriObject.get_attack(), pakuriObject.get_defense(), pakuriObject.get_speed()]
        return None

    

    # sorts the pakuri array to be listed
    def add_pakuri(self, species):
        for pakuri in self.pakuris:
            if pakuri == species:
                return False

        self.pakuris.append(species)
        return True

    # try catch block that adds a pakuri to the pakudex. When a pakuri already exists in the pakudex then a DuplicateSpeciesError exception is raised
    def evolve_species(self,species):
        for pakuri in self.pakuris:
            if pakuri == species:
                evolveList.append(species)
                return True

        return False

    # try catch block that is used to get stats on a pakuri. When pakuri doesn't exist then an exception is raised. 
    def sort_pakuri(self):
        self.pakuris.sort()
                