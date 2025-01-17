"""
Given the root of a binary tree with unique values and the values of two different nodes
of the tree x and y, return true if the nodes corresponding to the values x and y in the
tree are cousins, or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0, and children of each depth k
node are at the depth k + 1.
"""
from collections import deque
from typing import Optional
from TreeNode import TreeNode
from Constructor import TreeConstructor

def is_cousins (root: Optional [TreeNode], x: int, y: int) -> bool:
    if not root:
        return False

    queue = deque()

    queue.append((root, None, 1))
    found_x, x_parent, x_depth = False, None, 0
    found_y, y_parent, y_depth = False, None, 0

    while queue:
        for node in queue:
            if node [0].val == x:
                found_x = True
                x_parent = node [1]
                x_depth = node [2]

            if node [0].val == y:
                found_y = True
                y_parent = node [1]
                y_depth = node [2]

        if found_x and found_y:
            if x_parent != y_parent and x_depth == y_depth:
                print(str(x) + " and " + str(y) + " are cousins")
                return True
            else:
                print(str(x) + " and " + str(y) + " are not cousins")
                return False

        curr_node, parent, depth = queue.popleft()

        if curr_node.left:
            queue.append((curr_node.left, curr_node, depth + 1))

        if curr_node.right:
            queue.append((curr_node.right, curr_node, depth + 1))

if __name__ == '__main__':
    constructor = TreeConstructor()
    arr_input = [1,2,3,4]
    root1 = constructor.insert_level_order(arr_input, 0, len(arr_input))

    is_cousins(root1, 4, 3)

    arr_input2 = [1,2,3,None,4,None,5]
    root2 = constructor.insert_level_order(arr_input2, 0, len(arr_input2))

    is_cousins(root2, 5, 4)

    arr_input3 = [1,2,3,None,4]
    root3 = constructor.insert_level_order(arr_input3, 0, len(arr_input3))
    is_cousins(root3, 2, 3)