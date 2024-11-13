favorite_fruits=[]
favorite_fruits=input("Please state your favorite fruits(separate the fruits with a single space):")
favorite_fruits.split()
fruit = input("Please enter a fruit name:")
favorite_fruits.split().sort()
if favorite_fruits == fruit:
    print("You chose one of your favorite fruits! Enjoy!")
else: print("You chose a new fruit. I hope you enjoy")