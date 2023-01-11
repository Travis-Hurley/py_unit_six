#Travis Hurley - Jan - -- - 2023 - Running the birthday paradox
import random
def get_birthdays():
    list_one = []
    n = 2
    for x in range(n):
        list_one.append(random.randint(1, 3))
    return list_one
def is_duplicates(list_one):
    print()
def main():
    print("Hello! I will run the birthday function for you as many times as you would like!")
    while True:
        amount=input("How many would that be?")
        if amount == int:
            break
    for y in range(amount):
        get_birthdays()
