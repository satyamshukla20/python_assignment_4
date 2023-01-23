#Create animal base class with attribute and related methods then create sub concrete subclass using animal eg of subclass: cow, horse, dog


class Animal:
    def __init__(self,name,type):
        self.name=name
        self.type=type
    
    def __str__(self):
        return "My name is "+self.name+" & I am generated from animal class"

    def Introduction(self):
        print("My name is "+self.name+",My fav food is everything coz I am a generalisation")

class Cow(Animal):
    def __init__(self,name):
        super().__init__(name,type="Cattle")
    
    def Introduction(self):
        print("My name is "+self.name+" & I am generated from my class Cow,My fav food is Grass and I am a Herbivore as and am a "+self.type)

class Dog(Animal):
    def __init__(self,name,type):
        super().__init__(name,type="pet")

    def Introduction(self):
        print("My name is "+self.name+" & I am generated from my class Dog,My fav food is Bones and I am a Carnivore and I am a "+self.type)

class Horse(Animal):
    def __init__(self,name,type):
        super().__init__(name,type="Cattle")

    def Introduction(self):
        print("My name is "+self.name+" & I am generated from my class Horse,My fav food is Nuts and I am a Herbivore and I am a "+self.type)

a=Animal("Anabelle","none")
print(a)
a.Introduction()

b=Cow("Anabelle")
b.Introduction()