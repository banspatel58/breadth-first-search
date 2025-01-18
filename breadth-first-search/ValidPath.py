"""
There is a bidirectional graph with n vertices, where each vertex is labeled
from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D
integer array edges, where each edges[i] = [ui, vi] denotes a bidirectional
edge between vertex ui and vertex vi. Every vertex pair is connected by at most
 one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source
to vertex destination.

Given edges and the integers n, source, and destination, return true if there
is a valid path from source to destination, or false otherwise.

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
"""

from collections import defaultdict, deque
from typing import List


def valid_path_bfs(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque()
    queue.append(source)

    visited = {source}

    while queue:
        node = queue.popleft()

        if node == destination:
            print("Destination Found!!")
            return True

        for key in graph[node]:
            if key not in visited:
                visited.add(key)
                queue.append(key)

    print("Destination Not Found :-(")
    return False


def valid_path_dfs(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    visited = [False] * n
    visited[source] = True
    flag = True
    while flag:
        flag = False
        for edge in edges:
            if visited[edge[0]] != visited[edge[1]]:
                visited[edge[0]] = True
                visited[edge[1]] = True
                flag = True
            if visited[destination]:
                print("Destination Found!!")
                return True
    print("Destination Not Found :-(")
    return False

if __name__ == '__main__':
    valid_path_bfs(3, [[0,1],[1,2],[2,0]], 0, 2)
    valid_path_dfs(3, [[0,1],[1,2],[2,0]], 0, 2)