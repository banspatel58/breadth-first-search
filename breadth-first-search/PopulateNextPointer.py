"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer
should be set to NULL.

Initially, all next pointers are set to NULL.

Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer
to point to its next right node, just like in Figure B. The serialized output is in level order as connected
by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []

Constraints:

The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000

"""
from collections import deque
from typing import Optional

from TreeNode import TreeNode
from Constructor import TreeConstructor


def connect(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return root

    if not root.left and not root.right:
        root.next = None

    queue = [root]

    while queue:
        node = queue.pop(0)

        if node.left and node.right:
            node.left.next = node.right
            node.right.next = None
            queue.append(node.left)
            queue.append(node.right)
        elif node.left:
            node.left.next = None
        elif node.right:
            node.right.next = None
        else:
            node.next = None

    return root





if __name__ == '__main__':
    constructor = TreeConstructor()
    arr_input = [1,2,3,4,5,6,7]
    root1 = constructor.insert_level_order(arr_input, 0, len(arr_input))
    connect(root1)