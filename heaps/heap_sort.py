from heaps.min_heap import MinHeap


def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n)
        Space Complexity: O(1)
    """
    heap = MinHeap()
    for value in list: 
        heap.add(list)
    index = 0
    while not heap.empty():
        value[index] = heap.remove()
        index += 1
    return value
    