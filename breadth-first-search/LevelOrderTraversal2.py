"""
Given the root of a binary tree, return the bottom-up level order traversal of
its nodes' values. (i.e., from left to right, level by level from leaf to root).

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []
"""
from typing import Optional, List
from TreeNode import TreeNode
from Constructor import TreeConstructor


def level_order2(root: Optional[TreeNode]) -> List[List[int]]:
    result = []
    if not root:
        return result

    queue = [root]
    while queue:
        level_nodes = []
        for i in range(len(queue)):
            node = queue.pop(0)
            level_nodes.append(node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        result.append(level_nodes)

    result.reverse()
    print(result)
    return result

if __name__ == '__main__':
    constructor = TreeConstructor()
    arr_input = [3,9,20,None,None,15,7]
    root1 = constructor.insert_level_order(arr_input, 0, len(arr_input))

    level_order2(root1)