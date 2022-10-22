"""
uses quicksort algorithm to sort a list"
"""

def quicksort(array, first = 0, pivot = None):
    """
    This function checks if the recursion of quicksort should stop, if not a new partition happens and it calls itself twice.
    """
    if pivot is None: #makes sure to sort by the first and last index
        pivot = len(array)-1

    if first < pivot: #stops the recursion
        pivot_index = partition(array, first, pivot)
        quicksort(array, first, pivot_index-1)
        quicksort(array, pivot_index+1, pivot)


def partition(array, start, pivot):
    """
    With a pivot a list is rearange such as all the elements in the range of array[start] and array[pivot]
    that are larger than the pivots gets placed on the right of the pivot and those smaller than the pivot gets placed left of the pivot
    """
    pivot_value = array[pivot]
    i = start - 1
    for j in range(start, pivot):
        current = array[j]
        if current <= pivot_value:
            i += 1
            array[i], array[j] = array[j], array[i]
   
    array[pivot], array[i+1] = array[i+1], array[pivot]
    return i + 1
