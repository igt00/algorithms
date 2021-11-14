from graphs.data import graph
from sorts.data import get_list_of_randint


array = get_list_of_randint()

# Bubble sorting
from sorts.bubble_sort import bubble_sort
print(bubble_sort(array))

# Insertion sorting
from sorts.insertion_sort import insertion_sort
print(insertion_sort(array))

# Merge sorting
from sorts.merge_sort import merge_sort
print(merge_sort(array))

# Quick sorting
from sorts.quick_sort import quick_sort
print(quick_sort(array))

# Breadth first search
from graphs.breadth_first_search import bfs
print(bfs(graph, 1))

# Depth first search
from graphs.depth_first_search import dfs
print(dfs(graph, 1))
