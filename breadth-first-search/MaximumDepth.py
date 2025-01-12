from typing import Optional
from TreeNode import TreeNode
from Constructor import TreeConstructor

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