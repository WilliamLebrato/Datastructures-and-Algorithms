"""
This module uses the insertion sort algorithm to sort a list
"""
def insertionsort(array):
    """This function has loop that goes thru from index 1 to the last element.
    It compares an element with the one previous in the list, if its smaller they switch places, if its larger it stays on place."""
    size = len(array)
    for i in range(1, size):
        j = i - 1
        while array[j] > array[i] and i > 0:
            array[j], array[i] = array[i], array[j]
            j -= 1
            i -= 1
    return array
