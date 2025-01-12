"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the
same value.

Input: p = [1,2,3], q = [1,2,3]
Output: true

Input: p = [1,2], q = [1,null,2]
Output: false

Input: p = [1,2,1], q = [1,1,2]
Output: false
"""
from typing import Optional
from TreeNode import TreeNode
from Constructor import TreeConstructor

def same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return same_tree(p.right, q.right) and same_tree(p.left, q.left)

if __name__ == '__main__':
    array_p = [123]
    array_q = [123]
    binary_tree = TreeConstructor()
    p_tree = binary_tree.insert_level_order(array_p, 0, len(array_p))
    q_tree = binary_tree.insert_level_order(array_q, 0, len(array_q))

    print(same_tree(p_tree, q_tree))

