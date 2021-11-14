from sorts.data import ArrayType


def bubble_sort(array: ArrayType) -> ArrayType:
    """
    Bubble sort algorithm
    :param array: Array for sorting
    :return: Sorted array
    """
    array_length: int = len(array)
    for i in range(array_length):
        is_already_sorted: bool = True
        for j in range(array_length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                is_already_sorted = False
        if is_already_sorted:
            break
    return array
