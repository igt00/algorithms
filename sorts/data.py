from typing import List, Union
from random import randint

ArrayType = List[Union[int, str]]


def get_list_of_randint(start_index: int = 0, end_index: int = 50, count: int = 20) -> List[int]:
    """
    Get list with random integer values
    :param start_index: Start available value for list elems
    :param end_index: End available value for list elems
    :param count: Number of items in the list
    :return: List with random integer values
    """
    return [randint(start_index, end_index) for _ in range(count)]
