from typing import Optional
from TreeNode import TreeNode
from Constructor import TreeConstructor

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