from typing import Optional
from TreeNode import TreeNode
from Constructor import TreeConstructor


"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Input: root = [3,9,20,null,null,15,7]
Output: 2

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 
"""
def maximum_depth_binary_tree (root: Optional [TreeNode]) -> int:
    min_depth = 0

    if not root:
        return min_depth

    queue = [(root, 1)]

    while queue:
        node, min_depth = queue.pop(0)
        if not node.left and not node.right:
            return min_depth
        if node.left:
            queue.append((node.left, min_depth + 1))
        if node.right:
            queue.append((node.right, min_depth + 1))
    print(min_depth)
    return min_depth

if __name__ == '__main__':
    constructor = TreeConstructor()
    arr_input = [3,9,20,None, None,15,7]
    root1 = constructor.insert_level_order(arr_input, 0, len(arr_input))

    maximum_depth_binary_tree(root1)