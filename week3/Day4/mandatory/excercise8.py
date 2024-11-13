
price=0
while True:
    toppings=[]
    toppings=input("Please enter the toppings on your pizza:")
    print("I will add this topping on your pizza")
    price= price+2.5
    if (toppings=="quit"):
        toppings.split()
        price=price-2.5
        print("Here are the added toppings:", toppings)
        print('The total for the toppings:',price,"$")
        break

