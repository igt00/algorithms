from random import randint
print('a')


def get_list_of_randint(start_index: int = 0, end_index: int = 50, count: int = 20):
    """Получение списка случайных int чисел от start_index до end_index, элементов в списке - count"""
    return [randint(start_index, end_index) for _ in range(count)]
