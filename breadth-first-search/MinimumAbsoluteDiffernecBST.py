"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference
between the values of any two different nodes in the tree.

Input: root = [4,2,6,1,3]
Output: 1

Input: root = [1,0,48,null,null,12,49]
Output: 1
"""
from collections import deque
from typing import Optional
from TreeNode import TreeNode
from Constructor import TreeConstructor


def get_minimum_difference (root: Optional [TreeNode]) -> int:
    min_heap = []

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        min_heap.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    print(min_heap)
    min_heap = sorted(min_heap)

    min_diff = 10 ** 20
    for i in range(len(min_heap) - 1):
        min_diff = min(min_diff, abs(min_heap [i] - min_heap [i + 1]))

    print("Min Difference: " + str(min_diff))
    return min_diff

if __name__ == '__main__':
    constructor = TreeConstructor()
    arr_input1 = [4,2,6,1,3]
    root1 = constructor.insert_level_order(arr_input1, 0, len(arr_input1))
    get_minimum_difference(root1)

    arr_input2 = [1,0,48,None,None,12,49]
    root2 = constructor.insert_level_order(arr_input2, 0, len(arr_input2))
    get_minimum_difference(root2)