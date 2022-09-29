from heapq import heappush, heappop


def heap_sort(list):
    """ This method uses a heap to sort an array.
        Time Complexity:  O(n log n)
        Space Complexity: O(1)
    """
    heap = []
    for element in list:
        heappush(heap, element)

    sorted_elements = []

    while len(heap) != 0:
        sorted_elements.append(heappop(heap))

    return sorted_elements