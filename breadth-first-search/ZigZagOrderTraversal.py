"""
Given the root of a binary tree, return the zigzag level order
traversal of its nodes' values. (i.e., from left to right,
then right to left for the next level and alternate between).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []

"""

from typing import Optional, List
from TreeNode import TreeNode
from Constructor import TreeConstructor


def zig_zag_order(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []

    queue = [root]
    result = []
    zig_zag = False
    while queue:
        level_nodes = []
        for _ in range(len(queue)):
            node = queue.pop(0)

            level_nodes.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if zig_zag:
            level_nodes.reverse()
        result.append(level_nodes)
        zig_zag = not zig_zag
    print(result)
    return result


if __name__ == '__main__':
    constructor = TreeConstructor()
    arr_input = [3,9,20,None, None,15,7]
    root1 = constructor.insert_level_order(arr_input, 0, len(arr_input))

    zig_zag_order(root1)

