from typing import List, Union, Optional

from sorts.data import ArrayType


def binary_search(sorted_array: ArrayType, seeking_item: Union[int, str]) -> Optional[int]:
    """
    Binary search algorithm
    :param sorted_array:
    :param seeking_item: Seeking item in array
    :return: index of seeking item in array or None
    """
    start_index: int = 0
    end_index: int = len(sorted_array) - 1

    while start_index <= end_index:
        middle_index: int = (start_index + end_index) // 2
        middle_item = sorted_array[middle_index]

        if middle_item == seeking_item:
            return middle_index
        if middle_item > seeking_item:
            end_index = middle_index - 1
        else:
            start_index = middle_index + 1

    return None
