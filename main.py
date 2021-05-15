from base import get_list_of_randint
from binary_search import binary_search
from random import randrange


# Бинарный поиск
sorted_list = sorted(get_list_of_randint())
print(binary_search(sorted_list, sorted_list[randrange(0, len(sorted_list))]))
