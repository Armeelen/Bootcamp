class Farm:
    def __init__(self,farm_name):
        self.farm_name=farm_name
        self.animal = {}

    def add_animal(self, animal_name, animal_num=1):
        if animal_name in self.animal:
            self.animal[animal_name] += animal_num
        else:
            self.animal[animal_name] = animal_num

    def get_info(self):
        info=f"{self.farm_name} Farm "
        for animal, count in self.animal.items():
            info += f"{animal}: {count}\n"
        return info    
    def get_animal_types(self):
        self.animal = self.animal
        pass
    def get_short_info():
        pass
        
    
        

macdonald = Farm("Mcdonald")
macdonald.add_animal('Cow',5)
macdonald.add_animal('Sheep')
macdonald.add_animal('Sheep')
macdonald.add_animal('goat',12)
print(macdonald.get_info())