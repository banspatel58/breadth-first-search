"""
You are given two binary trees root1 and root2.

Imagine that when you put one of them to cover the other, some nodes of the two trees are
overlapped while the others are not. You need to merge the two trees into a new binary tree.
The merge rule is that if two nodes overlap, then sum node values up as the new value of the
merged node. Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Input: root1 = [1], root2 = [1,2]
Output: [2,2]
"""
from typing import Optional
from TreeNode import TreeNode
from Constructor import TreeConstructor


def merge_trees (root1: Optional [TreeNode], root2: Optional [TreeNode]) -> Optional [TreeNode]:
    if not root1:
        return root2
    elif not root2:
        return root1
    else:
        root = TreeNode(root1.val + root2.val)
        root.left = merge_trees(root1.left, root2.left)
        root.right = merge_trees(root1.right, root2.right)
        return root

if __name__ == '__main__':

    root1_array = [1,3,2,5]
    binary_tree = TreeConstructor()
    root_1 = binary_tree.insert_level_order(root1_array, 0, len(root1_array))

    root2_array = [2,1,3,None,4,None,7]
    root_2 = binary_tree.insert_level_order(root2_array, 0, len(root2_array))

    print(merge_trees(root_1, root_2))


    root3_array = [1]
    root_3 = binary_tree.insert_level_order(root3_array, 0, len(root3_array))

    root4_array = [1,2]
    root_4 = binary_tree.insert_level_order(root4_array, 0, len(root4_array))
    print(merge_trees(root_3, root_4))