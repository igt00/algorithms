def factorial(x: int) -> int:
    """Факториал числа"""
    if x == 1:
        return 1
    return x * factorial(x - 1)


def print_numbers_of_increase(n: int, x: int = 1) -> None:
    """Вывести все числа по возрастанию от 1 до n"""
    if x == n:
        print(x)
        return
    print(x)
    print_numbers_of_increase(n, x + 1)


def function_ackerman(m: int, n: int) -> int:
    """Вычисление функции Аккермана"""
    if m == 0:
        return n + 1
    if n == 0 and m > 0:
        return function_ackerman(m - 1, 1)
    if m > 0 and n > 0:
        return function_ackerman(m - 1, function_ackerman(m, n - 1))


def check_degree_of_two(x: int, additional_x: int = 1) -> bool:
    """Проверить, является ли число степенью 2"""
    if additional_x == x:
        return True
    if additional_x > x:
        return False
    return check_degree_of_two(x, additional_x * 2)


def amount_of_digits_of_number(x: int) -> int:
    """Сумма цифр числа"""
    if x < 10:
        return x
    return x % 10 + amount_of_digits_of_number(x // 10)


def amount_of_factorial_numbers(x: int) -> int:
    """Найти сумму факториалов числа"""
    if x == 1:
        return 1
    return factorial(x) + amount_of_factorial_numbers(x - 1)
