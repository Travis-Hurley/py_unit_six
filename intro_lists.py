def swap():
    """
    Function that swaps the first and last elements of the list, regardless of length
    :param list_one: a list of at least two elements
    :return: the same list with the first and last elements swapped
    """
    list_one = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    end = list_one[0]
    start = list_one[-1]
    list_one[0] = start
    list_one[-1] = end
    print(list_one)



def rotate_left():
    """
    Given a list of ints length 3, return a list with the elements "rotated left" so [1, 2, 3] yields [2, 3, 1].
    :param list_one: A list consisting of exactly three integers
    :return: a list where all the elements have been shifted 1 place to the left
    """
    list_one = [1, 2, 3]
    end = list_one[0]
    middle = list_one[2]
    start = list_one[1]
    list_one[0] = start
    list_one[1] = middle
    list_one[2] = end
    print(list_one)
rotate_left()


def max_end():
    """
    This function will find if the first or last element of a list is larger, then set all the elements
    of that list to that value.
    :param list_one: A list consisting of three elements - all integers
    :return: A list where all the elements are the larger of the first or last element of the original list
    """
    list_one=[0, 6, 1]
    first = list_one[0]
    last = list_one[-1]
    if first > last:
        list_one[1] = first
        list_one[-1] = first
    elif first < last:
        list_one[0] = last
        list_one[1] = last
    else:
        list_one[1] = last
    print(list_one)
