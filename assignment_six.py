# Travis Hurley - Jan - -- - 2023 - Running the birthday paradox
import random
global amount

def get_birthdays():
    list_one = []
    n = 23 # change to 23
    for x in range(n):
        list_one.append(random.randint(1, 365)) # change to 365
    print(list_one)
    return list_one
def is_duplicates(random_list):
    amount = 0
    v = 0
    for x in range(0, 23):
        v += 1
        var1 = random_list[x]
        for w in range(v, 23):
            var2 = random_list[w]
            if var2 == var1:
                amount += 1
                print(amount)
                return True

"""
def main():
    while True:
        try:
            list_one = int(input("How many times would you like to run the simulation? "))
        except ValueError:
            print("Sorry, I didn't understand your entry. Please enter a positive integer.")
            continue
        else:
            break
    for y in range(list_one):
        get_birthdays()
        is_duplicates(list_one)
"""
def main():
    while True:
        try:
            # instead of "list_one" you better call this next variable something else (e.g. number 0f times), because you are re-using this name elsewhere.
            number_of_times = int(input("How many times would you like to run the simulation? "))
        except ValueError:
            print("Sorry, I didn't understand your entry. Please enter a positive integer.")
            continue
        else:
            break
    for y in range(number_of_times):
        random_list = get_birthdays() # you were just calling the function... you need to assign it to something (e.g "random list)
        is_duplicates(random_list) # and then you need to pass it to the next process
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