from collections import deque
from typing import List, Union


def bfs(graph: list, vertex: Union[str, int]) -> List[Union[int, str]]:
    """
    Breadth first search algorithm
    :param graph: graph for searching
    :param vertex: start vertex
    :return: list of all vertex with bfs order
    """
    search_queue = deque()
    search_queue += [vertex]
    visited = []
    while search_queue:
        person = search_queue.popleft()
        if person not in visited:
            visited.append(person)
            search_queue += graph[person]
    return visited
