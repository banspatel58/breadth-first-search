from typing import Optional
from TreeNode import TreeNode
from BinaryTreeConstruction import BinaryTreeConstruction


"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Input: root = [1,2,2,3,4,4,3]
Output: true

Input: root = [1,2,2,null,3,null,3]
Output: false
"""

def is_symmetric (root: Optional [TreeNode]) -> bool:
    if not root:
        return False

def is_mirror(left_child: Optional[TreeNode], right_child: Optional[TreeNode]) -> bool:

    if not left_child and not right_child:
        return True
    if not left_child or not right_child:
        return False

    return (left_child.val == right_child.val) and (is_mirror(left_child.left, right_child.right) and
                                                    is_mirror(left_child.right, right_child.left))

if __name__ == '__main__':

    array_p = [1,2,2,None,3,None,3]
    binary_tree = BinaryTreeConstruction()
    p_tree = binary_tree.insert_level_order(array_p, 0, len(array_p))

    print(is_symmetric(p_tree))