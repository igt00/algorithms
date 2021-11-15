from typing import Union, List, Optional


def dfs(
    graph: dict,
    vertex: Union[str, int],
    visited: Optional[List[Union[int, str]]] = None,
) -> List[Union[int, str]]:
    """
    Depth first search algorithm
    :param graph: graph for searching
    :param vertex: start vertex
    :param visited: list of vertexes, who already visited
    :return: list of all vertex with dfs order
    """
    if not visited:
        visited = []
    visited.append(vertex)
    for next_vertex in graph[vertex]:
        if next_vertex not in visited:
            dfs(graph, next_vertex, visited)

    return visited
