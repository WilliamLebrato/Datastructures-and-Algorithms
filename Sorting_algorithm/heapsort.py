"""
This module sorts a list using the maxheap sorting algorithm

"""

def heapify(array, size, index):
    """
    array -  the array that we want to sort
    size - the lenght of A
    index - an index, it represents a node in the heap

    This function checks if a node (i) is larger than its children, if its not the node is exchanged with its largest child.
    We now need to check if the new child is larger than its new children and call this function agian on the new child.
    """
    left = 2 * index + 1
    right = 2 * index + 2
    largest = index
    if left < size and array[left] > array[index]:
        largest = left
    if right < size and array[right] > array[largest]:
        largest = right
    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        heapify(array, size, largest)

def extract(array, last):
    """
    The root and the last element in the heap switch position
    """
    array[0], array[last] = array[last], array[0]

def heapsort(array):
    """
    This is the main program of heapsort.

    First it starts building a max heap.
    
    Then it begins extracting elements, it takes the element from the root and switches it with the last element from the heap,
    then the old root is removed from the heap. 

    """
    size = len(array)
    start = size//2  
    for i in range(start, -1, -1): #Reapetition of heapify makes a max heap
        heapify(array, size, i)
    for i in range(size - 1, 0, -1): #The sorted list gets build from back to front
        extract(array, i)
        heapify(array, i, 0)

