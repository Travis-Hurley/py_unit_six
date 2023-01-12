# Travis Hurley - Jan - -- - 2023 - Running the birthday paradox
import random
def get_birthdays():
    list_one = []
    n = 2 # change to 23
    for x in range(n):
        list_one.append(random.randint(1, 3)) # change to 365
    return list_one
def is_duplicates(list_one):
    
def main():
    print("Hello! I will run the birthday function for you as many times as you would like!")
    amount = int(input("How many would that be?"))
    for y in range(amount):
        get_birthdays()
        is_duplicates(list_one)
main()

