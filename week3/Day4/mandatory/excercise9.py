price=0
people=int(input("Please state how much people there is:"))
while True:
    age=int(input("Please state your age:"))
    if age>=3 and age<12: price=price +10
    elif age>12: price = price +15
    # elif age<3:price = price +0
    people=people-1
    if people==0:
        print("The total price is :", price, "$")
