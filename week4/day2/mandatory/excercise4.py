import random

def compare_numbers(user_number):
    if not (1 <= user_number <= 100):
        print("Please enter a number between 1 and 100.")
        return
    
    random_number = random.randint(1, 100)
    
    if user_number == random_number:
        print(f"Success! Both numbers are {user_number}.")
    else:
        print(f"Fail! Your number was {user_number} and the generated number was {random_number}.")

# Example usage
user_number = int(input("Enter a number between 1 and 100: "))
compare_numbers(user_number)