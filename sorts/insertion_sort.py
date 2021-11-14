from sorts.data import ArrayType


def insertion_sort(array: ArrayType) -> ArrayType:
    """
    Insertion sorting algorithm
    :param array: Array for sorting
    :return: Sorted array
    """
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1

        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key_item

    return array
