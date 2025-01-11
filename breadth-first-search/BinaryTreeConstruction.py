from typing import List
from TreeNode import TreeNode

class BinaryTreeConstruction:

    def insert_level_order (self, arr: List [int], start: int, end: int) -> TreeNode:
        root = None

        if start < end:
            root = TreeNode(arr [start])

            # Insert Nodes on Left Tree
            root.left = self.insert_level_order(arr, 2 * start + 1, end)

            # Insert Nodes on Right Tree
            root.right = self.insert_level_order(arr, 2 * start + 2, end)

        return root