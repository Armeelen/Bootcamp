price=0
age = {'rick': 43, 'beth': 13, 'morty': 5, 'summer': 8}
for item in age.values():
    # age=['rick','beth','morty', 'summer']
    if age>=3 and age<12: price=price +10
    elif age>12: price = price +15
    # elif age<3:price = price +0
    # people=people-1
    # if people==0:
    print("The total price is :", price, "$")