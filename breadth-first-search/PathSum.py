"""
Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf
path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There are two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.
Example 3:

Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""

from typing import Optional

from TreeNode import TreeNode
from Constructor import TreeConstructor


def path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False

    if not root.left and not root.right:
        return root.val == target_sum
    print(target_sum)
    left_sum = path_sum(root.left, target_sum - root.val)
    right_sum = path_sum(root.right, target_sum - root.val)

    return left_sum or right_sum


if __name__ == '__main__':
    constructor = TreeConstructor()
    arr_input = [5,4,8,11,None,13,4,7,2,None,None,None,1]
    root1 = constructor.insert_level_order(arr_input, 0, len(arr_input))

    print(path_sum(root1, 22))