"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""
from collections import deque
from typing import List


def update_matrix (mat: List [List [int]]) -> List [List [int]]:
    rows, cols = len(mat), len(mat [0])

    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    queue = deque()

    for i in range(rows):
        for j in range(cols):
            if mat [i] [j] == 0:
                queue.append((i, j))
            else:
                mat [i] [j] = -1
    while queue:
        row, col = queue.popleft()

        for dr, dc in dirs:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < rows and 0 <= new_col < cols and mat [new_row] [new_col] == -1:
                mat [new_row] [new_col] = mat [row] [col] + 1
                queue.append((new_row, new_col))
    print(mat)
    return mat

if __name__ == '__main__':
    update_matrix([[0,0,0],[0,1,0],[0,0,0]])
    update_matrix([[0,0,0],[0,1,0],[1,1,1]])