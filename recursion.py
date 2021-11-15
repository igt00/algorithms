from typing import Optional, List


def factorial(value: int) -> int:
    """Get factorial by value"""
    if value < 2:
        return 1
    return value * factorial(value - 1)


def print_numbers_of_increase(value: int, x: int = 1) -> None:
    """Print all items between 1 and value"""
    print(x)
    if x == value:
        return
    print_numbers_of_increase(value, x + 1)


def function_ackerman(m: int, n: int) -> Optional[int]:
    """Get Ackerman function"""
    if m == 0:
        return n + 1
    if n == 0 and m > 0:
        return function_ackerman(m - 1, 1)
    if m > 0 and n > 0:
        return function_ackerman(m - 1, function_ackerman(m, n - 1))
    return None


def check_degree_of_two(value: int, additional_value: int = 1) -> bool:
    """Check that value is degree of two"""
    if additional_value == value:
        return True
    if additional_value > value:
        return False
    return check_degree_of_two(value, additional_value * 2)


def amount_of_digits_of_number(value: int) -> int:
    """Get amount of digits by value"""
    if value < 10:
        return value
    return value % 10 + amount_of_digits_of_number(value // 10)


def amount_of_factorial_number(value: int) -> int:
    """Get amount of factorial by value"""
    if value == 1:
        return 1
    return factorial(value) + amount_of_factorial_number(value - 1)


def get_amount_elems_from_array(array: List[int]):
    """Get amount of all elems from array"""
    if not array:
        return 0
    return array[0] + get_amount_elems_from_array(array[1:])


def get_max_elem_from_array(array: List[int]) -> int:
    """Get max item from array"""
    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    sub_max: int = get_max_elem_from_array(array[1:])
    return array[0] if array[0] > sub_max else sub_max
