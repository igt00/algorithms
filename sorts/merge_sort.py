from sorts.data import ArrayType


def merge_subarrays(left_subarray: ArrayType, right_subarray: ArrayType) -> ArrayType:
    """
    Merge two sorted subarrays to one sorted array
    :param left_subarray: Left subarray for merging
    :param right_subarray: Right subarray for merging
    :return: One sorted array
    """
    left_length: int = len(left_subarray)
    right_length: int = len(right_subarray)

    if left_length == 0:
        return right_subarray
    if right_length == 0:
        return left_subarray

    left_index = right_index = 0
    result: ArrayType = []

    while len(result) < left_length + right_length:
        if left_subarray[left_index] < right_subarray[right_index]:
            result.append(left_subarray[left_index])
            left_index += 1
        else:
            result.append(right_subarray[right_index])
            right_index += 1

        if len(left_subarray) == left_index:
            result += right_subarray[right_index:]
            break
        if len(right_subarray) == right_index:
            result += left_subarray[left_index:]
            break
    return result


def merge_sort(array: ArrayType) -> ArrayType:
    """
    Merge sorting algorithm
    :param array: Array for sorting
    :return: Sorted array
    """
    array_length: int = len(array)
    if array_length < 2:
        return array

    midpoint = array_length // 2

    left_subarray: ArrayType = merge_sort(array[:midpoint])
    right_subarray: ArrayType = merge_sort(array[midpoint:])
    return merge_subarrays(left_subarray, right_subarray)
