# Travis Hurley - Jan - -- - 2023 - Running the birthday paradox
import random
global amount
amount=0
def get_birthdays():
    list_one = []
    n = 2 # change to 23
    for x in range(n):
        list_one.append(random.randint(1, 3)) # change to 365
        print(list_one,"list")
    return list_one
def is_duplicates(list_one):
    while True:
        num = len(list_one)
        x = list_one[0]
        list_one[0:(num - 1)] = list_one[1:num]
        list_one[-1] = x
        list_one.pop[x]
        duplicate = list_one.count(x)
        if duplicate == 1:
            amount += 1
            print(amount,"amount")
            break


def main():
    print("Hello! I will run the birthday function for you as many times as you would like!")
    list_one = int(input("How many would that be?"))
    for y in range(list_one):
        get_birthdays()
        is_duplicates(list_one)
main()
"""
fruits = ["apple", "banana", "cherry"]

x = fruits.count(fruits[0])

print(x)


# Zain's much more elegant solution
def rotate_left(list_one):
    num = len(list_one)
    x = list_one[0]
    list_one[0:(num-1)] = list_one[1:num]
    list_one[-1] = x
    return list_one
list2 = [1, 2, 3, 4]
print(rotate_left(list2))
"""