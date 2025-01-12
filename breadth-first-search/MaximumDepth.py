from typing import Optional
from TreeNode import TreeNode
from Constructor import TreeConstructor


"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest 
path from the root node down to the farthest leaf node.

Input: root = [3,9,20,null,null,15,7]
Output: 3

Input: root = [1,null,2]
Output: 2
"""
def maximum_depth_binary_tree (root: Optional [TreeNode]) -> int:
    max_depth = 0

    if not root:
        return max_depth

    queue = [(root, 1)]

    while queue:
        node, max_depth = queue.pop(0)

        if node.left:
            queue.append((node.left, max_depth + 1))
        if node.right:
            queue.append((node.right, max_depth + 1))
    print(max_depth)
    return max_depth

if __name__ == '__main__':
    constructor = TreeConstructor()
    arr_input = [3,9,20,None, None,15,7]
    root1 = constructor.insert_level_order(arr_input, 0, len(arr_input))

    maximum_depth_binary_tree(root1)