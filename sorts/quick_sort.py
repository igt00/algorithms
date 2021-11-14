from typing import Union

from sorts.data import ArrayType


def quick_sort(array: ArrayType) -> ArrayType:
    """
    Quick sorting algorithm
    :param array: Array for sorting
    :return: Sorted array
    """
    if len(array) < 2:
        return array
    pivot: Union[int, str] = array[0]
    less_elems: ArrayType = [elem for elem in array[1:] if elem <= pivot]
    greatest_elems: ArrayType = [elem for elem in array[1:] if elem > pivot]
    return quick_sort(less_elems) + [pivot] + quick_sort(greatest_elems)
