from typing import List, Union, Optional


def binary_search(sorted_list: List[Union[int, float]], searched_item: Union[int, float]) -> Optional[int]:
    """
    Алгоритм бинарного поиска
    :param sorted_list: отсортированный список
    :param searched_item: искомый элемент
    :return: индекс искомого элемента или None
    """
    start_index: int = 0
    end_index: int = len(sorted_list) - 1

    while start_index <= end_index:
        middle_index: int = (start_index + end_index) // 2
        middle_item = sorted_list[middle_index]

        if middle_item == searched_item:
            return middle_index
        if middle_item > searched_item:
            end_index = middle_index - 1
        else:
            start_index = middle_index + 1

    return None
