class Dog:
    def __init__(self, name, height):
        self.name= name
        self.height = height

    def bark(self):
        print(f"\n{self.name}, goes woof!")

    def jump(self):
        x= self.height*2
        print(f"{self.name} jumps {x} cm high!")

def davids_dog():
    print("Dog name is Rex and it is 50 cum")
    dog=Dog("Rex",50)
    return dog

def sarahs_dog():
    print("\nDog name is Teacup and it is 20 cum")
    dog3=Dog("Teacup",20)
    return dog3

# def bigger_dog():
#     if 

dog1=davids_dog()
dog1.bark()
dog1.jump()
dog2 = sarahs_dog()
dog2.bark()
dog2.jump()
if dog2.height > dog1.height:
    print("\nTeacup is bigger than Rex")
else:
    print("\nRex is bigger than Teacup")