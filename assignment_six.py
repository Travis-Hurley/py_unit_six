# Travis Hurley - Jan/20/2023 - Running the birthday paradox
import random
amount = 0                          # assigns a variable for later use to keep track of amount of duplicates
def intro():
    '''
    explains the simulation to user
    asks user how many times it should run, but does not stop asking until proper answer is given (won't error out)
    :return: the amount of times wanted to run
    '''
    print("Hello! I will run a simulation called the Birthday Paradox.")
    print("It will calculate how many people have the same birthday in a group of 23.")
    while True:                     # Forms loop to restart until positive integer is given
        try:
            number_of_times = int(input("How many times would you like to run the simulation? "))
        except ValueError:          # stops code from ending and an error by restarting the loop
            print("Sorry, I didn't understand your entry. Please enter a positive integer.")
            continue               # restarts loop
        if number_of_times<0:      # does not accsept negitive int and restarts loop
            print("Sorry, I didn't understand your entry. Please enter a positive integer.")
        else:
            return number_of_times
def get_birthdays():
    '''
    forms list of 23 random numbers
    :return: returns list of 23 random numbers
    '''
    list_one = []                  # assigns variable to empty list
    n = 23 # change to 23          # variable for amount of numbers to add
    for x in range(n):             # uses variable to run the loop 23 times
        list_one.append(random.randint(1, 365))  # adds one random int to end of list 23 times
    return list_one
def is_duplicates(random_list):
    '''
    :param random_list: takes random 23 numbers from get_birthdays
    :return: returns true to break the loop
    '''
    global amount                   # recognizes amount as a variable defined before
    v = 0                           # sets variable to be used later as the number to start with in list
    for x in range(0, 23):          # will run 23 times in loop and uses x to keep track of position in list
        v += 1                      # adds one so the list does not compare the same number position in list
        var1 = random_list[x]       # sets variable to the number in list that the loop is checking for
        for w in range(v, 23):      # runs through the list and uses v to not check the same number against itself
            var2 = random_list[w]   # assigns variable to number being checked
            if var2 == var1:        # compares var1 (the number being looked for) to var2 (the number being checked)
                amount += 1         # if they are the same it adds one to the counter of duplicates
                return True         # breaks loop
def main():
    '''
    calls all functions and repeated the simulation the wanted amount of times
    calculates the amount of duplicates and presents to user - along with the goodbye
    '''
    number_of_thymes = intro()          # assigns variable to returned value in intro (amount of simulation runs)
    for y in range(number_of_thymes):   # runs the simulation wanted amount of times
        random_list = get_birthdays()   # assigns variable to random list returned by get_birthdays
        is_duplicates(random_list)      # runs is_duplicates with previous list
    percent=amount/number_of_thymes     # calculates the percentage of times a duplicate was found
    rond = round(percent, 4)            # assigns variable to the amount of times a duplicate was found
    real = rond * 100
    print(real,"% of the classes had duplicates!")  # prints amount of duplicates and says goodbye vvv
    print("This is",amount,"time(s).")
    print("Thank you for playing.")
main()